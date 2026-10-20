# delegate

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The input picker view’s delegate.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
weak var delegate: (any AVInputPickerInteraction.Delegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<AVInputPickerInteractionDelegate> delegate;
```

## See Also

### Setting the delegate
- [AVInputPickerInteraction.Delegate](./delegate-swift.protocol.md)
  The `AVInputPickerInteractionDelegate` protocol defines methods you use to receive notifications about transitions in an `AVInputPickerInteraction` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinputpickerinteraction/delegate-swift.property)*