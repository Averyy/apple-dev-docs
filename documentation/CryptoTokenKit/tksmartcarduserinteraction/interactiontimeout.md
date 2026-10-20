# interactionTimeout

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

The timeout, in seconds, after the first key stroke. If set to `0`, the reader-defined default timeout is used. `0` by default.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var interactionTimeout: TimeInterval { get set }
```

```objc
@property NSTimeInterval interactionTimeout;
```

## See Also

### Configuring Timeout
- [var initialTimeout: TimeInterval](./initialtimeout.md)
  The timeout, in seconds, for initial interaction. If set to `0`, the reader-defined default timeout is used. `0` by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteraction/interactiontimeout)*