# completeDate

**Framework**: App Store Server API  
**Kind**: typealias

The UNIX time, in milliseconds, that the App Store completes a request to extend a subscription renewal date for eligible subscribers.

**Availability**:
- App Store Server API 1.7+

## Declaration

```swift
timestamp completeDate
```

#### Discussion

For more information about a requesting a subscription-renewal-date extension, see [`Extend Subscription Renewal Dates for All Active Subscribers`](extend-subscription-renewal-dates-for-all-active-subscribers.md).

## See Also

- [type complete](complete.md)
  A Boolean value that indicates whether the App Store completed the request to extend a subscription renewal date to active subscribers.
- [type failedCount](failedcount.md)
  The count of subscriptions that fail to receive a subscription-renewal-date extension.
- [type succeededCount](succeededcount.md)
  The count of subscriptions that successfully receive a subscription-renewal-date extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/completedate)*