# compositionRenderer()

**Framework**: Quartz  
**Kind**: method

Returns the renderer object associated with the composition parameter view.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func compositionRenderer() -> (any QCCompositionRenderer)!
```

#### Return Value

A renderer object or `nil`, if the composition parameter view is not set to a renderer object.

## See Also

- [func setCompositionRenderer((any QCCompositionRenderer)!)](qccompositionparameterview/setcompositionrenderer(_:).md)
  Sets the composition parameter view for editing the input parameters of the provided renderer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionparameterview/compositionrenderer())*