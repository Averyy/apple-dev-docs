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
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CPMapPanelButtonConfiguration](cpmappanelbuttonconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppanelbuttonconfiguration)*