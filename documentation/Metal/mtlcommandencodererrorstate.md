# MTLCommandEncoderErrorState

**Framework**: Metal  
**Kind**: enum

Possible error conditions for the command encoder’s commands.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLCommandEncoderErrorState
```

## Topics

### Getting the error state
- [MTLCommandEncoderErrorState.completed](mtlcommandencodererrorstate/completed.md)
  A state that indicates the GPU successfully executed the commands without any errors.
- [MTLCommandEncoderErrorState.pending](mtlcommandencodererrorstate/pending.md)
  An error state that indicates the GPU didn’t execute the commands.
- [MTLCommandEncoderErrorState.affected](mtlcommandencodererrorstate/affected.md)
  An error state that indicates the GPU failed to fully execute the commands because of an error.
- [MTLCommandEncoderErrorState.faulted](mtlcommandencodererrorstate/faulted.md)
  An error state that indicates the commands in the command buffer are the cause of an error.
- [MTLCommandEncoderErrorState.unknown](mtlcommandencodererrorstate/unknown.md)
  An error state that indicates the command buffer doesn’t know the state of its commands on the GPU.
### Initializers
- [init?(rawValue: Int)](mtlcommandencodererrorstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var label: String](mtlcommandbufferencoderinfo/label.md)
  The name of the encoder that generates the error information.
- [var debugSignposts: [String]](mtlcommandbufferencoderinfo/debugsignposts.md)
  An array of debug signposts that Metal records as the GPU executes the commands of the encoder’s pass.
- [var errorState: MTLCommandEncoderErrorState](mtlcommandbufferencoderinfo/errorstate.md)
  The execution status of the command encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandencodererrorstate)*