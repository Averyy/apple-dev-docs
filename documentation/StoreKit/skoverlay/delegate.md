# delegate

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The overlay’s delegate.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any SKOverlayDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<SKOverlayDelegate> delegate;
```

## See Also

### Setting a delegate
- [protocol SKOverlayDelegate](../skoverlaydelegate.md)
  Methods for responding to the overlay’s appearance, dismissal, or failure to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlay/delegate)*