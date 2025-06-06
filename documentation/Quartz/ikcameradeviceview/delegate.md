# delegate

**Framework**: Quartz  
**Kind**: property

The camera device view delegate.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@IBOutlet
@MainActor unowned(unsafe) var delegate: (any IKCameraDeviceViewDelegate)! { get set }
```

#### Discussion

The delegate must conform to the [`IKCameraDeviceViewDelegate`](ikcameradeviceviewdelegate.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikcameradeviceview/delegate)*