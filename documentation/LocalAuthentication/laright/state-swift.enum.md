# LARight.State

**Framework**: Local Authentication  
**Kind**: enum  
**Role**: Enumeration

The possible states for a right during authorization.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum State
```

```c
enum LARightState : NSInteger;
```

#### Overview

You can use key-value observation and the [Combine](../../Combine/Combine.md) framework to observe the authorization state of an [`LARight`](../laright.md) instance:

```swift
let right = LARight()
let cancellable = right
    .publisher(for: \.state)
    .sink { _ in
        print("Right updated to \(right.state)")
    }

try await right.authorize(localizedReason: "Access sandcastle competition designs")
```

## Topics

### Authorization states
- [LARight.State.authorizing](./state-swift.enum/authorizing.md)
  The authorization is in progress but not completed.
- [LARight.State.authorized](./state-swift.enum/authorized.md)
  The authorization completed successfully.
- [LARight.State.notAuthorized](./state-swift.enum/notauthorized.md)
  The authorization failed.
- [LARight.State.unknown](./state-swift.enum/unknown.md)
  The authorization is in an unknown state.
### Initializers
- [init?(rawValue: Int)](./state-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Authentication and access
- [class LARight](../laright.md)
  A grouped set of requirements that gate access to a resource or operation.
- [class LAContext](../lacontext.md)
  A mechanism for evaluating authentication policies and access controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laright/state-swift.enum)*