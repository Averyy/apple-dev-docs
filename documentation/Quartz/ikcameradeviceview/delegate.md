# delegate

**Framework**: Quartz  
**Kind**: property  
**Role**: Instance Property

The camera device view delegate.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@IBOutlet
unowned(unsafe) var delegate: (any IKCameraDeviceViewDelegate)! { get set }
```

```objc
@property (assign) id<IKCameraDeviceViewDelegate> delegate;
```

#### Discussion

The delegate must conform to the [`IKCameraDeviceViewDelegate`](../ikcameradeviceviewdelegate.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikcameradeviceview/delegate)*