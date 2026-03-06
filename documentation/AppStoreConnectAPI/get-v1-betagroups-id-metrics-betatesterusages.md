# Read metrics for beta testers in a beta group

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get beta tester usage metrics for a beta group.

**Availability**:
- App Store Connect API 3.1+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/betaGroups/db51edb0-a8a4-4be9-8481-09dff260ea6e/metrics/betaTesterUsages?groupBy=betaTesters&filter%5BbetaTesters%5D=1aa1fe09-bb5c-47dd-a067-a6066db1d32
```

**Response**:

```json
{
  “data”: [
    {
      “type”: “appsBetaTesterUsages”,
      “dataPoints”: [
        {
          “start”: “2022-10-05”,
          “end”: “2023-10-05”,
          “values”: {
            “crashCount”: 13,
            “sessionCount”: 48,
            “feedbackCount”: 21
          }
        }
      ],
      “dimensions”: {
        “betaTesters”: {
          “data”: {
            “type”: “betaTesters”,
            “id”: “1aa1fe09-bb5c-47dd-a067-a6066db1d32d”
          },
          “links”: {
            “related”: “https://api.appstoreconnect.apple.com/v1/betaTesters/1aa1fe09-bb5c-47dd-a067-a6066db1d32d”,
            “groupBy”: “https://api.appstoreconnect.apple.com/v1/betaGroups/db51edb0-a8a4-4be9-8481-09dff260ea6e/metrics/betaTesterUsages?groupBy=betaTesters”
          }
        }
      }
    }
  ],
  “links”: {
    “self”: “https://api.appstoreconnect.apple.com/v1/betaTesters/842d4014-3ecc-4f80-8531-19aa800e3a53/metrics/betaTesterUsages?period=PT8760H&filter%5Bapps%5D=6448250830”
  },
  “meta”: {
    “paging”: {
      “total”: 1,
      “limit”: 50
    }
  }
}

```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaGroups/{id}/metrics/betaTesterUsages`

## Parameters

- `filter[betaTesters]` (string): An opaque resource ID that uniquely identifies the resource. Obtain the `betaTesters` resource ID from the [`List Beta Testers`](get-v1-betatesters.md) response.
- `groupBy` ([string])
- `limit` (integer)
- `period` (string)

## See Also

- [List Beta Groups](get-v1-betagroups.md)
  Find and list beta groups for all apps.
- [Read Beta Group Information](get-v1-betagroups-_id_.md)
  Get a specific beta group.
- [Read the App Information of a Beta Group](get-v1-betagroups-_id_-app.md)
  Get the app information for a specific beta group.
- [GET /v1/betaGroups/{id}/relationships/app](get-v1-betagroups-_id_-relationships-app.md)
- [Read recruitment criteria for a beta group](get-v1-betagroups-_id_-betarecruitmentcriteria.md)
  Get the recruitment criteria information for a specific beta group.
- [GET /v1/betaGroups/{id}/relationships/betaRecruitmentCriteria](get-v1-betagroups-_id_-relationships-betarecruitmentcriteria.md)
- [Read build compatibilty for a beta group](get-v1-betagroups-_id_-betarecruitmentcriterioncompatiblebuildcheck.md)
  Get the build compatibilty information for a specific beta group.
- [GET /v1/betaGroups/{id}/relationships/betaRecruitmentCriterionCompatibleBuildCheck](get-v1-betagroups-_id_-relationships-betarecruitmentcriterioncompatiblebuildcheck.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betagroups-_id_-metrics-betatesterusages)*