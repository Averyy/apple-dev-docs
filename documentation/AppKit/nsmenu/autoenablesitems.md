# autoenablesItems

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Indicates whether the menu automatically enables and disables its menu items.

**Availability**:
- macOS

## Declaration

```swift
var autoenablesItems: Bool { get set }
```

```objc
@property BOOL autoenablesItems;
```

## Discussion

This property contains a Boolean value, indicating whether the menu automatically enables and disables its menu items. If set to [`true`](../../Swift/true.md), menu items of the menu are automatically enabled and disabled according to rules computed by the NSMenuValidation informal protocol. By default, `NSMenu` objects autoenable their menu items.

## See Also

### Enabling and Disabling Menu Items
- [func update()](./update%28%29.md)
  Enables or disables the menu items of the menu based on the NSMenuValidation informal protocol and sizes the menu to fit its current menu items if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/autoenablesitems)*