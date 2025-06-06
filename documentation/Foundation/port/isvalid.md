# isValid

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the receiver is valid.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isValid: Bool { get }
```

#### Discussion

[`false`](https://developer.apple.com/documentation/swift/false) if the receiver is known to be invalid, otherwise [`true`](https://developer.apple.com/documentation/swift/true).

An `NSPort` object becomes invalid when its underlying communication resource, which is operating system dependent, is closed or damaged.

## See Also

- [func invalidate()](port/invalidate.md)
  Marks the receiver as invalid and posts an [`didBecomeInvalidNotification`](port/didbecomeinvalidnotification.md) to the default notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/port/isvalid)*