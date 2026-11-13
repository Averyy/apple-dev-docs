# subscript(_:_:)

**Framework**: TabularData  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses a column as an array by its name.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@backDeployed(before: macOS 15.4, iOS 18.4, tvOS 18.4, watchOS 11.4, visionOS 2.4)
subscript<T>(columnName: String, type: T.Type = T.self) -> [T?] { get set }
```

## Parameters

- `columnName`: The name of a column.
- `type`: The type of the column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/subscript(_:_:)-6oqm0)*