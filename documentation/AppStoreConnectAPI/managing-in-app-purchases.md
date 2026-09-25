# Managing In-App Purchases

**Framework**: App Store Connect API

Create In-App Purchases, configure their metadata and pricing, submit them for review, and promote them with the App Store Connect API.

#### Overview

The App Store Connect API lets you create and configure In-App Purchases for your app. After you create an In-App Purchase, you can add metadata, such as a display name and description, and choose your In-App Purchase pricing. After your app is fully configured, you’re able to submit your In-App Purchase for review. After approval, you can also schedule pricing changes and edit some metadata for your In-App Purchases.

##### Review App Store Connect Api Usage

To manage In-App Purchases with the App Store Connect API, you need to understand key concepts for using the API. If you’re new to using the App Store Connect API, make sure to read the documentation in the Essentials section of [`Schedule price changes`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-in-app-purchases/schedule-price-changes) and learn how to create API keys, generate JWTs, identify rate limits, and more.

To create and manage In-App Purchases, be sure you have one of the following user roles:

- `ACCOUNT_HOLDER`
- `ADMIN`
- `APP_MANAGER`

For the full list of App Store Connect user roles, see [`UserRole`](userrole.md) and [`Program Roles`](https://developer.apple.comhttps://developer.apple.com/support/roles).

##### Create Your in App Purchase

To create an In-App Purchase, use `POST /v2/inAppPurchases` ([`Create an In-App Purchase`](post-v2-inapppurchases.md)) with a payload that contains the required information, including an internal name, a product ID, the In-App Purchase type, and a review note. Additionally, supply the Apple ID of the app that contains this In-App Purchase.

Here’s an example payload:

```json
{
  "data": {
    "type": "inAppPurchases",
    "attributes": {
      "name": "Seattle Neighborhood Coffee Map",
      "productId": "MAPNEIGHBORHOODS",
      "inAppPurchaseType": "CONSUMABLE",
      "reviewNote": "This is a neighborhood map for helping to find awesome coffee shops."
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

```json
{
    "data": {
        "type": "inAppPurchases",
        "id": "6446452615",
        "attributes": {
            "name": "Seattle Neighborhood Coffee Map",
            "productId": "MAPNEIGHBORHOODS",
            "inAppPurchaseType": "CONSUMABLE",
            "state": "MISSING_METADATA",
            "reviewNote": "This is a neighborhood map for helping to find awesome coffee shops.",
            "familySharable": false,
            "contentHosting": null
        }   
```

Make note of the `id` in the response because you use this ID to look up or edit the In-App Purchase in the future.

```json
"id": "6446452615"
```

To look up a specific In-App Purchase, use the `id` with `GET /v2/inAppPurchases/{id}` ([`Read In-App Purchase information`](get-v2-inapppurchases-_id_.md)). You can also look up all In-App Purchases for an app using `GET /v1/apps/{id}/inAppPurchasesV2` ([`List all In-App Purchases for an app`](get-v1-apps-_id_-inapppurchasesv2.md)). Note that this is a `v1` endpoint.

Editing an In-App Purchase is similar, but you use `PATCH /v2/inAppPurchases/{id}` ([`Modify an In-App Purchase`](patch-v2-inapppurchases-_id_.md)). The editable fields are `name`, `reviewNote`, and `familySharable`. To control territory availability, use the In-App Purchase availability resource — see [`In-App Purchase availability`](in-app-purchase-availability.md).

> **Note**:  The `familySharable` field is editable only for auto-renewable subscriptions and non-consumable In-App Purchases.

##### Localize Metadata for Your in App Purchase

Localized display names and descriptions live on an *In-App Purchase version* — a draft container for the metadata and review images that go through App Review together. Create a version first, then attach localizations to it. The pre-4.4.1 workflow that posts localizations directly to the In-App Purchase (`POST /v1/inAppPurchaseLocalizations`) is deprecated as of 4.4.1 but remains available for existing integrations. For guidance on moving to the version-based workflow, see [`Migrating In-App Purchase metadata to v2`](migrating-in-app-purchase-metadata-to-v2.md).

Create a draft version with `POST /v1/inAppPurchaseVersions` ([`Create an In-App Purchase version`](post-v1-inapppurchaseversions.md)), relating it to the In-App Purchase you created above:

```json
{
  "data": {
    "type": "inAppPurchaseVersions",
    "relationships": {
      "inAppPurchase": {
        "data": {
          "type": "inAppPurchases",
          "id": "6446452615"
        }
      }
    }
  }
}
```

The response returns the version’s `id` and a `state` of `PREPARE_FOR_SUBMISSION`. Note the `id` — you use it in the next step:

```json
{
  "data": {
    "type": "inAppPurchaseVersions",
    "id": "abc123-4567-89ab-cdef-000000000001",
    "attributes": {
      "version": 1,
      "state": "PREPARE_FOR_SUBMISSION"
    }
  }
}
```

Add a localization by calling `POST /v2/inAppPurchaseLocalizations` ([`Create an In-App Purchase localization`](post-v2-inapppurchaselocalizations.md)). The payload specifies the locale, the display name, and the description, and relates the localization to the *version* — not the parent In-App Purchase:

```json
{
  "data": {
    "type": "inAppPurchaseLocalizations",
    "attributes": {
      "locale": "en-US",
      "name": "Seattle Neighborhood Coffee Map",
      "description": "This is a neighborhood map for helping to find awesome coffee shops."
    },
    "relationships": {
      "version": {
        "data": {
          "type": "inAppPurchaseVersions",
          "id": "abc123-4567-89ab-cdef-000000000001"
        }
      }
    }
  }
}
```

To read all localizations attached to a version, use `GET /v1/inAppPurchaseVersions/{id}/localizations` ([`List localizations for an In-App Purchase version`](get-v1-inapppurchaseversions-_id_-localizations.md)). To list every version on the parent In-App Purchase, use `GET /v2/inAppPurchases/{id}/versions` ([`List the versions of an In-App Purchase`](get-v2-inapppurchases-_id_-versions.md)). For the full version lifecycle, see [`Working with In-App Purchase versions`](working-with-in-app-purchase-versions.md).

##### Manage Pricing for Your in App Purchase

To set a price point for your In-App Purchase, look up the `id` of the price point you want to assign to the In-App Purchase. The following example uses the price point `4.99`.

To look up the price point ID, use the [`List all price points for an In-App Purchase`](get-v2-inapppurchases-_id_-pricepoints.md) endpoint:

```other
GET /v2/inAppPurchases/{id}/pricePoints?filter[territory]=USA&include=territory&limit=200
```

Filter the endpoint to reduce the amount of data you need to review.

Here’s an example response, truncated for clarity:

```json
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

To add a price point to an In-App Purchase, use `POST /v1/inAppPurchasePriceSchedules` ([`Add a Scheduled Price Change to an In-App Purchase`](post-v1-inapppurchasepriceschedules.md)). The first ID is the ID of the In-App Purchase, and the final ID is that of the price point.

> ❗ **Important**:  Review carefully because once a price increase goes into effect, your change can’t be reverted. Be sure to review information about price increases and changes at [`App Store Connect for iPhone and iPad`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/).

Here’s an example payload:

```json
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

After you configure an In-App Purchase and populate its version with localizations, submit it for App Review. The first step is to upload a screenshot to show what the In-App Purchase looks like to people.

You accomplish this task by using the `/v1/inAppPurchaseAppStoreReviewScreenshots` endpoint. This workflow is similar to the existing image workflows for App Clip images and app screenshots.

In the case of the In-App Purchase screenshot, you submit a single image using the following steps:

1. Make an image reservation with `POST /v1/inAppPurchaseAppStoreReviewScreenshots` ([`Create an In-App Purchase review screenshot`](post-v1-inapppurchaseappstorereviewscreenshots.md)).
2. Upload the image using the `PUT` URL provided in the response to the previous `POST`.
3. After your image uploads, use `PATCH /v1/inAppPurchaseAppStoreReviewScreenshots/{id}` ([`Commit a review screenshot for an In-App Purchase`](patch-v1-inapppurchaseappstorereviewscreenshots-_id_.md)) to commit the image.
4. Finally, use `GET /v1/inAppPurchaseAppStoreReviewScreenshots/{id}` ([`Read In-App Purchase review screenshot information`](get-v1-inapppurchaseappstorereviewscreenshots-_id_.md)) to confirm that the image is in place.

For more information, see [`Uploading Assets to App Store Connect`](uploading-assets-to-app-store-connect.md).

> ❗ **Important**:  Submit your first In-App Purchase together with an app binary submission through [`appstoreconnect.apple.com`](https://developer.apple.comhttps://appstoreconnect.apple.com). The review-submission API calls below don’t apply to that first submission. For subsequent In-App Purchases, submit using the API endpoints below without an associated app binary submission.

Submit a subsequent In-App Purchase version using the review submissions workflow. This is the current, non-deprecated path.

First, create a review submission for the app with `POST /v1/reviewSubmissions` ([`Create a Review Submission`](post-v1-reviewsubmissions.md)):

```json
{
  "data": {
    "type": "reviewSubmissions",
    "attributes": {
      "platform": "IOS"
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

Next, add the In-App Purchase version as an item on that review submission with `POST /v1/reviewSubmissionItems` ([`Create a Review Submission Item`](post-v1-reviewsubmissionitems.md)):

```json
{
  "data": {
    "type": "reviewSubmissionItems",
    "relationships": {
      "reviewSubmission": {
        "data": {
          "type": "reviewSubmissions",
          "id": "${reviewSubmissionId}"
        }
      },
      "inAppPurchaseVersion": {
        "data": {
          "type": "inAppPurchaseVersions",
          "id": "abc123-4567-89ab-cdef-000000000001"
        }
      }
    }
  }
}
```

Finally, submit the review submission by patching its `submitted` attribute to `true` with `PATCH /v1/reviewSubmissions/{id}` ([`Modify a Review Submission`](patch-v1-reviewsubmissions-_id_.md)):

```json
{
  "data": {
    "type": "reviewSubmissions",
    "id": "${reviewSubmissionId}",
    "attributes": {
      "submitted": true
    }
  }
}
```

The version’s state transitions from `PREPARE_FOR_SUBMISSION` to `READY_FOR_REVIEW` when you add it to a review submission, then to `WAITING_FOR_REVIEW` after you mark the submission `submitted`, then `IN_REVIEW`, and finally to `APPROVED` or `REJECTED`. Poll `GET /v1/inAppPurchaseVersions/{id}` ([`Read In-App Purchase version information`](get-v1-inapppurchaseversions-_id_.md)) to check the current state.

The `POST /v1/inAppPurchaseSubmissions` ([`Create a review submission for an In-App Purchase`](post-v1-inapppurchasesubmissions.md)) endpoint is deprecated as of 4.4.1. Existing integrations that submit an In-App Purchase directly by its `id` continue to work, but new integrations use the review submissions workflow described above. For guidance on moving to the version-based workflow, see [`Migrating In-App Purchase metadata to v2`](migrating-in-app-purchase-metadata-to-v2.md).

##### Promote Your in App Purchase

After your In-App Purchase gets approved, you can promote it to people who visit your app listing in the App Store. To accomplish this task, use `POST /v1/promotedPurchases` ([`Promote a purchase`](post-v1-promotedpurchases.md)) with a payload that includes your Apple ID and the ID for your In-App Purchase. The response confirms the state is `"Waiting for Review"`. You can also look up the state of a specific promoted purchase by using `GET /v2/inAppPurchases/{id}/promotedPurchase` ([`Read promoted purchase information for an In-App Purchase`](get-v2-inapppurchases-_id_-promotedpurchase.md)), or look up the status of all your promoted purchases by using `GET /v1/apps/{id}/promotedPurchases` ([`List all promoted purchases for an app`](get-v1-apps-_id_-promotedpurchases.md)).

Here’s an example payload:

```json
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

At some point, you might want to change the price of your In-App Purchase. Use one of these two methods:

- Make an immediate change of price.
- Schedule a price change for a future time.

To perform either type of price change, you use a process similar to setting the initial price. First, look up your current price point using `GET /v1/inAppPurchasePriceSchedules/{id}/manualPrices` ([`Read Price Information for an In-App Purchase Price Schedule`](get-v1-inapppurchasepriceschedules-_id_-manualprices.md)) — where `id` is the In-App Purchase ID — to determine the desired price point. The following screenshot shows what the current pricing looks like in App Store Connect for the In-App Purchase.

![Screenshot of a price schedule from appstoreconnect.apple.com.](/images/com.apple.appstoreconnectapi/media-4054484@2x.png)

The following example request includes several additional fields and filters:

```other
GET /v1/inAppPurchasePriceSchedules/6446148560/manualPrices?fields%5BinAppPurchasePricePoints%5D=priceTier&filter%5Bterritory%5D=USA&include=inAppPurchasePricePoint
```

Here’s an example response that includes the information from the request above:

```json
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

This first portion of the response is shown below. This portion shows an `inAppPurchasePrices` with `id`, but the `startDate` attribute is `null`, which means this is the current price. You can look up the customer price for a particular territory by looking up the `inAppPurchasePricePoints` by `id` using `GET /v2/inAppPurchases/{id}/pricePoints` ([`List all price points for an In-App Purchase`](get-v2-inapppurchases-_id_-pricepoints.md)) and searching the response for the ID.

```json
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

The second portion of the response is shown below. This portion shows another `inAppPurchasePrices` with `id`, but the `startDate` attribute is an ISO 8601 formatted date that shows the date the price of the In-App Purchase changes. This portion of the response also has a different `inAppPurchasePricePoints` `id`, showing a change of price.

```json
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

Now that you know about the current price and the scheduled price change, you might want to schedule another price change, like reverting back to the original price. To accomplish this task, use `POST /v1/inAppPurchasePriceSchedules` ([`Add a Scheduled Price Change to an In-App Purchase`](post-v1-inapppurchasepriceschedules.md)) with a payload like this:

```json
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

```json
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

```json
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

For more information on creating and editing In-App Purchases, see [`Overview for configuring In-App Purchases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/overview-for-configuring-in-app-purchases) in [`App Store Connect for iPhone and iPad`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/).

## See Also

- [Working with In-App Purchase versions](working-with-in-app-purchase-versions.md)
  Manage draft versions of an In-App Purchase’s localized metadata and review images before submitting for App Review.
- [Migrating In-App Purchase metadata to v2](migrating-in-app-purchase-metadata-to-v2.md)
  Update an existing integration from the pre-4.4.1 metadata workflow to the version-based v2 workflow.
- [In-App Purchase Versions](in-app-purchase-versions.md)
  Create and read draft versions of an In-App Purchase, with their localized metadata and review images.
- [In-App Purchases](in-app-purchases.md)
  Create, modify, and delete In-App Purchases for your app.
- [In-App Purchase Localizations](in-app-purchase-localizations.md)
  Create, modify, and delete localized metadata for In-App Purchase versions.
- [In-App Purchase localizations (v1)](in-app-purchase-localizations-v1.md)
  Create, modify, and delete localized metadata for In-App Purchases.
- [In-App Purchase price schedules](in-app-purchase-price-schedules.md)
  Create a scheduled price change for an In-App Purchase, and get information about scheduled price changes.
- [In-App Purchase availability](in-app-purchase-availability.md)
  Read and modify territory availability for an In-App Purchase.
- [In-App Purchase images](in-app-purchase-images.md)
  Create, modify, and delete promotion images for In-App Purchases.
- [In-App Purchase images (v1)](in-app-purchase-images-v1.md)
  Create, modify, and delete promotion images for your In-App Purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/managing-in-app-purchases)*