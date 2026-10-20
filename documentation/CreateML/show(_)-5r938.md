# show(_:)

**Framework**: Create ML  
**Kind**: func  
**Role**: Function

Generates a streaming visualization of the data column.

**Availability**:
- macOS 10.15+ - Deprecated in 14.0

## Declaration

```swift
func show<Element>(_ column: MLDataColumn<Element>) -> any MLStreamingVisualizable where Element : MLDataValueConvertible
```

**Other overloads**:

```swift
func show(_ column: MLUntypedColumn) -> any MLStreamingVisualizable
```

```swift
func show(_ table: MLDataTable) -> any MLStreamingVisualizable
```

## See Also

### Column visualizations
- [func show(MLUntypedColumn) -> any MLStreamingVisualizable](./show%28_%29-9645r.md)
  Generates a streaming visualization of the untyped column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/show(_:)-5r938)*