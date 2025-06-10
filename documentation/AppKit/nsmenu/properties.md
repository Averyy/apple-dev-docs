# NSMenu.Properties

**Framework**: AppKit  
**Kind**: struct

These constants are used as a bitmask for specifying a set of menu or menu item properties, and are contained by the [`propertiesToUpdate`](nsmenu/propertiestoupdate.md) property.

**Availability**:
- macOS ?+

## Declaration

```swift
struct Properties
```

## Topics

### Constants
- [static var propertyItemTitle: NSMenu.Properties](nsmenu/properties/propertyitemtitle.md)
  The menu item’s title.
- [static var propertyItemAttributedTitle: NSMenu.Properties](nsmenu/properties/propertyitemattributedtitle.md)
  The menu item’s attributed string title.
- [static var propertyItemKeyEquivalent: NSMenu.Properties](nsmenu/properties/propertyitemkeyequivalent.md)
  The menu item’s key equivalent.
- [static var propertyItemImage: NSMenu.Properties](nsmenu/properties/propertyitemimage.md)
  The menu image.
- [static var propertyItemEnabled: NSMenu.Properties](nsmenu/properties/propertyitemenabled.md)
  Whether the menu item is enabled or disabled.
- [static var propertyItemAccessibilityDescription: NSMenu.Properties](nsmenu/properties/propertyitemaccessibilitydescription.md)
  The menu item’s accessibility description.
### Creating an NSMenu Property
- [init(rawValue: UInt)](nsmenu/properties/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/properties)*