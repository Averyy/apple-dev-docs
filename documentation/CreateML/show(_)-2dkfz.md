# show(_:)

**Framework**: Create ML  
**Kind**: func  
**Role**: Function

Generates a streaming visualization of the data table.

**Availability**:
- macOS 10.15+ - Deprecated in 14.0

## Declaration

```swift
func show(_ table: MLDataTable) -> any MLStreamingVisualizable
```

**Other overloads**:

```swift
func show(_ column: MLUntypedColumn) -> any MLStreamingVisualizable
```

```swift
func show<Element>(_ column: MLDataColumn<Element>) -> any MLStreamingVisualizable where Element : MLDataValueConvertible
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/show(_:)-2dkfz)*