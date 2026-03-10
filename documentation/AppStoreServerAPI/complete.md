# complete

**Framework**: App Store Server API  
**Kind**: typealias

A Boolean value that indicates whether the App Store completed the request to extend a subscription renewal date to active subscribers.

**Availability**:
- App Store Server API 1.7+

## Declaration

```swift
boolean complete
```

#### Discussion

The request is complete when this value is `TRUE`. For more information about the subscription-renewal-date extension, see [`Extend Subscription Renewal Dates for All Active Subscribers`](extend-subscription-renewal-dates-for-all-active-subscribers.md).

## See Also

- [type completeDate](completedate.md)
  The UNIX time, in milliseconds, that the App Store completes a request to extend a subscription renewal date for eligible subscribers.
- [type failedCount](failedcount.md)
  The count of subscriptions that fail to receive a subscription-renewal-date extension.
- [type succeededCount](succeededcount.md)
  The count of subscriptions that successfully receive a subscription-renewal-date extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/complete)*