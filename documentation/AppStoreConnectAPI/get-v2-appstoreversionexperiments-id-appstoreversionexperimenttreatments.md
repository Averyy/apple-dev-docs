# List All Treatments for an App Store Experiment

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

- `fields[appStoreVersionExperimentTreatmentLocalizations]` ([string])
- `fields[appStoreVersionExperimentTreatments]` ([string])
- `fields[appStoreVersionExperiments]` ([string])
- `include` ([string])
- `limit` (integer)
- `limit[appStoreVersionExperimentTreatmentLocalizations]` (integer)

## See Also

- [GET /v2/appStoreVersionExperiments/{id}/relationships/appStoreVersionExperimentTreatments](get-v2-appstoreversionexperiments-_id_-relationships-appstoreversionexperimenttreatments.md)
- [GET /v1/appStoreVersionExperimentTreatments/{id}](get-v1-appstoreversionexperimenttreatments-_id_.md)
- [GET /v1/appStoreVersionExperimentTreatments/{id}/appStoreVersionExperimentTreatmentLocalizations](get-v1-appstoreversionexperimenttreatments-_id_-appstoreversionexperimenttreatmentlocalizations.md)
- [GET /v1/appStoreVersionExperimentTreatments/{id}/relationships/appStoreVersionExperimentTreatmentLocalizations](get-v1-appstoreversionexperimenttreatments-_id_-relationships-appstoreversionexperimenttreatmentlocalizations.md)
- [Modify an App Store version experiement treatment](patch-v1-appstoreversionexperimenttreatments-_id_.md)
  Update the name and app icon name for a specific App Store version experiment.
- [POST /v1/appStoreVersionExperimentTreatments](post-v1-appstoreversionexperimenttreatments.md)
- [Delete a Treatment for an App Store Version Experiment](delete-v1-appstoreversionexperimenttreatments-_id_.md)
  Delete metadata that you configured for an App Store Version experiment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-appstoreversionexperiments-_id_-appstoreversionexperimenttreatments)*