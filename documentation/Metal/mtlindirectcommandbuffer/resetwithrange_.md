# resetWithRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Resets a range of commands to their default state.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```objc
- (void) resetWithRange:(NSRange) range;
```

## Parameters

- `range`: The range of commands to reset. The range needs to fit inside the indirect command buffer’s extents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcommandbuffer/resetwithrange:)*