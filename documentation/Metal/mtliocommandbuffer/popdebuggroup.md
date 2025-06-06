# popDebugGroup()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Restores the previous name for this input/output command encoder by removing the top item of the debug name stack.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func popDebugGroup()
```

## See Also

- [var label: String?](mtliocommandbuffer/label.md)
  An optional name for the input/output command buffer.
- [func pushDebugGroup(String)](mtliocommandbuffer/pushdebuggroup(_:).md)
  Sets the current name for this input/output command encoder by adding it to the top of the debug name stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocommandbuffer/popdebuggroup())*