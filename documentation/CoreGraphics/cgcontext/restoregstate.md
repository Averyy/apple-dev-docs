# restoreGState()

**Framework**: Core Graphics  
**Kind**: method

Sets the current graphics state to the state most recently saved.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func restoreGState()
```

#### Discussion

Core Graphics removes the graphics state at the top of the stack so that the most recently saved state becomes the current graphics state.

## See Also

- [func saveGState()](cgcontext/savegstate.md)
  Pushes a copy of the current graphics state onto the graphics state stack for the context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/restoregstate())*