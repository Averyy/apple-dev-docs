# popDebugGroup()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) popDebugGroup;
```

#### Discussion

Use [`pushDebugGroup(_:)`](./pushdebuggroup%28_%29.md) to group commands within the command buffer, which adds a new group to a stack, effectively nesting a group within any previous group. Call [`popDebugGroup()`](./popdebuggroup%28%29.md) to mark the end of a group of commands within the command buffer, and restore the previous group, if applicable. You can inspect the group and the commands it contains when viewing the contents of a frame capture with Metal Debugger.

Labels can help you profile and debug your app at runtime with Metal Debugger and other tools. See [Naming resources and commands](../../Xcode/naming-resources-and-commands.md) for more information about using labels and other debugging techniques.

## See Also

### Grouping commands within a GPU frame capture
- [func pushDebugGroup(String)](./pushdebuggroup%28_%29.md)
  Marks the beginning of a debug group and gives it an identifying label, which temporarily replaces the previous group, if applicable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/popdebuggroup())*