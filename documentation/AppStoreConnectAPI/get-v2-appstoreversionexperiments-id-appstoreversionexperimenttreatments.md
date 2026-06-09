# List all treatments for an app store experiment

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of all treatments for a specific App Store version experiment.

**Availability**:
- App Store Connect API 2.4+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v2/appStoreVersionExperiments/1a22d9a7-f574-4669-b1ca-1ba88f786c19/appStoreVersionExperimentTreatments
```

**Response**:

```json
{
  “data” : [ {
    “type” : “appStoreVersionExperimentTreatments”,
    “id” : “0af1be11-a7d9-4e94-aef5-f8ea12bc3be7”,
    “attributes” : {
      “name” : “Treatment Bravo”,
      “appIcon” : null,
      “appIconName” : null,
      “promotedDate” : null
    },
    “relationships” : {
      “appStoreVersionExperimentTreatmentLocalizations” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/appStoreVersionExperimentTreatments/0af1be11-a7d9-4e94-aef5-f8ea12bc3be7/relationships/appStoreVersionExperimentTreatmentLocalizations”,
          “related” : “https://api.appstoreconnect.apple.com/v1/appStoreVersionExperimentTreatments/0af1be11-a7d9-4e94-aef5-f8ea12bc3be7/appStoreVersionExperimentTreatmentLocalizations”
        }
      }
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/appStoreVersionExperimentTreatments/0af1be11-a7d9-4e94-aef5-f8ea12bc3be7”
    }
  }, {
    “type” : “appStoreVersionExperimentTreatments”,
    “id” : “a84d0df3-4c16-4073-adbd-90b94c742c68”,
    “attributes” : {
      “name” : “Treatment Alpha”,
      “appIcon” : null,
      “appIconName” : null,
      “promotedDate” : null
    },
    “relationships” : {
      “appStoreVersionExperimentTreatmentLocalizations” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/appStoreVersionExperimentTreatments/a84d0df3-4c16-4073-adbd-90b94c742c68/relationships/appStoreVersionExperimentTreatmentLocalizations”,
          “related” : “https://api.appstoreconnect.apple.com/v1/appStoreVersionExperimentTreatments/a84d0df3-4c16-4073-adbd-90b94c742c68/appStoreVersionExperimentTreatmentLocalizations”
        }
      }
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/appStoreVersionExperimentTreatments/a84d0df3-4c16-4073-adbd-90b94c742c68”
    }
  } ],
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v2/appStoreVersionExperiments/1a22d9a7-f574-4669-b1ca-1ba88f786c19/appStoreVersionExperimentTreatments”
  },
  “meta” : {
    “paging” : {
      “total” : 2,
      “limit” : 50
    }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/appStoreVersionExperiments/{id}/appStoreVersionExperimentTreatments`

## Parameters

- `fields[appStoreVersionExperimentTreatmentLocalizations]` ([string]): Additional fields to include for each App Store version experiment treatment localization resource returned by the response.
- `fields[appStoreVersionExperimentTreatments]` ([string]): Additional fields to include for each App Store version experiment treatment resource returned by the response.
- `fields[appStoreVersionExperiments]` ([string]): Additional fields to include for each App Store version experiment resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The maximum number of App Store version experiment treatment resources to return.
- `limit[appStoreVersionExperimentTreatmentLocalizations]` (integer): The maximum number of related App Store version experiment treatment localization resources to return.

## See Also

- [List treatment IDs for an app store version experiment](get-v2-appstoreversionexperiments-_id_-relationships-appstoreversionexperimenttreatments.md)
  Get a list of experiment treatment IDs for a specific App Store version experiment.
- [Read app store version experiment treatment information](get-v1-appstoreversionexperimenttreatments-_id_.md)
  Get information about a specific App Store version experiment treatment.
- [List all localizations for an app store version experiment treatment](get-v1-appstoreversionexperimenttreatments-_id_-appstoreversionexperimenttreatmentlocalizations.md)
  Get a list of all localizations for a specific App Store version experiment treatment.
- [List localization IDs for an App Store version experiment treatment](get-v1-appstoreversionexperimenttreatments-_id_-relationships-appstoreversionexperimenttreatmentlocalizations.md)
- [Modify an app store version experiment treatment](patch-v1-appstoreversionexperimenttreatments-_id_.md)
  Update the name and app icon name for a specific App Store version experiment.
- [Create an app store version experiment treatment](post-v1-appstoreversionexperimenttreatments.md)
  Add a new treatment to an App Store version experiment.
- [Delete a treatment for an app store version experiment](delete-v1-appstoreversionexperimenttreatments-_id_.md)
  Delete metadata that you configured for an App Store Version experiment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-appstoreversionexperiments-_id_-appstoreversionexperimenttreatments)*