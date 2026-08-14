# TN3180: Reverting to App Store Server Notifications V1

**Framework**: Technotes

Migrate from version 2 to version 1 of App Store Server Notifications using the Modify an App endpoint.

#### Overview

When you enable your server to receive App Store Server Notifications, you configure your settings in App Store Connect. You select the version of App Store Server Notifications you want to receive, and provide your server URL, as described in [`Enter server URLs for App Store Server Notifications`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/enter-server-urls-for-app-store-server-notifications).

> **Note**: The [`App Store Server Notifications V1`](https://developer.apple.com/documentation/appstoreservernotifications/app-store-server-notifications-v1) endpoint and version 1 notifications are deprecated. Implement the [`App Store Server Notifications V2`](https://developer.apple.com/documentation/appstoreservernotifications/app-store-server-notifications-v2) endpoint on your server to receive version 2 notifications instead.

In the unusual case that you need to revert from version 2 to version 1 of App Store Server Notifications, use the [`Modify an app`](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-apps-_id_) endpoint.

#### Create the App Modification Request

The Modify an App endpoint updates app information including the URL and version you use for App Store Notifications. To use this endpoint, create a object that includes the `id`, `type`, and `attributes` properties detailed in [`AppUpdateRequest.Data`](https://developer.apple.com/documentation/appstoreconnectapi/appupdaterequest/data-data.dictionary).

To revert to version 1 of App Store Server Notifications, add the following attributes to the request body of the endpoint:

| Attribute | Value |
| --- | --- |
| `subscriptionStatusUrl` | Your server’s [`App Store Server Notifications V1`](https://developer.apple.com/documentation/appstoreservernotifications/app-store-server-notifications-v1) endpoint URL. |
| `subscriptionStatusUrlVersion` | `V1` to indicate you’re using version 1 of App Store Server Notifications. |

The following code shows an example of a modification request that changes only the app’s App Store Server Notifications URL and version:

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/apps/6446998023 -d
"{
    "data": {
        "type": "apps",
        "id": "6446998023",
        "attributes": {
            "subscriptionStatusUrl": "https://myserver.example.com",
            "subscriptionStatusUrlVersion": "V1"
        }
    }
}"

```

**Response**:

```None
{
    "data": {
        "type": "apps",
        "id": "6446998023",
        "attributes": {
            "name": "Your Next Cortado",
            "bundleId": "com.bdt.ync",
            "sku": "YNC",
            "primaryLocale": "en-US",
            "isOrEverWasMadeForKids": false,
            "subscriptionStatusUrl": "https://myserver.example.com",
            "subscriptionStatusUrlVersion": "V1",
            "subscriptionStatusUrlForSandbox": null,
            "subscriptionStatusUrlVersionForSandbox": null,
            "availableInNewTerritories": true,
            "contentRightsDeclaration": "DOES_NOT_USE_THIRD_PARTY_CONTENT"
        },
        "relationships": {
            "ciProduct": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/ciProduct",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/ciProduct"
                }
            },
            "betaTesters": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/betaTesters"
                }
            },
            "betaGroups": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/betaGroups",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/betaGroups"
                }
            },
            "appStoreVersions": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/appStoreVersions",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/appStoreVersions"
                }
            },
            "preReleaseVersions": {
                "links": {
                     "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/preReleaseVersions",
                     "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/preReleaseVersions"
                }
            },
            "betaAppLocalizations": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/betaAppLocalizations",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/betaAppLocalizations"
                }
            },
            "builds": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/builds",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/builds"
                }
            },
            "betaLicenseAgreement": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/betaLicenseAgreement",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/betaLicenseAgreement"
                }
            },
            "betaAppReviewDetail": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/betaAppReviewDetail",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/betaAppReviewDetail"
                }
            },
            "appInfos": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/appInfos",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/appInfos"
                }
            },
            "appClips": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/appClips",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/appClips"
                }
            },
            "appPricePoints": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/appPricePoints",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/appPricePoints"
                }
            },
            "pricePoints": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/pricePoints",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/pricePoints"
                }
            },
            "endUserLicenseAgreement": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/endUserLicenseAgreement",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/endUserLicenseAgreement"
                }
            },
            "preOrder": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/preOrder",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/preOrder"
                }
            },
            "prices": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/prices",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/prices"
                }
            },
            "appPriceSchedule": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/appPriceSchedule",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/appPriceSchedule"
                }
            },
            "availableTerritories": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/availableTerritories",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/availableTerritories"
                }
            },
            "appAvailability": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/appAvailability",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/appAvailability"
                }
            },
            "inAppPurchases": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/inAppPurchases",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/inAppPurchases"
                }
            },
            "subscriptionGroups": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/subscriptionGroups",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/subscriptionGroups"
                }
            },
            "gameCenterEnabledVersions": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/gameCenterEnabledVersions",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/gameCenterEnabledVersions"
                }
            },
            "perfPowerMetrics": {
                "links": {
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/perfPowerMetrics"
                }
            },
            "appCustomProductPages": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/appCustomProductPages",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/appCustomProductPages"
                }
            },
            "inAppPurchasesV2": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/inAppPurchasesV2",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/inAppPurchasesV2"
                }
            },
            "promotedPurchases": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/promotedPurchases",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/promotedPurchases"
                }
            },
            "appEvents": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/appEvents",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/appEvents"
                }
            },
            "reviewSubmissions": {
                "links": {
                "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/reviewSubmissions",
                "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/reviewSubmissions"
                }
            },
            "subscriptionGracePeriod": {
            "links": {
                "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/subscriptionGracePeriod",
                "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/subscriptionGracePeriod"
                }
            },
            "customerReviews": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/customerReviews",
                    "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/customerReviews"
                }
            }
        },
        "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023"
        }
    },
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023"
    }
}
```

To change your server’s URL for receiving App Store Server Notifications in the sandbox environment, add the following attributes to the request body of the endpoint:

| Attribute | Value |
| --- | --- |
| `subscriptionStatusUrlForSandbox` | Your server’s [`App Store Server Notifications V1`](https://developer.apple.com/documentation/appstoreservernotifications/app-store-server-notifications-v1) endpoint URL for the sandbox environment. |
| `subscriptionStatusUrlVersionForSandbox` | `V1` to indicate you’re using version 1 of App Store Server Notifications in the sandbox environment. |

#### Revision History

- **2024-11-12** First published.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3180-reverting-app-store-server-notifications-v1)*