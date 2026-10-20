# delegate

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

The delegate for observing events that occur during the user interaction.

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
weak var delegate: (any TKSmartCardUserInteractionDelegate)? { get set }
```

```objc
@property (weak, nullable) id<TKSmartCardUserInteractionDelegate> delegate;
```

## See Also

### Handling User Interaction Events
- [protocol TKSmartCardUserInteractionDelegate](../tksmartcarduserinteractiondelegate.md)
  The interface implemented by a Smart Card user interaction delegate to handle user interaction events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteraction/delegate)*