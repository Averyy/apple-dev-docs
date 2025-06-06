# popDebugGroup()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Marks the end of a debug group and, if applicable, restores the previous group from a stack.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func popDebugGroup()
```

#### Discussion

Use [`pushDebugGroup(_:)`](mtlcommandbuffer/pushdebuggroup(_:).md) to group commands within the command buffer, which adds a new group to a stack, effectively nesting a group within any previous group. Call [`popDebugGroup()`](mtlcommandbuffer/popdebuggroup().md) to mark the end of a group of commands within the command buffer, and restore the previous group, if applicable. You can inspect the group and the commands it contains when viewing the contents of a frame capture with Metal Debugger.

Labels can help you profile and debug your app at runtime with Metal Debugger and other tools. See `Enhancing Frame Capture by Using Labels` for more information about using labels and other debugging techniques.

## See Also

- [func pushDebugGroup(String)](mtlcommandbuffer/pushdebuggroup(_:).md)
  Marks the beginning of a debug group and gives it an identifying label, which temporarily replaces the previous group, if applicable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/popdebuggroup())*