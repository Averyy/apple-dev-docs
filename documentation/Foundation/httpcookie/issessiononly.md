# isSessionOnly

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the cookie should be discarded at the end of the session (regardless of expiration date).

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isSessionOnly: Bool { get }
```

#### Discussion

This value is [`true`](https://developer.apple.com/documentation/Swift/true) if the cookie should be discarded at the end of the session (regardless of expiration date), otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var expiresDate: Date?](httpcookie/expiresdate.md)
  The cookie’s expiration date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookie/issessiononly)*