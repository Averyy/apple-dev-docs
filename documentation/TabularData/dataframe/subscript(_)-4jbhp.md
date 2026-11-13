# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses a result column by its typed descriptor.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
subscript<T>(column: ResultColumn<T>) -> Column<T> { get }
```

## See Also

### Accessing evaluation results
- [subscript(metric _: Metric) -> Column<Metric>](./subscript%28metric%29.md)
  Accesses a metric column using the metric’s name


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/subscript(_:)-4jbhp)*