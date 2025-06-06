# keepsMenuPresented

**Framework**: UIKit  
**Kind**: property

An attribute indicating that the menu remains presented after firing the element’s action instead of dismissing.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static var keepsMenuPresented: UIMenuElement.Attributes { get }
```

#### Discussion

Use this attribute to allow a person to perform a menu action multiple times without dismissing the menu in between.

This attribute doesn’t have an effect if you build your app with Mac Catalyst.

## See Also

- [static var destructive: UIMenuElement.Attributes](uimenuelement/attributes/destructive.md)
  An attribute indicating the destructive style.
- [static var disabled: UIMenuElement.Attributes](uimenuelement/attributes/disabled.md)
  An attribute indicating the disabled style.
- [static var hidden: UIMenuElement.Attributes](uimenuelement/attributes/hidden.md)
  An attribute indicating the hidden style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/keepsmenupresented)*