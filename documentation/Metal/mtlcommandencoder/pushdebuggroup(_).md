# pushDebugGroup(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Pushes a specific string onto a stack of debug group strings for the command encoder.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func pushDebugGroup(_ string: String)
```

```objc
- (void) pushDebugGroup:(NSString *) string;
```

## Discussion

For more information, see [Naming resources and commands](../../Xcode/naming-resources-and-commands.md).

## See Also

### Annotating the command buffer with debug information
- [func insertDebugSignpost(String)](./insertdebugsignpost%28_%29.md)
  Inserts a debug string into the captured frame data.
- [func popDebugGroup()](./popdebuggroup%28%29.md)
  Pops the latest string off of a stack of debug group strings for the command encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandencoder/pushdebuggroup(_:))*