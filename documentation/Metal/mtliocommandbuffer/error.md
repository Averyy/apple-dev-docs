# error

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

Stores the details of an error when the GPU experienced a problem with the input/output command buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var error: (any Error)? { get }
```

## See Also

- [var status: MTLIOStatus](mtliocommandbuffer/status.md)
  Represents the state of the input/output command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocommandbuffer/error)*