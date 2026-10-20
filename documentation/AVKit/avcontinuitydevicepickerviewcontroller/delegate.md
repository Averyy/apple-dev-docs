# delegate

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The delegate that responds to events from the continuity device picker view controller.

**Availability**:
- tvOS 17.0+

## Declaration

```swift
weak var delegate: (any AVContinuityDevicePickerViewControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<AVContinuityDevicePickerViewControllerDelegate> delegate;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontinuitydevicepickerviewcontroller/delegate)*