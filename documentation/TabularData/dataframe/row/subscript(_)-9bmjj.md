# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses a slice from a range of indices.

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
subscript(bounds: Range<Int>) -> Slice<DataFrame.Row> { get set }
```

## Parameters

- `bounds`: A valid column index range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/row/subscript(_:)-9bmjj)*