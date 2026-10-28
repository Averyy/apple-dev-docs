# SFAuthorizationViewState

**Framework**: Security Interface  
**Kind**: struct  
**Role**: Structure

Defines the current state of the authorization view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
struct SFAuthorizationViewState
```

```c
typedef enum { ... } SFAuthorizationViewState;
```

## Overview

These constants are described in Constants in [`SFAuthorizationView`](./sfauthorizationview.md).

## Topics

### Initializers
- [init(UInt32)](./sfauthorizationviewstate/init%28_%29.md)
- [init(rawValue: UInt32)](./sfauthorizationviewstate/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt32](./sfauthorizationviewstate/rawvalue.md)
### Constants
- [var SFAuthorizationStartupState: SFAuthorizationViewState](./sfauthorizationstartupstate.md)
  Indicates that the state is starting up
- [var SFAuthorizationViewInProgressState: SFAuthorizationViewState](./sfauthorizationviewinprogressstate.md)
  Indicates that the state is in progress
- [var SFAuthorizationViewLockedState: SFAuthorizationViewState](./sfauthorizationviewlockedstate.md)
  Indicates that the state is locked
- [var SFAuthorizationViewUnlockedState: SFAuthorizationViewState](./sfauthorizationviewunlockedstate.md)
  Indicates that the state is unlocked

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Reference
- [struct SFButtonType](./sfbuttontype.md)
  These constants define the button types used by authorization plug-ins.
- [struct SFViewType](./sfviewtype.md)
  These constants define the view type requested by the authorization plug-in.
- [SecurityInterface Constants](./securityinterface-constants.md)
  Constants in the SecurityInterface framework.
- [SecurityInterface Data Types](./securityinterface-data-types.md)
  Data types found in the Security Interface framework.
- [SecurityInterface Enumerations](./securityinterface-enumerations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationviewstate)*