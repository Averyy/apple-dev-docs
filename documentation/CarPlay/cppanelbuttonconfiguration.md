# CPPanelButtonConfiguration

**Framework**: CarPlay  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
class CPPanelButtonConfiguration
```

#### Overview

A panel list section. It contains a primary and secondary action button.

## Topics

### Initializers
- [init?(coder: NSCoder)](cppanelbuttonconfiguration/init(coder:).md)
- [init(primaryAction: CPTextButton, secondaryAction: CPTextButton?)](cppanelbuttonconfiguration/init(primaryaction:secondaryaction:).md)
  Initializes a button configuration with a primary action and an optional secondary action.
### Instance Properties
- [var primaryAction: CPTextButton](cppanelbuttonconfiguration/primaryaction.md)
  The primary action button.
- [var secondaryAction: CPTextButton?](cppanelbuttonconfiguration/secondaryaction.md)
  The secondary action button, or @c nil if excluded.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [CPMapPanelButtonConfiguration](cpmappanelbuttonconfiguration.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppanelbuttonconfiguration)*