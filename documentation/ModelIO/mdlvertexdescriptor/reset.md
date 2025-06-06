# reset()

**Framework**: Model I/O  
**Kind**: method

Resets a vertex descriptor to its default state.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func reset()
```

#### Discussion

Calling this method returns the descriptor to its original state, as is produced when initializing a vertex descriptor with the inherited [`init()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/init()) method. After calling this method, the descriptor contains a single empty [`MDLVertexAttribute`](mdlvertexattribute.md) object and a single empty [`MDLVertexBufferLayout`](mdlvertexbufferlayout.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvertexdescriptor/reset())*