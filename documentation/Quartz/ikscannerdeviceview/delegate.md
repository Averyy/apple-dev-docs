# delegate

**Framework**: Quartz  
**Kind**: property

The scanner device delegate

**Availability**:
- macOS 10.6+

## Declaration

```swift
@IBOutlet
@MainActor unowned(unsafe) var delegate: (any IKScannerDeviceViewDelegate)! { get set }
```

#### Discussion

The delegate is sent notifications of errors as well as the completed scan content.

The delegate must conform to the [`IKScannerDeviceViewDelegate`](ikscannerdeviceviewdelegate.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikscannerdeviceview/delegate)*