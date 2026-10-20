# delegate

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

The token delegate.

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
weak var delegate: (any TKTokenDelegate)? { get set }
```

```objc
@property (weak, nullable) id<TKTokenDelegate> delegate;
```

## See Also

### Responding to Session Creation
- [protocol TKTokenDelegate](../tktokendelegate.md)
  The interface that a token delegate implements to respond to session creation events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktoken/delegate)*