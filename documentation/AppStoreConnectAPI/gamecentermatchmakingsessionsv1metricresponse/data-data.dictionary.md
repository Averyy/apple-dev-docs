# GameCenterMatchmakingSessionsV1MetricResponse.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data structure for the results of a successful matchmaking session.

**Availability**:
- App Store Connect API 3.1+

## Declaration

```
object GameCenterMatchmakingSessionsV1MetricResponse.Data
```

## Topics

### Objects
- [object GameCenterMatchmakingSessionsV1MetricResponse.Data.DataPoints](./data-data.dictionary/datapoints-data.dictionary.md)
  The time-series data points for the Game Center matchmaking sessions metric.

## Properties

- `dataPoints` ([GameCenterMatchmakingSessionsV1MetricResponse.Data.DataPoints])
- `granularity` (string): The granularity of the data using the ISO 8601 format for durations.

  **Allowed Values**: `P1D`, `PT1H`, `PT15M`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecentermatchmakingsessionsv1metricresponse/data-data.dictionary)*