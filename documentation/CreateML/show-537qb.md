# show(_:_:)

**Framework**: Create ML  
**Kind**: func

Generates a streaming plot visualization of the two data columns.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func show<ElementX, ElementY>(_ x: MLDataColumn<ElementX>, _ y: MLDataColumn<ElementY>) -> any MLStreamingVisualizable where ElementX : MLDataValueConvertible, ElementY : MLDataValueConvertible
```

## See Also

- [func show(MLUntypedColumn, MLUntypedColumn) -> any MLStreamingVisualizable](show(_:_:)-2tmbf.md)
  Generates a streaming plot visualization of the two untyped columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/show(_:_:)-537qb)*