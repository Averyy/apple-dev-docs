# LARight.State

**Framework**: Local Authentication  
**Kind**: enum

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

#### Overview

You can use key-value observation and the [`Combine`](https://developer.apple.com/documentation/Combine) framework to observe the authorization state of an [`LARight`](laright.md) instance:

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
- [LARight.State.authorizing](laright/state-swift.enum/authorizing.md)
  The authorization is in progress but not completed.
- [LARight.State.authorized](laright/state-swift.enum/authorized.md)
  The authorization completed successfully.
- [LARight.State.notAuthorized](laright/state-swift.enum/notauthorized.md)
  The authorization failed.
- [LARight.State.unknown](laright/state-swift.enum/unknown.md)
  The authorization is in an unknown state.
### Initializers
- [init?(rawValue: Int)](laright/state-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class LARight](laright.md)
  A grouped set of requirements that gate access to a resource or operation.
- [class LAContext](lacontext.md)
  A mechanism for evaluating authentication policies and access controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laright/state-swift.enum)*