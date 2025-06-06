# delegate

**Framework**: CryptoTokenKit  
**Kind**: property

The token driver delegate.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
weak var delegate: (any TKTokenDriverDelegate)? { get set }
```

## See Also

- [protocol TKTokenDriverDelegate](tktokendriverdelegate.md)
  The interface that a token driver delegate implements to respond to token creation events.
- [TKTokenDriver.ClassID](tktokendriver/classid.md)
  The type of the class identifier for the token driver.
- [TKTokenDriver.Configuration](tktokendriver/configuration.md)
  A configuration for one class of token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokendriver/delegate)*