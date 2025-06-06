# MTLCommandEncoderErrorState.pending

**Framework**: Metal  
**Kind**: case

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

## See Also

- [MTLCommandEncoderErrorState.completed](mtlcommandencodererrorstate/completed.md)
  A state that indicates the GPU successfully executed the commands without any errors.
- [MTLCommandEncoderErrorState.affected](mtlcommandencodererrorstate/affected.md)
  An error state that indicates the GPU failed to fully execute the commands because of an error.
- [MTLCommandEncoderErrorState.faulted](mtlcommandencodererrorstate/faulted.md)
  An error state that indicates the commands in the command buffer are the cause of an error.
- [MTLCommandEncoderErrorState.unknown](mtlcommandencodererrorstate/unknown.md)
  An error state that indicates the command buffer doesn’t know the state of its commands on the GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandencodererrorstate/pending)*