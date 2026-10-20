# hidden

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

An attribute indicating the hidden style.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
static var hidden: UIMenuElement.Attributes { get }
```

```c
UIMenuElementAttributesHidden
```

#### Discussion

When you use this attribute, the menu system doesn’t display the menu element. However, if the menu element is a [`UIKeyCommand`](../../uikeycommand.md) object, the user can still select it using the keyboard shortcut specified by the key command object.

## See Also

### Attributes
- [static var destructive: UIMenuElement.Attributes](./destructive.md)
  An attribute indicating the destructive style.
- [static var disabled: UIMenuElement.Attributes](./disabled.md)
  An attribute indicating the disabled style.
- [static var keepsMenuPresented: UIMenuElement.Attributes](./keepsmenupresented.md)
  An attribute indicating that the menu remains presented after firing the element’s action instead of dismissing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/hidden)*