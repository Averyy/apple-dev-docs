# status

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Represents the state of the input/output command buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var status: MTLIOStatus { get }
```

```objc
@property (readonly) MTLIOStatus status;
```

## See Also

### Checking the state of a command buffer
- [var error: (any Error)?](./error.md)
  Stores the details of an error when the GPU experienced a problem with the input/output command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocommandbuffer/status)*