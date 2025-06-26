# insertDebugSignpost(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Inserts a debug string into the captured frame data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func insertDebugSignpost(_ string: String)
```

#### Discussion

For more information, see [`Naming resources and commands`](https://developer.apple.com/documentation/Xcode/Naming-resources-and-commands).

## See Also

- [func pushDebugGroup(String)](mtlcommandencoder/pushdebuggroup(_:).md)
  Pushes a specific string onto a stack of debug group strings for the command encoder.
- [func popDebugGroup()](mtlcommandencoder/popdebuggroup.md)
  Pops the latest string off of a stack of debug group strings for the command encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandencoder/insertdebugsignpost(_:))*