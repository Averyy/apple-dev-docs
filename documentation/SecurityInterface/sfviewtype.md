# SFViewType

**Framework**: Security Interface  
**Kind**: struct

These constants define the view type requested by the authorization plug-in.

**Availability**:
- macOS 10.3+

## Declaration

```swift
struct SFViewType
```

## Topics

### Initializers
- [init(UInt32)](sfviewtype/init(_:).md)
- [init(rawValue: UInt32)](sfviewtype/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt32](sfviewtype/rawvalue.md)
### Constants
- [var SFViewTypeIdentityAndCredentials: SFViewType](sfviewtypeidentityandcredentials.md)
  Indicates a view that contains controls for identity and credentials was requested by the authorization plug-in.
- [var SFViewTypeCredentials: SFViewType](sfviewtypecredentials.md)
  Indicates a view that contains controls for credentials was requested by the authorization plug-in.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct SFAuthorizationViewState](sfauthorizationviewstate.md)
  Defines the current state of the authorization view.
- [struct SFButtonType](sfbuttontype.md)
  These constants define the button types used by authorization plug-ins.
- [SecurityInterface Constants](securityinterface-constants.md)
  Constants in the SecurityInterface framework.
- [SecurityInterface Data Types](securityinterface-data-types.md)
  Data types found in the Security Interface framework.
- [SecurityInterface Enumerations](securityinterface-enumerations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfviewtype)*