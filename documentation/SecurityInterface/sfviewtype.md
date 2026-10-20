# SFViewType

**Framework**: Security Interface  
**Kind**: struct  
**Role**: Structure

These constants define the view type requested by the authorization plug-in.

**Availability**:
- macOS 10.3+

## Declaration

```swift
struct SFViewType
```

```c
typedef enum { ... } SFViewType;
```

## Topics

### Initializers
- [init(UInt32)](./sfviewtype/init%28_%29.md)
- [init(rawValue: UInt32)](./sfviewtype/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt32](./sfviewtype/rawvalue.md)
### Constants
- [var SFViewTypeIdentityAndCredentials: SFViewType](./sfviewtypeidentityandcredentials.md)
  Indicates a view that contains controls for identity and credentials was requested by the authorization plug-in.
- [var SFViewTypeCredentials: SFViewType](./sfviewtypecredentials.md)
  Indicates a view that contains controls for credentials was requested by the authorization plug-in.

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
- [struct SFButtonType](./sfbuttontype.md)
  These constants define the button types used by authorization plug-ins.
- [SecurityInterface Constants](./securityinterface-constants.md)
  Constants in the SecurityInterface framework.
- [SecurityInterface Data Types](./securityinterface-data-types.md)
  Data types found in the Security Interface framework.
- [SecurityInterface Enumerations](./securityinterface-enumerations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfviewtype)*