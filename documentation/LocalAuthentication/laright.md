# LARight

**Framework**: Local Authentication  
**Kind**: class  
**Role**: Class

A grouped set of requirements that gate access to a resource or operation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class LARight
```

```objc
@interface LARight : NSObject
```

#### Overview

Use [`LARight`](./laright.md) instances to protect access to portions of your app that may contain sensitive information. By default, [`LARight`](./laright.md) instances require people to authenticate with Face ID, Touch ID, Apple Watch, or the device passcode. The following creates an [`LARight`](./laright.md) with the default authentication requirements:

```swift
let loginRight = LARight()
    
func login() async throws {
    try await loginRight.authorize(localizedReason: "Access sandcastle competition designs")
}

func logout() async {
    await loginRight.deauthorize()
}
```

## Topics

### Authorizing a right
- [init()](./laright/init%28%29.md)
  Creates a right using the default authorization requirements.
- [init(requirement: LAAuthenticationRequirement)](./laright/init%28requirement%29.md)
  Creates a right with the authentication requirements you supply.
- [var tag: Int](./laright/tag.md)
  An integer you use to identify a right.
- [func authorize(localizedReason: String, completion: ((any Error)?) -> Void)](./laright/authorize%28localizedreason,completion%29.md)
  Performs an authorization on the right.
- [func authorize(localizedReason: String, in: LAPresentationContext, completion: ((any Error)?) -> Void)](./laright/authorize%28localizedreason,in,completion%29.md)
  Performs an authorization on the right with a window context you supply.
### Deauthorizing a right
- [func deauthorize(completion: () -> Void)](./laright/deauthorize%28completion%29.md)
  Invalidates a previously authorized right.
### Monitoring authorization status
- [func checkCanAuthorize(completion: ((any Error)?) -> Void)](./laright/checkcanauthorize%28completion%29.md)
  Checks whether the right has permission to perform authorization.
- [var state: LARight.State](./laright/state-swift.property.md)
  The current authorization state for a right.
- [LARight.State](./laright/state-swift.enum.md)
  The possible states for a right during authorization.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [LAPersistedRight](./lapersistedright.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Authentication and access
- [LARight.State](./laright/state-swift.enum.md)
  The possible states for a right during authorization.
- [class LAContext](./lacontext.md)
  A mechanism for evaluating authentication policies and access controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laright)*