# popDebugGroup()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Pops the latest string off of a stack of debug group strings for the command encoder.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func popDebugGroup()
```

#### Discussion

For more information, see [`Naming resources and commands`](https://developer.apple.com/documentation/Xcode/Naming-resources-and-commands).

## See Also

- [func insertDebugSignpost(String)](mtlcommandencoder/insertdebugsignpost(_:).md)
  Inserts a debug string into the captured frame data.
- [func pushDebugGroup(String)](mtlcommandencoder/pushdebuggroup(_:).md)
  Pushes a specific string onto a stack of debug group strings for the command encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandencoder/popdebuggroup())*