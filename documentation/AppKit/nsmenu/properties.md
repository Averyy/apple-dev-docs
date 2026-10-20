# NSMenu.Properties

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

These constants are used as a bitmask for specifying a set of menu or menu item properties, and are contained by the [`propertiesToUpdate`](./propertiestoupdate.md) property.

**Availability**:
- macOS

## Declaration

```swift
struct Properties
```

```c
enum NSMenuProperties : NSUInteger;
```

## Topics

### Constants
- [static var propertyItemTitle: NSMenu.Properties](./properties/propertyitemtitle.md)
  The menu item’s title.
- [static var propertyItemAttributedTitle: NSMenu.Properties](./properties/propertyitemattributedtitle.md)
  The menu item’s attributed string title.
- [static var propertyItemKeyEquivalent: NSMenu.Properties](./properties/propertyitemkeyequivalent.md)
  The menu item’s key equivalent.
- [static var propertyItemImage: NSMenu.Properties](./properties/propertyitemimage.md)
  The menu image.
- [static var propertyItemEnabled: NSMenu.Properties](./properties/propertyitemenabled.md)
  Whether the menu item is enabled or disabled.
- [static var propertyItemAccessibilityDescription: NSMenu.Properties](./properties/propertyitemaccessibilitydescription.md)
  The menu item’s accessibility description.
### Creating an NSMenu Property
- [init(rawValue: UInt)](./properties/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/properties)*