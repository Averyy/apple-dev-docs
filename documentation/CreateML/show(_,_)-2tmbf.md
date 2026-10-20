# show(_:_:)

**Framework**: Create ML  
**Kind**: func  
**Role**: Function

Generates a streaming plot visualization of the two untyped columns.

**Availability**:
- macOS 10.15+ - Deprecated in 14.0

## Declaration

```swift
func show(_ x: MLUntypedColumn, _ y: MLUntypedColumn) -> any MLStreamingVisualizable
```

**Other overloads**:

```swift
func show<ElementX, ElementY>(_ x: MLDataColumn<ElementX>, _ y: MLDataColumn<ElementY>) -> any MLStreamingVisualizable where ElementX : MLDataValueConvertible, ElementY : MLDataValueConvertible
```

## See Also

### Plot visualizations
- [func show<ElementX, ElementY>(MLDataColumn<ElementX>, MLDataColumn<ElementY>) -> any MLStreamingVisualizable](./show%28_,_%29-537qb.md)
  Generates a streaming plot visualization of the two data columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/show(_:_:)-2tmbf)*