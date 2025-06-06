# debugSignposts

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

An array of debug signposts that Metal records as the GPU executes the commands of the encoder’s pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var debugSignposts: [String] { get }
```

## See Also

- [var label: String](mtlcommandbufferencoderinfo/label.md)
  The name of the encoder that generates the error information.
- [var errorState: MTLCommandEncoderErrorState](mtlcommandbufferencoderinfo/errorstate.md)
  The execution status of the command encoder.
- [enum MTLCommandEncoderErrorState](mtlcommandencodererrorstate.md)
  Possible error conditions for the command encoder’s commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbufferencoderinfo/debugsignposts)*