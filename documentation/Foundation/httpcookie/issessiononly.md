# isSessionOnly

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, getter=isSessionOnly) BOOL sessionOnly;
```

#### Discussion

This value is [`true`](../../Swift/true.md) if the cookie should be discarded at the end of the session (regardless of expiration date), otherwise [`false`](../../Swift/false.md).

## See Also

### Determining cookie lifespan
- [var expiresDate: Date?](./expiresdate.md)
  The cookie’s expiration date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookie/issessiononly)*