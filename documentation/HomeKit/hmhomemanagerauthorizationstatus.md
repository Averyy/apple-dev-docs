# HMHomeManagerAuthorizationStatus

**Framework**: HomeKit  
**Kind**: struct  
**Role**: Structure

The possible home-access states.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct HMHomeManagerAuthorizationStatus
```

```c
enum HMHomeManagerAuthorizationStatus : NSUInteger;
```

#### Overview

Inspect the home manager’s [`authorizationStatus`](./hmhomemanager/authorizationstatus.md) property for one or more of the bits defined by [`HMHomeManagerAuthorizationStatus`](./hmhomemanagerauthorizationstatus.md).

## Topics

### Recognizing Status Values
- [static var determined: HMHomeManagerAuthorizationStatus](./hmhomemanagerauthorizationstatus/determined.md)
  The user has set the app’s level of access to home data.
- [static var authorized: HMHomeManagerAuthorizationStatus](./hmhomemanagerauthorizationstatus/authorized.md)
  The app has access to home data.
- [static var restricted: HMHomeManagerAuthorizationStatus](./hmhomemanagerauthorizationstatus/restricted.md)
  The app doesn’t have access to home data.
### Creating an Authorization Status
- [init(rawValue: UInt)](./hmhomemanagerauthorizationstatus/init%28rawvalue%29.md)
  Creates an access status from a raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Inspecting authorization status
- [var authorizationStatus: HMHomeManagerAuthorizationStatus](./hmhomemanager/authorizationstatus.md)
  The current state of the app’s access to home data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanagerauthorizationstatus)*