# Understanding webhook events

**Framework**: App Store Connect API

Learn the events that describe payloads and the notifications the system sends.

**Availability**:
- App Store Connect API 4.0+

#### Overview

Webhooks give you real-time, event-driven notifications via HTTP about payloads, so you can act on these events in an automated way. If enabled, you get notification from webhooks when one of the events you specify occurs. Use the webhook information to make subsequent calls to App Store Connect API to retrieve data.

Webhook events describe the payloads that the systems sends to your listening server based on your configurations when using [`Create a webhook configuration`](post-v1-webhooks.md). To read a list of possible webhook event types, see [`WebhookEventType`](webhookeventtype.md).

To learn more about setting up, testing, and parsing webhook configurations, see [`Configuring and parsing App Store Connect API webhook notifications`](configuring-webhook-notifications.md).

#### Learn Webhook Event Types

Here are three types of webhook event types; each includes different information, based on whether the systems notifies you about app status changes or beta-tester feedback crashes or screenshots.

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
      "newExternalBuildState": "READY_FOR_REVIEW",
      "oldExternalBuildState": "PREPARE_FOR_SUBMISSION",
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

- **Background Asset version state change**: These notifications show when your background asset upload changes state during processing.

```json
{
  "data": {
    "type": "backgroundAssetVersionStateUpdated",
    "id": "cd7e273b-0514-4bf6-9ccb-30449a7d03e4",
    "attributes": {
      "timestamp": "2025-12-08T14:30:45Z",
      "newState": "FAILED",
      "oldState": "PROCESSING"
    },
    "relationships": {
      "instance": {
        "id": "607fea97-a6ba-445d-a9bd",
        "type": "backgroundAssetVersions",
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/backgroundAssetVersions/607fea97-a6ba-445d-a9bd"
        }
      }
    }
  }
}
```

- **Background Asset version internal beta release updates**: These notifications show when your Background Asset version internal beta release is created or when the state changes with beta review.

**BACKGROUND_ASSET_VERSION_INTERNAL_BETA_RELEASE_CREATED**:

```json
{
  "data": {
    "type": "backgroundAssetVersionInternalBetaReleaseCreated",
    "id": "607fea97-a6ba-445d-a9ba",
    "attributes": {
      "timestamp": "2025-12-05T14:30:45Z"
    },
    "relationships": {
      "instance": {
        "id": "607fea97-a6ba-445d-a9bd",
        "type": "backgroundAssetVersionInternalBetaReleaseCreated",
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/backgroundAssetVersionInternalBetaReleaseCreated/607fea97-a6ba-445d-a9bd"
        }
      }
    }
  }
}        
```

**BACKGROUND_ASSET_VERSION_EXTERNAL_BETA_RELEASE_STATE_UPDATED**:

```json
{
  "data": {
    "type": "backgroundAssetVersionExternalBetaReleaseStateUpdated",
    "id": "607fea97-a6ba-445d-a9ba",
    "attributes": {
      "timestamp": "2025-12-05T14:30:45Z",
      "newState": "REJECTED",
      "oldState": "IN_REVIEW"
    },
    "relationships": {
      "instance": {
        "id": "607fea97-a6ba-445d-a9bd",
        "type": "backgroundAssetVersionExternalBetaReleases",
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/backgroundAssetVersionExternalBetaReleases/607fea97-a6ba-445d-a9bd"
        }
      }
    }
  }
}
```

- **Background Asset App Store Release**: These notifications show when a new background asset is available for App Store users.

```json
{
  "data": {
    "type": "backgroundAssetVersionAppStoreReleaseStateUpdated",
    "id": "607fea97-a6ba-445d-a9ba",
    "attributes": {
      "timestamp": "2025-12-05T14:30:45Z",
      "newState": "REJECTED",
      "oldState": "IN_REVIEW"
    },
    "relationships": {
      "instance": {
        "id": "607fea97-a6ba-445d-a9bd",
        "type": "backgroundAssetVersionAppStoreReleases",
        "links": {
          "self": "/v1/backgroundAssetVersionAppStoreReleases/607fea97-a6ba-445d-a9bd"
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
      "newState": "BuildUploadState"
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
      }
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

## See Also

- [Configuring and parsing App Store Connect API webhook notifications](configuring-webhook-notifications.md)
  Manage the configuration, testing, and processing of App Store Connect API notifications for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/webhook-events)*