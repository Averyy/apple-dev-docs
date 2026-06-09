# Read app store experiment information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information for a specific App Store version experiment.

**Availability**:
- App Store Connect API 2.4+

## Mentions

- [App Store Connect API 2.4 release notes](app-store-connect-api-2-4-release-notes.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v2/appStoreVersionExperiments/1a22d9a7-f574-4669-b1ca-1ba88f786c19
```

**Response**:

```json
{
  “data” : {
    “type” : “appStoreVersionExperiments”,
    “id” : “1a22d9a7-f574-4669-b1ca-1ba88f786c19”,
    “attributes” : {
      “name” : “PPO Test 1”,
      “platform” : “IOS”,
      “trafficProportion” : 50,
      “state” : “PREPARE_FOR_SUBMISSION”,
      “reviewRequired” : true,
      “startDate” : null,
      “endDate” : null
    },
    “relationships” : {
      “appStoreVersionExperimentTreatments” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v2/appStoreVersionExperiments/1a22d9a7-f574-4669-b1ca-1ba88f786c19/relationships/appStoreVersionExperimentTreatments”,
          “related” : “https://api.appstoreconnect.apple.com/v2/appStoreVersionExperiments/1a22d9a7-f574-4669-b1ca-1ba88f786c19/appStoreVersionExperimentTreatments”
        }
      }
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v2/appStoreVersionExperiments/1a22d9a7-f574-4669-b1ca-1ba88f786c19”
    }
  },
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v2/appStoreVersionExperiments/1a22d9a7-f574-4669-b1ca-1ba88f786c19”
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/appStoreVersionExperiments/{id}`

## Parameters

- `fields[appStoreVersionExperimentTreatments]` ([string]): Additional fields to include for each App Store version experiment treatment resource returned by the response.
- `fields[appStoreVersionExperiments]` ([string]): Additional fields to include for each App Store version experiment resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[appStoreVersionExperimentTreatments]` (integer): The maximum number of related App Store version experiment treatment resources to return.
- `limit[controlVersions]` (integer): The maximum number of related control version resources to return.
- `fields[appStoreVersions]` ([string])
- `fields[apps]` ([string])

## See Also

- [List all experiments for an app store version v1](get-v1-appstoreversions-_id_-appstoreversionexperiments.md)
  Get a list of all experiments for an App Store version of an app across all platforms.
- [List all experiments ids for an app store version v1](get-v1-appstoreversions-_id_-relationships-appstoreversionexperiments.md)
  Get a list of all experiments IDs for an App Store version of an app across all platforms.
- [List all experiments for an app store version](get-v1-appstoreversions-_id_-appstoreversionexperimentsv2.md)
  Get a list of all experiments for an App Store version of an app across all platforms.
- [List all experiment ids for an app store version](get-v1-appstoreversions-_id_-relationships-appstoreversionexperimentsv2.md)
  Get a list of all experiments IDs for an App Store version across all platforms.
- [List all treatments for an app store experiment](get-v2-appstoreversionexperiments-_id_-appstoreversionexperimenttreatments.md)
  Get a list of all treatments for a specific App Store version experiment.
- [List treatment IDs for an app store version experiment](get-v2-appstoreversionexperiments-_id_-relationships-appstoreversionexperimenttreatments.md)
  Get a list of experiment treatment IDs for a specific App Store version experiment.
- [Create an app store experiment](post-v2-appstoreversionexperiments.md)
  Add a new experiment to an App Store version.
- [Modify an app store experiment](patch-v2-appstoreversionexperiments-_id_.md)
  Update the name, the started state, and the proportion of traffic to send to an App Store experiment.
- [Delete an app store experiment](delete-v2-appstoreversionexperiments-_id_.md)
  Delete a specific App Store version experiment before it starts.
- [Read app store experiment information v1](get-v1-appstoreversionexperiments-_id_.md)
  Get information for a specific App Store version experiment.
- [List all treatments for an app store experiment v1](get-v1-appstoreversionexperiments-_id_-appstoreversionexperimenttreatments.md)
  Get a list of all treatments for a specific App Store version experiment.
- [List treatment IDs for an App Store version experiment](get-v1-appstoreversionexperiments-_id_-relationships-appstoreversionexperimenttreatments.md)
- [Modify an app store experiment v1](patch-v1-appstoreversionexperiments-_id_.md)
  Update the name, the started state, and the proportion of traffic to send to an App Store experiment.
- [Create an app store experiment v1](post-v1-appstoreversionexperiments.md)
  Add a new experiment to an App Store version.
- [Delete an app store version experiment v1](delete-v1-appstoreversionexperiments-_id_.md)
  Delete a specific App Store version experiment before it starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-appstoreversionexperiments-_id_)*