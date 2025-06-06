# Managing in-app purchases

**Framework**: App Store Connect API

Learn how to create and manage in-app purchases with the App Store Connect API.

#### Overview

The App Store Connect API lets you create and configure in-app purchases for your app. After you create an in-app purchase, you can add metadata, such as a display name and description, and choose your in-app purchase pricing. Once your app is fully configured, you’re able to submit your in-app purchase for review. After approval, you can also schedule pricing changes and edit some metadata for your in-app purchases.

##### Review App Store Connect Api Usage

To manage in-app purchases with the App Store Connect API, you need to understand key concepts for using the API. If you’re new to using the App Store Connect API, make sure to read the documentation in the Essentials section of [`Schedule price changes`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-in-app-purchases/schedule-price-changes) and learn how to create API keys, generate JWTs, identify rate limits, and more.

To create and manage in-app purchases, be sure you have one of the following user roles:

- `ACCOUNT_HOLDER`
- `ADMIN`
- `APP_MANAGER`

For the full list of App Store Connect user roles, see [`UserRole`](userrole.md) and [`Program Roles`](https://developer.apple.comhttps://developer.apple.com/support/roles).

##### Create Your in App Purchase

To create an in-app purchase, use `POST /v2/inAppPurchases` ([`Create an In-App Purchase`](post-v2-inapppurchases.md)) with a payload that contains the required information, including an internal name, a product ID, the in-app purchase type, a review note, and territory availability. Additionally, supply the Apple ID of the app that contains this in-app purchase.

Here’s an example payload:

```other
{
  "data": {
    "type": "inAppPurchases",
    "attributes": {
      "name": "Seattle Neighborhood Coffee Map",
      "productId": "MAPNEIGHBORHOODS",
      "inAppPurchaseType": "CONSUMABLE",
      "reviewNote": "This is a neighborhood map for helping to find awesome coffee shops.",
      "availableInAllTerritories": true
    },
    "relationships": {
      "app": {
        "data": {
          "type": "apps",
          "id": "6446148572"
        }
      }
    }
  }
}
```

Here’s an example response, truncated for clarity:

```other
{
    "data": {
        "type": "inAppPurchases",
        "id": "6446452615",
        "attributes": {
            "name": "Neighborhood Coffee Map",
            "productId": "MAPNEIGHBORHOODS",
            "inAppPurchaseType": "CONSUMABLE",
            "state": "MISSING_METADATA",
            "isAppStoreReviewInProgress": false,
            "submitWithNextAppStoreVersion": false,
            "reviewNote": "This is a neighborhood map for helping to find awesome coffee shops.",
            "familySharable": false,
            "contentHosting": null,
            "clearedForSaleForAllTerritories": true,
            "availableInAllTerritories": true
        }   
```

Make note of the `id` in the response because you use this ID to look up or edit the in-app purchase in the future.

```other
"id": "6446452615"
```

To look up a specific in-app purchase, use the `id` with `GET /v2/inAppPurchases/{id}` ([`Read In-App Purchase Information`](get-v1-inapppurchases-_id_.md)). You can also look up all in-app purchases for an app using `GET /v1/apps/{id}/inAppPurchasesV2` ([`List All In-App Purchases for an App V1`](get-v1-apps-_id_-inapppurchases.md)). Note that this is a `v1` endpoint.

Editing an in-app purchase is similar, but you use `PATCH /v2/inAppPurchases/{id}` ([`Modify an In-App Purchase`](patch-v2-inapppurchases-_id_.md)). The editable fields are `name`, `availableInAllTerritories`, and `reviewNote`.

> **Note**:  The `familySharable` field is editable only for auto-renewable subscriptions and non-consumable in-app purchases.

 The `familySharable` field is editable only for auto-renewable subscriptions and non-consumable in-app purchases.

##### Localize Metadata for Your in App Purchase

To make your in-app purchase ready for consumption, add localized display names and descriptions. Use `POST /v1/inAppPurchaseLocalizations` ([`List All Localizations for an In-App Purchase`](get-v2-inapppurchases-_id_-inapppurchaselocalizations.md)) with a payload that describes the locale, the localized display name, and the localized description for the in-app purchase.

Here’s an example payload:

```other
{
  "data": {
    "type": "inAppPurchaseLocalizations",
    "attributes": {
      "locale": "en-US",
      "name": "Seattle Neighborhood Coffee Map",
      "description": "This is a neighborhood map for helping to find awesome coffee shops."
    },
    "relationships": {
      "inAppPurchaseV2": {
        "data": {
          "type": "inAppPurchases",
          "id": "6446452615"
        }
      }
    }
  }
}
```

Here’s an example response, truncated for clarity:

```other
{
  "data": {
    "type": "inAppPurchaseLocalizations",
    "id": "d7195d00-386d-4389-bef6-bdf196f30e3a",
    "attributes": {
      "name": "Seattle Neighborhood Coffee Map",
      "locale": "en-US",
      "description": "This is a neighborhood map for helping to find awesome coffee shops.",
      "state": "PROPOSED",
      "submitted": false
    },
```

##### Manage Pricing for Your in App Purchase

To set a price point for your in-app purchase, look up the `id` of the price point you want to assign to the in-app purchase. The following example uses the price point `4.99`.

To look up the price point ID, use the [`List All Price Points for an In-App Purchase`](get-v2-inapppurchases-_id_-pricepoints.md) endpoint:

```other
GET /v2/inAppPurchases/{id}/pricePoints?filter[territory]=USA&include=territory&limit=200
```

> 💡 **Tip**:  Filter the API endpoint to reduce the amount of data you need to review.

 Filter the API endpoint to reduce the amount of data you need to review.

Here’s an example response, truncated for clarity:

```other
    "type" : "inAppPurchasePricePoints",
    "id" : "NjQ0NjQ1MjYxNV91c180",
    "attributes" : {
      "customerPrice" : "3.99",
      "proceeds" : "0.0",
      "priceTier" : "4"
    },
    "relationships" : {
      "territory" : {
        "data" : {
          "type" : "territories",
          "id" : "USA"
        }
      },
      "equalizations" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/inAppPurchasePricePoints/NjQ0NjQ1MjYxNV91c180/relationships/equalizations",
          "related" : "https://api.appstoreconnect.apple.com/v1/inAppPurchasePricePoints/NjQ0NjQ1MjYxNV91c180/equalizations"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/inAppPurchasePricePoints/NjQ0NjQ1MjYxNV91c180"
    }
  }, {
    "type" : "inAppPurchasePricePoints",
    "id" : "NjQ0NjQ1MjYxNV91c181",
    "attributes" : {
      "customerPrice" : "4.99",
      "proceeds" : "0.0",
      "priceTier" : "5"
    },
    "relationships" : {
      "territory" : {
        "data" : {
          "type" : "territories",
          "id" : "USA"
        }
      },
      "equalizations" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/inAppPurchasePricePoints/NjQ0NjQ1MjYxNV91c181/relationships/equalizations",
          "related" : "https://api.appstoreconnect.apple.com/v1/inAppPurchasePricePoints/NjQ0NjQ1MjYxNV91c181/equalizations"
        }
      }
    },
```

Note that the ID for the `4.99` price point is `NjQ0NjQ1MjYxNV91c181`. You use this value in the following step.

To add a price point to an in-app purchase, use `POST /v1/inAppPurchasePriceSchedules` ([`Add a scheduled price change to an in-app purchase`](post-v1-inapppurchasepriceschedules.md)). The first ID is the ID of the in-app purchase, and the final ID is that of the price point.

> ❗ **Important**:  Review carefully because once a price increase goes into effect, your change can’t be reverted. Be sure to review information about price increases and changes at [`App Store Connect for iPhone and iPad`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/).

 Review carefully because once a price increase goes into effect, your change can’t be reverted. Be sure to review information about price increases and changes at [`App Store Connect for iPhone and iPad`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/).

Here’s an example payload:

```other
{
  "data": {
    "type": "inAppPurchases",
    "id": "6446452615",
    "attributes": {},
    "relationships": {
      "prices": {
        "data": [
          {
            "type": "inAppPurchasePrices",
            "id": "${price1}"
          }
        ]
      }
    }
  },
  "included": [
    {
      "type": "inAppPurchasePrices",
      "id": "${price1}",
      "attributes": {
        "startDate": null
      },
      "relationships": {
        "inAppPurchaseV2": {
          "data": {
            "type": "inAppPurchasesV2",
            "id": "6446452615"
          }
        },
        "inAppPurchasePricePoint": {
          "data": {
            "type": "inAppPurchasePricePoints",
            "id": "NjQ0NjQ1MjYxNV91c181"
          }
        }
      }
    }
  ]
}
```

##### Submit Your in App Purchase

After you configure an in-app purchase, you need to submit it to App Review for approval before it can be available to users. The first step in getting an in-app purchase ready for review is to upload a screenshot to App Review to show what the in-app puchase looks like to users.

You accomplish this task by using the `/v1/inAppPurchaseAppStoreReviewScreenshots` endpoint. This workflow is similar to the existing image workflows for App Clip images and app screenshots.

In the case of the in-app purchase screenshot, you submit a single image using the following steps:

1. Make an image reservation with `POST /v1/inAppPurchaseAppStoreReviewScreenshots` ([`Create an In-App Purchase Review Screenshot`](post-v1-inapppurchaseappstorereviewscreenshots.md)).
2. Upload the image using the `PUT` URL provided in the response to the previous `POST`.
3. After your image uploads, use `PATCH /v1/inAppPurchaseAppStoreReviewScreenshots/{id}` ([`Commit a Review Screenshot for an In-App Purchase`](patch-v1-inapppurchaseappstorereviewscreenshots-_id_.md)) to commit the image.
4. Finally, use `GET /v1/inAppPurchaseAppStoreReviewScreenshots/{id}` ([`Read In-App Purchase Review Screenshot Information`](get-v1-inapppurchaseappstorereviewscreenshots-_id_.md)) to confirm that the image is in place.

For more information, see [`Uploading Assets to App Store Connect`](uploading-assets-to-app-store-connect.md).

After you upload your screenshot for App Review, the next step is submission.

> ❗ **Important**:  You need to submit your first in-app purchase with an app binary submission. This must be done through [`appstoreconnect.apple.com`](https://developer.apple.comhttps://appstoreconnect.apple.com). For subsequent in-app purchases, you can submit using the following API endpoint without an associated app binary submission.

 You need to submit your first in-app purchase with an app binary submission. This must be done through [`appstoreconnect.apple.com`](https://developer.apple.comhttps://appstoreconnect.apple.com). For subsequent in-app purchases, you can submit using the following API endpoint without an associated app binary submission.

If this isn’t your first in-app purchase, use `POST /v1/inAppPurchaseSubmissions` ([`Create a Review Submission for an In-App Purchase`](post-v1-inapppurchasesubmissions.md)) with a payload like this:

```other
{
  "data": {
    "type": "inAppPurchaseSubmissions",
    "relationships": {
      "inAppPurchaseV2": {
        "data": {
          "type": "inAppPurchases",
          "id": "6446452615"
        }
      }
    }
  }
}
```

##### Promote Your in App Purchase

After your in-app purchase gets approved, you can to promote it to users who visit your app listing in the App Store. To accomplish this task, use `POST /v1/promotedPurchases` ([`Promote a Purchase`](post-v1-promotedpurchases.md)) with a payload that includes your Apple ID and the ID for your in-app purchase. The response confirms the state is `"Waiting for Review"`. You can also look up the state of a specific promoted purchase by using `GET /v1/promotedPurchases` ([`Read Promoted Purchase Information for an In-App Purchase`](get-v2-inapppurchases-_id_-promotedpurchase.md)), or look up the status of all your promoted purchases by using `GET /v1/apps/{id}/promotedPurchases` ([`List All Promoted Purchases for an App`](get-v1-apps-_id_-promotedpurchases.md)).

Here’s an example payload:

```other
{
  "data": {
    "type": "promotedPurchases",
    "attributes": {
      "visibleForAllUsers": true,
      "enabled": true
    },
    "relationships": {
      "app": {
        "data": {
          "type": "apps",
          "id": "6446148572"
        }
      },
      "inAppPurchaseV2": {
        "data": {
          "type": "inAppPurchases",
          "id": "6446452615"
        }
      }
    }
  }
}
```

Promoted purchase images are icons that are displayed in an App Store listing next to promoted purchase metadata. Each promoted purchase has a single image associated and displayed next to the name of the promoted purchase. The upload process is similar to the App Review screenshot process, but with the `/v1/promotedPurchaseImages` endpoint. Use the same `POST`, `PUT`, `PATCH`, and `GET` steps. For more information, see [`Uploading Assets to App Store Connect`](uploading-assets-to-app-store-connect.md).

##### Update in App Purchase Prices

At some point, you might want to change the price of your in-app purchase. Use one of these two methods:

- Make an immediate change of price.
- Schedule a price change for a future time.

To perform either type of price change, you use a process similar to setting the initial price. First, look up your current price point using `GET /v1/inAppPurchasePriceSchedules/{id}/manualPrices` ([`Read in-app purchase price schedule information`](get-v1-inapppurchasepriceschedules-_id_.md)) — where `id` is the in-app purchase ID — to determine the desired price point. The following screenshot shows what the current pricing looks like in App Store Connect for the in-app purchase.

![Screenshot of a price schedule from appstoreconnect.apple.com.](https://docs-assets.developer.apple.com/published/b6a27ee1110af1eae7eba4fbc79faf6b/media-4054484%402x.png)

The following example request includes several additional fields and filters:

```other
GET /v1/inAppPurchasePriceSchedules/6446148560/manualPrices?fields%5BinAppPurchasePricePoints%5D=priceTier&filter%5Bterritory%5D=USA&include=inAppPurchasePricePoint 
```

Here’s an example response that includes the information from the request above:

```other
{
  "data" : [ {
    "type" : "inAppPurchasePrices",
    "id" : "eyJpIjoiNjQ0NjE0ODU2MCIsImQiOjAsImMiOiJVU0EifQ",
    "attributes" : {
      "startDate" : null
    },
    "relationships" : {
      "inAppPurchasePricePoint" : {
        "data" : {
          "type" : "inAppPurchasePricePoints",
          "id" : "NjQ0NjE0ODU2MF91c18y"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/inAppPurchasePrices/eyJpIjoiNjQ0NjE0ODU2MCIsImQiOjAsImMiOiJVU0EifQ"
    }
  }, {
    "type" : "inAppPurchasePrices",
    "id" : "eyJpIjoiNjQ0NjE0ODU2MCIsImQiOjE5MjAxLCJjIjoiVVNBIn0",
    "attributes" : {
      "startDate" : "2022-07-28"
    },
    "relationships" : {
      "inAppPurchasePricePoint" : {
        "data" : {
          "type" : "inAppPurchasePricePoints",
          "id" : "NjQ0NjE0ODU2MF91c18xMA"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/inAppPurchasePrices/eyJpIjoiNjQ0NjE0ODU2MCIsImQiOjE5MjAxLCJjIjoiVVNBIn0"
    }
  } ],
  "included" : [ {
    "type" : "inAppPurchasePricePoints",
    "id" : "NjQ0NjE0ODU2MF91c18y",
    "attributes" : {
      "priceTier" : "2"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/inAppPurchasePricePoints/NjQ0NjE0ODU2MF91c18y"
    }
  }, {
    "type" : "inAppPurchasePricePoints",
    "id" : "NjQ0NjE0ODU2MF91c18xMA",
    "attributes" : {
      "priceTier" : "10"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/inAppPurchasePricePoints/NjQ0NjE0ODU2MF91c18xMA"
    }
  } ],
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/inAppPurchasePriceSchedules/6446148560/manualPrices?include=inAppPurchasePricePoint&filter%5Bterritory%5D=USA&fields%5BinAppPurchasePricePoints%5D=priceTier"
  },
  "meta" : {
    "paging" : {
      "total" : 2,
      "limit" : 50
    }
  }
}
```

This first portion of the response is shown below. This portion shows an `inAppPurchasePrices` with `id`, but the `startDate` attribute is `null`, which means this is the current price. You can look up the customer price for a particular territory by looking up the `inAppPurchasePricePoints` by `id` using `GET /v2/inAppPurchases/{id}/pricePoints` ([`List All Price Points for an In-App Purchase`](get-v2-inapppurchases-_id_-pricepoints.md)) and searching the response for the ID.

```other
{
  "data" : [ {
    "type" : "inAppPurchasePrices",
    "id" : "eyJpIjoiNjQ0NjE0ODU2MCIsImQiOjAsImMiOiJVU0EifQ",
    "attributes" : {
      "startDate" : null
    },
    "relationships" : {
      "inAppPurchasePricePoint" : {
        "data" : {
          "type" : "inAppPurchasePricePoints",
          "id" : "NjQ0NjE0ODU2MF91c18y"
        }
      }
    },
```

The second portion of the response is shown below. This portion shows another `inAppPurchasePrices` with `id`, but the `startDate` attribute is an ISO 8601 formatted date that shows the date the price of the in-app purchase will change. This portion of the response also has a different `inAppPurchasePricePoints` `id`, showing a change of price.

```other
"included" : [ {
    "type" : "inAppPurchasePricePoints",
    "id" : "NjQ0NjE0ODU2MF91c18y",
    "attributes" : {
      "priceTier" : "2"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/inAppPurchasePricePoints/NjQ0NjE0ODU2MF91c18y"
    }
  }, {
    "type" : "inAppPurchasePricePoints",
    "id" : "NjQ0NjE0ODU2MF91c18xMA",
    "attributes" : {
      "priceTier" : "10"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/inAppPurchasePricePoints/NjQ0NjE0ODU2MF91c18xMA"
    }
  } ],
```

By using extra parameters and filters, you can also see the `priceTier` for the current and upcoming price change:

```other
GET /v2/inAppPurchases/{id}/pricePoints?fields%5BinAppPurchasePricePoints%5D=priceTier&filter%5Bterritory%5D=USA&include=inAppPurchasePricePoint
```

Now that you know about the current price and the scheduled price change, you might want to schedule another price change, like reverting back to the original price. To accomplish this task, use `POST /v1/inAppPurchasePriceSchedules` ([`Add a scheduled price change to an in-app purchase`](post-v1-inapppurchasepriceschedules.md)) with a payload like this:

```other
{
  "data": {
    "type": "inAppPurchasePriceSchedules",
    "relationships": {
      "inAppPurchase": {
        "data": {
          "type": "inAppPurchases",
          "id": "6446452615"
        }
      },
      "manualPrices": {
        "data": [
          {
            "type": "inAppPurchasePrices",
            "id": "${prices-id}"
          },
          {
            "type": "inAppPurchasePrices",
            "id": "${prices-id-1}"
          }
        ]
      }
    }
  },
  "included": [
    {
      "type": "inAppPurchasePrices",
      "id": "${prices-id}",
      "attributes": {
        "startDate": "2022-06-29"
      },
      "relationships": {
        "inAppPurchaseV2": {
          "data": {
            "type": "inAppPurchases",
            "id": "6446452615"
          }
        },
        "inAppPurchasePricePoint": {
          "data": {
            "type": "inAppPurchasePricePoints",
            "id": "NjQ0NjE0ODU2MF91c18x"
          }
        }
      }
    },
    {
      "type": "inAppPurchasePrices",
      "id": "${prices-id-1}",
      "attributes": {
        "startDate": "2022-07-28"
      },
      "relationships": {
        "inAppPurchaseV2": {
          "data": {
            "type": "inAppPurchases",
            "id": "6446452615"
          }
        },
        "inAppPurchasePricePoint": {
          "data": {
            "type": "inAppPurchasePricePoints",
            "id": "NjQ0NjE0ODU2MF91c18xMA"
          }
        }
      }
    }
  ]
}

```

This payload has two sections. The first section contains references to two `manualPrices`, which are the current price and the scheduled future price.

```other
"manualPrices": {
        "data": [
          {
            "type": "inAppPurchasePrices",
            "id": "${prices-id}"
          },
          {
            "type": "inAppPurchasePrices",
            "id": "${prices-id-1}"
          }

        ]
      }
    }
```

The `included` portion of the payload states the price points and change date for the current price and scheduled price.

```other
 "included": [
    {
      "type": "inAppPurchasePrices",
      "id": "${prices-id}",
      "attributes": {
        "startDate": "2022-06-29"
      },
      "relationships": {
        "inAppPurchaseV2": {
          "data": {
            "type": "inAppPurchases",
            "id": "6446452615"
          }
        },
        "inAppPurchasePricePoint": {
          "data": {
            "type": "inAppPurchasePricePoints",
            "id": "NjQ0NjE0ODU2MF91c18x"
          }
        }
      }
    },
        {
      "type": "inAppPurchasePrices",
      "id": "${prices-id-1}",
      "attributes": {
        "startDate": "2022-07-28"
      },
      "relationships": {
        "inAppPurchaseV2": {
          "data": {
            "type": "inAppPurchases",
            "id": "6446452615"
          }
        },
        "inAppPurchasePricePoint": {
          "data": {
            "type": "inAppPurchasePricePoints",
            "id": "NjQ0NjE0ODU2MF91c18xMA"
          }
        }
      }
    }
  ]
}
```

The `POST` call with this payload results in a `201` response.

For more information on creating and editing in-app purchases, see [`Overview for configuring in-app purchases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/overview-for-configuring-in-app-purchases) in [`App Store Connect for iPhone and iPad`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/).

## See Also

- [In-App Purchases](in-app-purchases.md)
  Create, modify, and delete in-app purchases for your app.
- [In-App Purchase Localizations](in-app-purchase-localizations.md)
  Create, modify, and delete localized metadata for in-app purchases.
- [In-App purchase price schedules](in-app-purchase-price-schedules.md)
  Create a scheduled price change for an in-app purchase, and get information about scheduled price changes.
- [In-app purchase availability](in-app-purchase-availability.md)
  Read and modify territory availability for an in-app purchase.
- [In-app purchase images](in-app-purchase-images.md)
  Create, modify, and delete promotion images for your in-app purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/managing-in-app-purchases)*