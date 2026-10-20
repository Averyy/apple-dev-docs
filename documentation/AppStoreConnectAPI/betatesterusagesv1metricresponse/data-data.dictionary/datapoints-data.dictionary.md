# BetaTesterUsagesV1MetricResponse.Data.DataPoints

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The time-series data points for the beta tester usage metric, each representing a time interval with usage counts.

**Availability**:
- App Store Connect API 3.1+

## Declaration

```
object BetaTesterUsagesV1MetricResponse.Data.DataPoints
```

## Topics

### Objects
- [object BetaTesterUsagesV1MetricResponse.Data.DataPoints.Values](./datapoints-data.dictionary/values-data.dictionary.md)
  The usage count values within a single data point of the beta tester usage metric.

## Properties

- `end` (date-time)
- `start` (date-time)
- `values` (BetaTesterUsagesV1MetricResponse.Data.DataPoints.Values)

## See Also

### Objects
- [object BetaTesterUsagesV1MetricResponse.Data.Dimensions](./dimensions-data.dictionary.md)
  The dimensional breakdown for the beta tester usage metric, organized by app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betatesterusagesv1metricresponse/data-data.dictionary/datapoints-data.dictionary)*