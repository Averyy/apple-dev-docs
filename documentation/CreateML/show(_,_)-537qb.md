# show(_:_:)

**Framework**: Create ML  
**Kind**: func  
**Role**: Function

Generates a streaming plot visualization of the two data columns.

**Availability**:
- macOS 10.15+ - Deprecated in 14.0

## Declaration

```swift
func show<ElementX, ElementY>(_ x: MLDataColumn<ElementX>, _ y: MLDataColumn<ElementY>) -> any MLStreamingVisualizable where ElementX : MLDataValueConvertible, ElementY : MLDataValueConvertible
```

**Other overloads**:

```swift
func show(_ x: MLUntypedColumn, _ y: MLUntypedColumn) -> any MLStreamingVisualizable
```

## See Also

### Plot visualizations
- [func show(MLUntypedColumn, MLUntypedColumn) -> any MLStreamingVisualizable](./show%28_,_%29-2tmbf.md)
  Generates a streaming plot visualization of the two untyped columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/show(_:_:)-537qb)*