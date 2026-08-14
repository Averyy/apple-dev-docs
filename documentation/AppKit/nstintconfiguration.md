# NSTintConfiguration

**Framework**: AppKit  
**Kind**: class

An object that gives you the ability to choose from system-provided tinting behaviors.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class NSTintConfiguration
```

## Topics

### Initializing a Tint Configuration
- [convenience init(fixedColor: NSColor)](nstintconfiguration/init(fixedcolor:).md)
  Creates a new tint configuration using a specific color value.
- [convenience init(preferredColor: NSColor)](nstintconfiguration/init(preferredcolor:).md)
  Creates a new tint configuration for the system to use when the app’s preferred accent color is in use.
### Changing an App’s Appearance
- [var adaptsToUserAccentColor: Bool](nstintconfiguration/adaptstouseraccentcolor.md)
  A Boolean value that indicates whether the tint configuration alters its effect based on the user’s preferred accent color choice.
### Setting the Tint Color
- [class var `default`: NSTintConfiguration](nstintconfiguration/default.md)
  The system tints the content using the system default value for its context.
- [class var monochrome: NSTintConfiguration](nstintconfiguration/monochrome.md)
  The content always displays in monochrome.
- [var baseTintColor: NSColor?](nstintconfiguration/basetintcolor.md)
  The color the system supplies when you create a tint configuration.
- [var equivalentContentTintColor: NSColor?](nstintconfiguration/equivalentcontenttintcolor.md)
  A color object that matches the effective content tint.
### Initializers
- [init?(coder: NSCoder)](nstintconfiguration/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [func outlineView(NSOutlineView, tintConfigurationForItem: Any) -> NSTintConfiguration?](nsoutlineviewdelegate/outlineview(_:tintconfigurationforitem:).md)
  Customizes an item’s tinting behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstintconfiguration)*