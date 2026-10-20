# popDebugGroup()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Pops the latest string off of a stack of debug group strings for the command encoder.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func popDebugGroup()
```

```objc
- (void) popDebugGroup;
```

#### Discussion

For more information, see [Naming resources and commands](../../Xcode/naming-resources-and-commands.md).

## See Also

### Annotating the command buffer with debug information
- [func insertDebugSignpost(String)](./insertdebugsignpost%28_%29.md)
  Inserts a debug string into the captured frame data.
- [func pushDebugGroup(String)](./pushdebuggroup%28_%29.md)
  Pushes a specific string onto a stack of debug group strings for the command encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandencoder/popdebuggroup())*