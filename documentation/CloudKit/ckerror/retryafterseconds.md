# retryAfterSeconds

**Framework**: CloudKit  
**Kind**: property

The number of seconds to wait before you retry the request.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS ?+
- watchOS 3.0+

## Declaration

```swift
var retryAfterSeconds: Double? { get }
```

#### Discussion

This property’s value is available only when the error’s `code` is [`serviceUnavailable`](ckerror/serviceunavailable.md) or [`requestRateLimited`](ckerror/requestratelimited.md).

The error’s `userInfo` dictionary contains the same value as this property. You can access it using the [`CKErrorRetryAfterKey`](ckerrorretryafterkey.md) key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckerror/retryafterseconds)*