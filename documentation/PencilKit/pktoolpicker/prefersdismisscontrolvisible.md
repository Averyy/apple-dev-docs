# prefersDismissControlVisible

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

If this is true the tool picker may show UI that allows dismissing it. If this is false the tool picker will not show this UI. By default this resigns first responder, but is customizable by `PKToolPickerDelegate`’s `toolPickerWillDismiss...` method.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var prefersDismissControlVisible: Bool { get set }
```

```objc
@property (nonatomic) BOOL prefersDismissControlVisible;
```

## Discussion

By default this is true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpicker/prefersdismisscontrolvisible)*