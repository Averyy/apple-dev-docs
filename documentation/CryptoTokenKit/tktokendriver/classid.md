# TKTokenDriver.ClassID

**Framework**: CryptoTokenKit  
**Kind**: typealias  
**Role**: Type Alias

The type of the class identifier for the token driver.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
typealias ClassID = String
```

```c
typedef NSString * TKTokenDriverClassID;
```

## See Also

### Responding to Token Creation
- [var delegate: (any TKTokenDriverDelegate)?](./delegate.md)
  The token driver delegate.
- [protocol TKTokenDriverDelegate](../tktokendriverdelegate.md)
  The interface that a token driver delegate implements to respond to token creation events.
- [TKTokenDriver.Configuration](./configuration.md)
  A configuration for one class of token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokendriver/classid)*