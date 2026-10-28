# delegate

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
weak var delegate: (any AVLegibleMediaOptionsMenuController.Delegate)? { get set }
```

```objc
@property (nonatomic, weak) id<AVLegibleMediaOptionsMenuControllerDelegate> delegate;
```

## Discussion

The delegate for receiving caption preview and state change notifications.

## See Also

### Configuring a delegate
- [AVLegibleMediaOptionsMenuController.Delegate](./delegate-swift.protocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller/delegate-swift.property)*