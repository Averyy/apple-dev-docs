# delegate

**Framework**: Quartz  
**Kind**: property  
**Role**: Instance Property

The scanner device delegate

**Availability**:
- macOS 10.6+

## Declaration

```swift
@IBOutlet
unowned(unsafe) var delegate: (any IKScannerDeviceViewDelegate)! { get set }
```

```objc
@property (assign) id<IKScannerDeviceViewDelegate> delegate;
```

#### Discussion

The delegate is sent notifications of errors as well as the completed scan content.

The delegate must conform to the [`IKScannerDeviceViewDelegate`](../ikscannerdeviceviewdelegate.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikscannerdeviceview/delegate)*