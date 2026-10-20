# delegate

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The player view’s delegate object.

**Availability**:
- macOS 12.0+

## Declaration

```swift
weak var delegate: (any AVPlayerViewDelegate)? { get set }
```

```objc
@property (nonatomic, weak, readwrite, nullable) id<AVPlayerViewDelegate> delegate;
```

## See Also

### Setting the delegate object
- [protocol AVPlayerViewDelegate](../avplayerviewdelegate.md)
  A protocol that defines the methods to implement to participate in the player view’s full-screen presentation life cycle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/delegate)*