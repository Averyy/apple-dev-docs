# overrideUserInterfaceStyle

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) UIUserInterfaceStyle overrideUserInterfaceStyle;
```

## Discussion

If you set this property, consider if you need to set [`colorUserInterfaceStyle`](./coloruserinterfacestyle.md) to a select a different user interface style. The default user interface style is [`UIUserInterfaceStyle.unspecified`](../../UIKit/uiuserinterfacestyle/unspecified.md).

## See Also

### Customizing picker behavior
- [var isRulerActive: Bool](./isruleractive.md)
  A Boolean value that indicates whether the ruler is visible on the canvas.
- [var colorUserInterfaceStyle: UIUserInterfaceStyle](./coloruserinterfacestyle.md)
  The user interface style for the tool picker.
- [var showsDrawingPolicyControls: Bool](./showsdrawingpolicycontrols.md)
  A Boolean value that indicates whether the default drawing policy UI is visible.
- [var stateAutosaveName: String?](./stateautosavename.md)
  The name used to automatically save the tool picker’s state in the defaults system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpicker/overrideuserinterfacestyle)*