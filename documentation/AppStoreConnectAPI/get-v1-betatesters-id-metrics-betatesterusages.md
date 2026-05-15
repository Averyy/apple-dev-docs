# Read Beta Tester Usage Metrics

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get usage metrics for a specific beta tester.

**Availability**:
- App Store Connect API 3.1+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/betaTesters/1aa1fe09-bb5c-47dd-a067-a6066db1d32d/metrics/betaTesterUsages?period=P90D&filter%5Bapps%5D=6447306070
```

**Response**:

```json
{  "data": [
    {
      "type": "betaTesterUsages",
      "dataPoints": [
        {
          "start": "2023-07-07",
          "end": "2023-10-05",
          "values": {
            "crashCount": 11,
            "sessionCount": 9,
            "feedbackCount": 21
          }
        }
      ],
      "dimensions": {
        "apps": {
          "data": {
            "type": "apps",
            "id": "6447306070"
          },
          "links": {
            "related": "https://api.appstoreconnect.apple.com/v1/apps/6447306070"
          }
        }
      }
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/betaTesters/1aa1fe09-bb5c-47dd-a067-a6066db1d32d/metrics/betaTesterUsages?period=PT2160H&filter%5Bapps%5D=6447306070"
  },
  "meta": {
    "paging": {
      "total": 1,
      "limit": 50
    }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaTesters/{id}/metrics/betaTesterUsages`

## Parameters

- `filter[apps]` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `apps` resource ID from the [`List Apps`](get-v1-apps.md) response.
- `limit` (integer)
- `period` (string): -`P7D`: 7 days -`P30D`: 30 days -`P90D`: 90 days -`P365D`: 356 days

## See Also

- [Read Beta Tester Metrics for an App](get-v1-apps-_id_-metrics-betatesterusages.md)
  Get usage metrics for beta testers of a specific app.
- [Read Metrics for Beta Testers in a Beta Group](get-v1-betagroups-_id_-metrics-betatesterusages.md)
  Get beta tester usage metrics for a beta group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betatesters-_id_-metrics-betatesterusages)*