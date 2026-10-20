# SFButtonType

**Framework**: Security Interface  
**Kind**: struct  
**Role**: Structure

These constants define the button types used by authorization plug-ins.

**Availability**:
- macOS 10.3+

## Declaration

```swift
struct SFButtonType
```

```c
typedef enum { ... } SFButtonType;
```

## Topics

### Initializers
- [init(UInt32)](./sfbuttontype/init%28_%29.md)
- [init(rawValue: UInt32)](./sfbuttontype/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt32](./sfbuttontype/rawvalue.md)
### Constants
- [var SFButtonTypeCancel: SFButtonType](./sfbuttontypecancel.md)
  Indicates the Cancel button was pressed.
- [var SFButtonTypeOK: SFButtonType](./sfbuttontypeok.md)
  Indicates the OK button was pressed.
- [var SFButtonTypeBack: SFButtonType](./sfbuttontypeback.md)
  Indicates the Back button was pressed.
- [var SFButtonTypeLogin: SFButtonType](./sfbuttontypelogin.md)
  Indicates the Login button was pressed.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Reference
- [struct SFAuthorizationViewState](./sfauthorizationviewstate.md)
  Defines the current state of the authorization view.
- [struct SFViewType](./sfviewtype.md)
  These constants define the view type requested by the authorization plug-in.
- [SecurityInterface Constants](./securityinterface-constants.md)
  Constants in the SecurityInterface framework.
- [SecurityInterface Data Types](./securityinterface-data-types.md)
  Data types found in the Security Interface framework.
- [SecurityInterface Enumerations](./securityinterface-enumerations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfbuttontype)*