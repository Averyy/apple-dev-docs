# AnalyticsReportRequest.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe an analytics report request resource.

**Availability**:
- App Store Connect API 3.4+

## Declaration

```
object AnalyticsReportRequest.Attributes
```

## Properties

- `accessType` (string):

  - **`ONE_TIME_SNAPSHOT`**: A type that provides up-to-the-moment data and goes back as far as is available. It doesn’t generate any new data after the day you request it.
  - **`ONGOING`**: A type that provides current data and is the most typical. It generates daily reports.

  **Allowed Values**: `ONE_TIME_SNAPSHOT`, `ONGOING`
- `stoppedDueToInactivity` (boolean):

  > **Note**: Note If you don’t retrieve data for a long time, a report request changes to `stoppedDueToInactivity`. You need to make a new request to resume getting reports.

## See Also

### Objects
- [object AnalyticsReportRequest.Relationships](./relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/analyticsreportrequest/attributes-data.dictionary)*