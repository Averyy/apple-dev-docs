# MTLCommandEncoderErrorState.pending

**Framework**: Metal  
**Kind**: case  
**Role**: Case

An error state that indicates the GPU didn’t execute the commands.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case pending
```

```c
MTLCommandEncoderErrorStatePending
```

## See Also

### Getting the error state
- [MTLCommandEncoderErrorState.completed](./completed.md)
  A state that indicates the GPU successfully executed the commands without any errors.
- [MTLCommandEncoderErrorState.affected](./affected.md)
  An error state that indicates the GPU failed to fully execute the commands because of an error.
- [MTLCommandEncoderErrorState.faulted](./faulted.md)
  An error state that indicates the commands in the command buffer are the cause of an error.
- [MTLCommandEncoderErrorState.unknown](./unknown.md)
  An error state that indicates the command buffer doesn’t know the state of its commands on the GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandencodererrorstate/pending)*