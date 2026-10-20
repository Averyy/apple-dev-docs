# addCompletedHandler(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Adds a closure that Metal calls immediately after the GPU finishes executing the commands in the input/output command buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func addCompletedHandler(_ block: @escaping MTLIOCommandBufferHandler)
```

```objc
- (void) addCompletedHandler:(MTLIOCommandBufferHandler) block;
```

## Parameters

- `block`: A Swift closure or an Objective-C block with your code.

## See Also

### Adding final commands
- [func copyStatus(buffer: any MTLBuffer, offset: Int)](./copystatus%28buffer,offset%29.md)
  Encodes a command that writes the input/output command buffer’s status to a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocommandbuffer/addcompletedhandler(_:))*