# startDate

**Framework**: App Store Server API  
**Kind**: typealias  
**Role**: Type

The start date of a timespan, expressed in UNIX time, in milliseconds.

**Availability**:
- App Store Server API 1.5+

## Declaration

```
timestamp startDate
```

## Discussion

The start date must be earlier than the [`endDate`](./enddate.md).

## See Also

### Data types
- [type endDate](./enddate.md)
  The end date of a timespan, expressed in UNIX time, in milliseconds.
- [type notificationType](./notificationtype.md)
  A notification type value that App Store Server Notifications 2 uses.
- [type notificationSubtype](./notificationsubtype.md)
  A notification subtype value that App Store Server Notifications 2 uses.
- [type onlyFailures](./onlyfailures.md)
  A Boolean value that indicates whether the response includes only notifications that failed to reach your server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/startdate)*