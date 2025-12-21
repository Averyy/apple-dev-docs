# autoenablesItems

**Framework**: AppKit  
**Kind**: property

Indicates whether the menu automatically enables and disables its menu items.

**Availability**:
- macOS ?+

## Declaration

```swift
var autoenablesItems: Bool { get set }
```

#### Discussion

This property contains a Boolean value, indicating whether the menu automatically enables and disables its menu items. If set to [`true`](https://developer.apple.com/documentation/Swift/true), menu items of the menu are automatically enabled and disabled according to rules computed by the NSMenuValidation informal protocol. By default, `NSMenu` objects autoenable their menu items.

## See Also

- [func update()](nsmenu/update.md)
  Enables or disables the menu items of the menu based on the NSMenuValidation informal protocol and sizes the menu to fit its current menu items if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/autoenablesitems)*