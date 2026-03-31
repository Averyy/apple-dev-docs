# onlyFailures

**Framework**: App Store Server API  
**Kind**: typealias

A Boolean value that indicates whether the response includes only notifications that failed to reach your server.

**Availability**:
- App Store Server API 1.8+

## Declaration

```swift
boolean onlyFailures
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

A value of `true` indicates that you want to receive just the App Store server notifications that failed to reach your server, including those that the App Store server is currently retrying.

## See Also

- [type startDate](startdate.md)
  The start date of a timespan, expressed in UNIX time, in milliseconds.
- [type endDate](enddate.md)
  The end date of a timespan, expressed in UNIX time, in milliseconds.
- [type notificationType](notificationtype.md)
  A notification type value that App Store Server Notifications 2 uses.
- [type notificationSubtype](notificationsubtype.md)
  A notification subtype value that App Store Server Notifications 2 uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/onlyfailures)*