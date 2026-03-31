# failedCount

**Framework**: App Store Server API  
**Kind**: typealias

The count of subscriptions that fail to receive a subscription-renewal-date extension.

**Availability**:
- App Store Server API 1.7+

## Declaration

```swift
int64 failedCount
```

#### Discussion

For information about retrying a renewal date extension when if fails, see [`Extending the renewal date for auto-renewable subscriptions`](extending-the-renewal-date-for-auto-renewable-subscriptions.md).

## See Also

- [type complete](complete.md)
  A Boolean value that indicates whether the App Store completed the request to extend a subscription renewal date to active subscribers.
- [type completeDate](completedate.md)
  The UNIX time, in milliseconds, that the App Store completes a request to extend a subscription renewal date for eligible subscribers.
- [type succeededCount](succeededcount.md)
  The count of subscriptions that successfully receive a subscription-renewal-date extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/failedcount)*