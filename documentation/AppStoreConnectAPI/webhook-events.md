# Understanding webhook events

**Framework**: App Store Connect API

Learn the events that describe payloads and the notifications the system sends.

**Availability**:
- App Store Connect API 4.0+

#### Overview

Webhooks give you real-time, event-driven notifications over HTTP, so you can act on events in an automated way. When you enable a webhook, you get a notification each time one of the events you specify occurs. Use the information in the notification to make subsequent calls to the App Store Connect API to retrieve data.

Webhook events describe the payloads that the system sends to your listening server, based on the configuration you provide when using [`Create a Webhook Configuration`](post-v1-webhooks.md). To read a list of possible webhook event types, see [`WebhookEventType`](webhookeventtype.md).

To learn more about setting up, testing, and parsing webhook configurations, see [`Configuring and parsing App Store Connect API webhook notifications`](configuring-webhook-notifications.md).

#### Learn Webhook Event Types

The following event types are available. Each type carries a different set of attributes, depending on whether the system notifies you about an app status change, a build change, beta tester feedback, a background asset change, or an alternative marketplace change.

- **App status changes**: Notifications that show when your app changes status, including review states.

```json
{
  "data": {
    "type": "appStoreVersionAppVersionStateUpdated",
    "id": "7c813492-9516-4c79-903e-224effdd57ac",
    "version": 1,
    "attributes": {
      "newValue": "READY_FOR_REVIEW",
      "oldValue": "PREPARE_FOR_SUBMISSION",
      "timestamp": "2025-04-16T05:00:52.745Z"
    },
    "relationships": {
      "instance": {
        "data": {
          "type": "appStoreVersions",
          "id": "ad7e6298-2570-4ca6-b3cc-f81788e40bdc"
        }
      }
    }
  }
}
```

- **Build beta state changes**: These notifications show when the external beta build status changes.

```json
{
  "data": {
    "type": "buildBetaDetailExternalBuildStateUpdated",
    "id": "4a9eacca-e53f-4006-85db-aa18c515663a",
    "version": 1,
    "attributes": {
      "newExternalBuildState": "BETA_APPROVED",
      "oldExternalBuildState": "IN_BETA_REVIEW",
      "timestamp": "2025-04-16T05:00:52.745Z"
    },
    "relationships": {
      "instance": {
        "data": {
          "type": "buildBetaDetails",
          "id": "ad7e6298-2570-4ca6-b3cc-f81788e40bdc"
        }
      }
    }
  }
}
```

- **Beta feedback**: Notifications that show when beta testers report feedback with screenshots or crashes.

**BETA_FEEDBACK_SCREENSHOT_SUBMISSION_CREATED**:

```json
{
  "data": {
    "type": "betaFeedbackScreenshotSubmissionCreated",
    "id": "4a9eacca-e53f-4006-85db-aa18c515663a",
    "version": 1,
    "attributes": {
      "timestamp": "2025-05-08T01:29:36.16Z"
    },
    "relationships": {
      "instance": {
        "data": {
          "type": "betaFeedbackScreenshotSubmissions",
          "id": "AD8JvKbr0BK0Cj9OnM6WO6I"
        },
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/betaFeedbackScreenshotSubmissions/AD8JvKbr0BK0Cj9OnM6WO6I"
        }
      }
    }
  }
}
```

**BETA_FEEDBACK_CRASH_SUBMISSION_CREATED**:

```json
{
  "data": {
    "type": "betaFeedbackCrashSubmissionCreated",
    "id": "a4319bc8-ed16-460b-8de6-ba9734b55631",
    "version": 1,
    "attributes": {
      "timestamp": "2025-05-16T20:53:20.729Z"
    },
    "relationships": {
      "instance": {
        "data": {
          "type": "betaFeedbackCrashSubmissions",
          "id": "AK7UjG-qL5QxXf3gIOGjbpQ"
        },
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/betaFeedbackCrashSubmissions/AK7UjG-qL5QxXf3gIOGjbpQ"
        }
      }
    }
  }
}
```

- **Background asset version state changes**: These notifications show when your background asset version changes state during processing. The system sends this event after you commit an upload with [`Commit an Uploaded Asset Pack to a Background Asset Version`](patch-v1-backgroundassetuploadfiles-_id_.md), when import validation finishes. A change from `PROCESSING` to `FAILED` indicates that validation failed; you also receive an email with more context about the failure. For the full list of states, see [`BackgroundAssetVersionState`](backgroundassetversionstate.md).

```json
{
  "data": {
    "type": "backgroundAssetVersionStateUpdated",
    "id": "4734e219-9977-470c-824a-59053380b7cd",
    "attributes": {
      "timestamp": "2025-12-05T14:30:45Z",
      "newState": "FAILED",
      "oldState": "PROCESSING"
    },
    "relationships": {
      "instance": {
        "id": "7012050b-e2a4-4a2c-bb98-f2b30cfdfaaf",
        "type": "backgroundAssetVersions",
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/backgroundAssetVersions/7012050b-e2a4-4a2c-bb98-f2b30cfdfaaf"
        }
      }
    }
  }
}
```

- **Background asset internal beta releases**: These notifications show when the system creates an internal beta release for your background asset version. The system sends this event when import validation succeeds, which confirms that the asset pack processed successfully and that you can submit the version for external beta or App Store review.

```json
{
  "data": {
    "type": "backgroundAssetVersionInternalBetaReleaseCreated",
    "id": "e877854d-27a3-4b97-84aa-040d0fa543ff",
    "attributes": {
      "timestamp": "2025-12-05T14:30:45Z"
    },
    "relationships": {
      "instance": {
        "id": "eee09d96-b9c2-4038-a179-4093187fc1f5",
        "type": "backgroundAssetVersionInternalBetaReleases",
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/backgroundAssetVersionInternalBetaReleases/eee09d96-b9c2-4038-a179-4093187fc1f5"
        }
      }
    }
  }
}
```

- **Background asset external beta release state changes**: These notifications show when your background asset version moves through beta review. A change to `REJECTED` indicates that review didn’t approve the version, and a change to `READY_FOR_TESTING` indicates that the version is live for external beta testers. For the full list of states, see [`BackgroundAssetVersionExternalBetaReleaseState`](backgroundassetversionexternalbetareleasestate.md).

**Rejected in review**:

```json
{
  "data": {
    "type": "backgroundAssetVersionExternalBetaReleaseStateUpdated",
    "id": "787bde23-cb91-4ebf-a70c-2c809dae7020",
    "attributes": {
      "timestamp": "2025-12-05T14:30:45Z",
      "newState": "REJECTED",
      "oldState": "IN_REVIEW"
    },
    "relationships": {
      "instance": {
        "id": "83c5efef-4c73-454f-8c3e-8537b7491fbe",
        "type": "backgroundAssetVersionExternalBetaReleases",
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/backgroundAssetVersionExternalBetaReleases/83c5efef-4c73-454f-8c3e-8537b7491fbe"
        }
      }
    }
  }
}
```

**Ready for testing**:

```json
{
  "data": {
    "type": "backgroundAssetVersionExternalBetaReleaseStateUpdated",
    "id": "787bde23-cb91-4ebf-a70c-2c809dae7020",
    "attributes": {
      "timestamp": "2025-12-05T14:30:45Z",
      "newState": "READY_FOR_TESTING",
      "oldState": "PROCESSING_FOR_TESTING"
    },
    "relationships": {
      "instance": {
        "id": "83c5efef-4c73-454f-8c3e-8537b7491fbe",
        "type": "backgroundAssetVersionExternalBetaReleases",
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/backgroundAssetVersionExternalBetaReleases/83c5efef-4c73-454f-8c3e-8537b7491fbe"
        }
      }
    }
  }
}
```

- **Background asset App Store release state changes**: These notifications show when your background asset version moves through App Store review. A change to `REJECTED` indicates that review didn’t approve the version, and a change to `READY_FOR_DISTRIBUTION` indicates that the version is available to App Store customers. For the full list of states, see [`BackgroundAssetVersionAppStoreReleaseState`](backgroundassetversionappstorereleasestate.md).

**Rejected in review**:

```json
{
  "data": {
    "type": "backgroundAssetVersionAppStoreReleaseStateUpdated",
    "id": "d7499adf-2c03-4e20-b4b5-5e5741f511b2",
    "attributes": {
      "timestamp": "2025-12-05T14:30:45Z",
      "newState": "REJECTED",
      "oldState": "IN_REVIEW"
    },
    "relationships": {
      "instance": {
        "id": "ca76cfb1-befc-4071-8012-189e5b8d6ef1",
        "type": "backgroundAssetVersionAppStoreReleases",
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/backgroundAssetVersionAppStoreReleases/ca76cfb1-befc-4071-8012-189e5b8d6ef1"
        }
      }
    }
  }
}
```

**Ready for distribution**:

```json
{
  "data": {
    "type": "backgroundAssetVersionAppStoreReleaseStateUpdated",
    "id": "d7499adf-2c03-4e20-b4b5-5e5741f511b2",
    "attributes": {
      "timestamp": "2025-12-05T14:30:45Z",
      "newState": "READY_FOR_DISTRIBUTION",
      "oldState": "PROCESSING_FOR_DISTRIBUTION"
    },
    "relationships": {
      "instance": {
        "id": "ca76cfb1-befc-4071-8012-189e5b8d6ef1",
        "type": "backgroundAssetVersionAppStoreReleases",
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/backgroundAssetVersionAppStoreReleases/ca76cfb1-befc-4071-8012-189e5b8d6ef1"
        }
      }
    }
  }
}
```

- **Build status changes**: These notifications show when your build status changes.

```json
{
  "data": {
    "type": "buildUploadStateUpdated",
    "id": "7c813492-9516-4c79-903e-224effdd57ac",
    "version": 1,
    "attributes": {
      "newState": "COMPLETE"
    },
    "relationships": {
      "instance": {
        "data": {
          "type": "buildUploads",
          "id": "ad7e6298-2570-4ca6-b3cc-f81788e40bdc"
        }
      }
    }
  }
}
```

- **Alternative app marketplace changes**: These notifications inform a marketplace about changes to apps it distributes. The system sends a notification for these changes: - A new app version is available.
- You need to remove a specific app version.
- You need to remove all versions of an app.

**ALTERNATIVE_DISTRIBUTION_PACKAGE_VERSION_CREATED**:

```json
{
  "data": {
    "type": "alternativeDistributionPackageVersionCreated",
    "id": "419ee583-c17e-4b24-84e1-738c24eb47a4",
    "version": 1,
    "attributes": {
      "appId": "10795428705",
      "timestamp": "2025-07-10T22:35:02.541411Z"
    },
    "relationships": {
      "instance": {
        "data": {
          "type": "alternativeDistributionPackageVersions",
          "id": "8d50a4f6-7653-4ccc-b9e2-b0133eb9b0d3"
        },
        "links": {
          "self": "https://api-appstoreconnect.itunes.apple.com/v1/alternativeDistributionPackageVersions/8d50a4f6-7653-4ccc-b9e2-b0133eb9b0d3"
        }
      },
      "marketplaceApp": {
        "data": {
          "type": "apps",
          "id": "10738627177"
        },
        "links": {
          "self": "https://api-appstoreconnect.itunes.apple.com/v1/apps/10738627177"
        }
      }
    }
  }
}
```

**ALTERNATIVE_DISTRIBUTION_PACKAGE_AVAILABLE_UPDATED**:

```json
{
  "data": {
    "type": "alternativeDistributionPackageAvailableUpdated",
    "id": "da44e419-437b-4dbe-894c-2da570ffc4d1",
    "version": 1,
    "attributes": {
      "available": true,
      "territories": [
        "DNK",
        "IRL",
        "NLD",
        "SVK",
        "SVN",
        "LTU",
        "HRV",
        "PRT",
        "MLT",
        "CYP",
        "AUT",
        "SWE",
        "HUN",
        "ESP",
        "EST",
        "BEL",
        "FIN",
        "POL",
        "BGR",
        "LUX",
        "CZE",
        "FRA",
        "DEU",
        "LVA",
        "ITA",
        "GRC",
        "ROU"
      ],
      "appId": "10795428705",
      "timestamp": "2025-07-11T17:47:14.498347Z"
    },
    "relationships": {
      "instance": {
        "data": {
          "type": "alternativeDistributionPackages",
          "id": "2d2c0995-dc9b-455a-bbd8-316c0a1e893f"
        },
        "links": {
          "self": "https://api-appstoreconnect.itunes.apple.com/v1/alternativeDistributionPackages/2d2c0995-dc9b-455a-bbd8-316c0a1e893f"
        }
      },
      "marketplaceApp": {
        "data": {
          "type": "apps",
          "id": "10738627177"
        },
        "links": {
          "self": "https://api-appstoreconnect.itunes.apple.com/v1/apps/10738627177"
        }
      }
    }
  }
}
```

**ALTERNATIVE_DISTRIBUTION_TERRITORY_AVAILABILITY_UPDATED**:

```json
{
  "data": {
    "type": "alternativeDistributionTerritoryAvailabilityUpdated",
    "id": "33e75449-3196-4bf7-9e69-ca12c3e4f56f",
    "version": 1,
    "attributes": {
      "available": true,
      "territories": [
        "DNK",
        "IRL",
        "NLD",
        "SVK",
        "SVN",
        "LTU",
        "HRV",
        "PRT",
        "MLT",
        "CYP",
        "AUT",
        "SWE",
        "HUN",
        "ESP",
        "EST",
        "BEL",
        "FIN",
        "POL",
        "BGR",
        "LUX",
        "CZE",
        "FRA",
        "DEU",
        "LVA",
        "ITA",
        "GRC",
        "ROU"
      ],
      "appId": "10795421620",
      "timestamp": "2025-07-17T14:55:16.125331Z"
    },
    "relationships": {
      "marketplaceApp": {
        "data": {
          "type": "apps",
          "id": "10737747186"
        },
        "links": {
          "self": "https://api-appstoreconnect.itunes.apple.com/v1/apps/10737747186"
        }
      }
    }
  }
}
```

#### Trace Background Asset Events to Your Api Calls

Background asset events correspond to specific points in the upload and review workflow, so you can use them to drive automation instead of polling for state.

To upload a new background asset version, make the following calls:

1. Create a background asset with [`Create Asset Pack Record`](post-v1-backgroundassets.md).
2. Create a background asset version with [`Create Asset Pack Version Record`](post-v1-backgroundassetversions.md).
3. Create a background asset upload file with [`Create a Reservation for an Asset Pack Upload`](post-v1-backgroundassetuploadfiles.md).
4. Upload the asset pack to the URLs the previous response returns.
5. Commit the upload with [`Commit an Uploaded Asset Pack to a Background Asset Version`](patch-v1-backgroundassetuploadfiles-_id_.md).

Committing the upload triggers import validation, and the validation result determines which event the system sends. After validation succeeds, submitting the version for review triggers further events:

| Event type | The system sends it when |
| --- | --- |
| `BACKGROUND_ASSET_VERSION_STATE_UPDATED` | Import validation fails after you commit the upload. The state changes from `PROCESSING` to `FAILED`, and you also receive an email with more context about the failure. |
| `BACKGROUND_ASSET_VERSION_INTERNAL_BETA_RELEASE_CREATED` | Import validation succeeds. The asset pack is ready for you to submit for external beta or App Store review. |
| `BACKGROUND_ASSET_VERSION_EXTERNAL_BETA_RELEASE_STATE_UPDATED` | Beta review rejects the version, or the version becomes available to external beta testers. |
| `BACKGROUND_ASSET_VERSION_APP_STORE_RELEASE_STATE_UPDATED` | App Store review rejects the version, or the version becomes available to App Store customers. |

Submit a version for App Store review with [`Create a Review Submission`](post-v1-reviewsubmissions.md).

> **Note**: Each background asset event reports the affected resource in `relationships.instance`, with the resource `id`, `type`, and a `self` link. Unlike other webhook events, background asset events don’t wrap that identifier in a `data` object.

## See Also

- [Configuring and parsing App Store Connect API webhook notifications](configuring-webhook-notifications.md)
  Manage the configuration, testing, and processing of App Store Connect API notifications for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/webhook-events)*