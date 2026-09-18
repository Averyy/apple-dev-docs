# CPPanelButtonConfiguration

**Framework**: CarPlay  
**Kind**: class

A type that provides the common behaviors for a button layout in a panel.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
class CPPanelButtonConfiguration
```

#### Overview

The `CPPanelButtonConfiguration` type defines the default behaviors for button configurations in a panel. You don’t create this type directly or use it to configure your panel. Instead, instantiate one of the defined subclasses based on the type of panel you’re configuring. For example, create a [`CPMapPanelButtonConfiguration`](cpmappanelbuttonconfiguration.md) object when configuring content for a [`CPMapPanel`](cpmappanel.md) type.

## Topics

### Initializers
- [init?(coder: NSCoder)](cppanelbuttonconfiguration/init(coder:).md)
- [init(primaryAction: CPTextButton, secondaryAction: CPTextButton?)](cppanelbuttonconfiguration/init(primaryaction:secondaryaction:).md)
  Initializes the button configuration object with the specified buttons.
### Instance Properties
- [var primaryAction: CPTextButton](cppanelbuttonconfiguration/primaryaction.md)
  The primary action button for the panel.
- [var secondaryAction: CPTextButton?](cppanelbuttonconfiguration/secondaryaction.md)
  An optional action button to display in the panel.

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