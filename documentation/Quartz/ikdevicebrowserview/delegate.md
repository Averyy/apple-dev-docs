# delegate

**Framework**: Quartz  
**Kind**: property

Specifies the delegate object.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@IBOutlet
@MainActor unowned(unsafe) var delegate: (any IKDeviceBrowserViewDelegate)! { get set }
```

#### Discussion

The delegate object must conform to the [`IKDeviceBrowserViewDelegate`](ikdevicebrowserviewdelegate.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikdevicebrowserview/delegate)*