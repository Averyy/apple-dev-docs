# overrideUserInterfaceStyle

**Framework**: PencilKit  
**Kind**: property

The specific user interface style to apply to the tool picker.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var overrideUserInterfaceStyle: UIUserInterfaceStyle { get set }
```

#### Discussion

If you set this property, consider if you need to set [`colorUserInterfaceStyle`](pktoolpicker/coloruserinterfacestyle.md) to a select a different user interface style. The default user interface style is [`UIUserInterfaceStyle.unspecified`](https://developer.apple.com/documentation/UIKit/UIUserInterfaceStyle/unspecified).

## See Also

- [var isRulerActive: Bool](pktoolpicker/isruleractive.md)
  A Boolean value that indicates whether the ruler is visible on the canvas.
- [var colorUserInterfaceStyle: UIUserInterfaceStyle](pktoolpicker/coloruserinterfacestyle.md)
  The user interface style for the tool picker.
- [var showsDrawingPolicyControls: Bool](pktoolpicker/showsdrawingpolicycontrols.md)
  A Boolean value that indicates whether the default drawing policy UI is visible.
- [var stateAutosaveName: String?](pktoolpicker/stateautosavename.md)
  The name used to automatically save the tool picker’s state in the defaults system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpicker/overrideuserinterfacestyle)*