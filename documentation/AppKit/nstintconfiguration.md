# NSTintConfiguration

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that gives you the ability to choose from system-provided tinting behaviors.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class NSTintConfiguration
```

```objc
@interface NSTintConfiguration : NSObject
```

## Topics

### Initializing a Tint Configuration
- [convenience init(fixedColor: NSColor)](./nstintconfiguration/init%28fixedcolor%29.md)
  Creates a new tint configuration using a specific color value.
- [convenience init(preferredColor: NSColor)](./nstintconfiguration/init%28preferredcolor%29.md)
  Creates a new tint configuration for the system to use when the app’s preferred accent color is in use.
### Changing an App’s Appearance
- [var adaptsToUserAccentColor: Bool](./nstintconfiguration/adaptstouseraccentcolor.md)
  A Boolean value that indicates whether the tint configuration alters its effect based on the user’s preferred accent color choice.
### Setting the Tint Color
- [class var `default`: NSTintConfiguration](./nstintconfiguration/default.md)
  The system tints the content using the system default value for its context.
- [class var monochrome: NSTintConfiguration](./nstintconfiguration/monochrome.md)
  The content always displays in monochrome.
- [var baseTintColor: NSColor?](./nstintconfiguration/basetintcolor.md)
  The color the system supplies when you create a tint configuration.
- [var equivalentContentTintColor: NSColor?](./nstintconfiguration/equivalentcontenttintcolor.md)
  A color object that matches the effective content tint.
### Initializers
- [init?(coder: NSCoder)](./nstintconfiguration/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Customizing Tint Color
- [func outlineView(NSOutlineView, tintConfigurationForItem: Any) -> NSTintConfiguration?](./nsoutlineviewdelegate/outlineview%28_,tintconfigurationforitem%29.md)
  Customizes an item’s tinting behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstintconfiguration)*