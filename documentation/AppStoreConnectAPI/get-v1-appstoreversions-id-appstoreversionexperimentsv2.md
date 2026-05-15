# List All Experiments for an App Store Version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of all experiments for an App Store version of an app across all platforms.

**Availability**:
- App Store Connect API 2.4+

## Mentions

- [App Store Connect API 2.4 release notes](app-store-connect-api-2-4-release-notes.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/appStoreVersions/fb3bb89c-47c3-4cbf-8af7-677fb801c09f/appStoreVersionExperimentsV2
```

**Response**:

```json
{
  "data" : [ {
    "type" : "appStoreVersionExperiments",
    "id" : "1a22d9a7-f574-4669-b1ca-1ba88f786c19",
    "attributes" : {
      "name" : "PPO Test 1",
      "platform" : "IOS",
      "trafficProportion" : 50,
      "state" : "READY_FOR_REVIEW",
      "reviewRequired" : true,
      "startDate" : null,
      "endDate" : null
    },
    "relationships" : {
      "appStoreVersionExperimentTreatments" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v2/appStoreVersionExperiments/1a22d9a7-f574-4669-b1ca-1ba88f786c19/relationships/appStoreVersionExperimentTreatments",
          "related" : "https://api.appstoreconnect.apple.com/v2/appStoreVersionExperiments/1a22d9a7-f574-4669-b1ca-1ba88f786c19/appStoreVersionExperimentTreatments"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appStoreVersionExperiments/1a22d9a7-f574-4669-b1ca-1ba88f786c19"
    }
  } ],
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/appStoreVersions/fb3bb89c-47c3-4cbf-8af7-677fb801c09f/appStoreVersionExperimentsV2"
  },
  "meta" : {
    "paging" : {
      "total" : 1,
      "limit" : 50
    }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersions/{id}/appStoreVersionExperimentsV2`

## Parameters

- `fields[appStoreVersionExperimentTreatments]` ([string])
- `fields[appStoreVersionExperiments]` ([string])
- `fields[appStoreVersions]` ([string])
- `fields[apps]` ([string])
- `filter[state]` ([string])
- `include` ([string])
- `limit` (integer)
- `limit[appStoreVersionExperimentTreatments]` (integer)
- `limit[controlVersions]` (integer)

## See Also

- [List All Experiments for an App Store Version V1](get-v1-appstoreversions-_id_-appstoreversionexperiments.md)
  Get a list of all experiments for an App Store version of an app across all platforms.
- [List All Experiments IDs for an App Store Version V1](get-v1-appstoreversions-_id_-relationships-appstoreversionexperiments.md)
  Get a list of all experiments IDs for an App Store version of an app across all platforms.
- [List All Experiment IDs for an App Store Version](get-v1-appstoreversions-_id_-relationships-appstoreversionexperimentsv2.md)
  Get a list of all experiments IDs for an App Store version across all platforms.
- [Read App Store Experiment Information](get-v2-appstoreversionexperiments-_id_.md)
  Get information for a specific App Store version experiment.
- [List All Treatments for an App Store Experiment](get-v2-appstoreversionexperiments-_id_-appstoreversionexperimenttreatments.md)
  Get a list of all treatments for a specific App Store version experiment.
- [GET /v2/appStoreVersionExperiments/{id}/relationships/appStoreVersionExperimentTreatments](get-v2-appstoreversionexperiments-_id_-relationships-appstoreversionexperimenttreatments.md)
- [Create an App Store Experiment](post-v2-appstoreversionexperiments.md)
  Add a new experiment to an App Store version.
- [Modify an App Store Experiment](patch-v2-appstoreversionexperiments-_id_.md)
  Update the name, the started state, and the proportion of traffic to send to an App Store experiment.
- [Delete an App Store Experiment](delete-v2-appstoreversionexperiments-_id_.md)
  Delete a specific App Store version experiment before it starts.
- [Read App Store Experiment Information V1](get-v1-appstoreversionexperiments-_id_.md)
  Get information for a specific App Store version experiment.
- [List All Treatments for an App Store Experiment V1](get-v1-appstoreversionexperiments-_id_-appstoreversionexperimenttreatments.md)
  Get a list of all treatments for a specific App Store version experiment.
- [GET /v1/appStoreVersionExperiments/{id}/relationships/appStoreVersionExperimentTreatments](get-v1-appstoreversionexperiments-_id_-relationships-appstoreversionexperimenttreatments.md)
- [Modify an App Store Experiment V1](patch-v1-appstoreversionexperiments-_id_.md)
  Update the name, the started state, and the proportion of traffic to send to an App Store experiment.
- [Create an App Store Experiment V1](post-v1-appstoreversionexperiments.md)
  Add a new experiment to an App Store version.
- [Delete an App Store Version Experiment V1](delete-v1-appstoreversionexperiments-_id_.md)
  Delete a specific App Store version experiment before it starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversions-_id_-appstoreversionexperimentsv2)*