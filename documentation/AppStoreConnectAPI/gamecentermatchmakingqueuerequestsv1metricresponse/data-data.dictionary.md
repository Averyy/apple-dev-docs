# GameCenterMatchmakingQueueRequestsV1MetricResponse.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data structure in a response body for the match requests in a queue.

**Availability**:
- App Store Connect API 3.1+

## Declaration

```
object GameCenterMatchmakingQueueRequestsV1MetricResponse.Data
```

## Topics

### Objects
- [object GameCenterMatchmakingQueueRequestsV1MetricResponse.Data.DataPoints](./data-data.dictionary/datapoints-data.dictionary.md)
  The key properties of the data in the response.
- [object GameCenterMatchmakingQueueRequestsV1MetricResponse.Data.Dimensions](./data-data.dictionary/dimensions-data.dictionary.md)
  The details of the data in the response.

## Properties

- `dataPoints` ([GameCenterMatchmakingQueueRequestsV1MetricResponse.Data.DataPoints])
- `dimensions` (GameCenterMatchmakingQueueRequestsV1MetricResponse.Data.Dimensions)
- `granularity` (string): The granularity of the data using the ISO 8601 format for durations.

  **Allowed Values**: `P1D`, `PT1H`, `PT15M`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecentermatchmakingqueuerequestsv1metricresponse/data-data.dictionary)*