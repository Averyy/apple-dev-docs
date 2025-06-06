# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript

Returns a slice of the column by selecting elements with a collection of Booleans.

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
subscript<C>(mask: C) -> AnyColumnSlice where C : Collection, C.Element == Bool { get }
```

## Parameters

- `mask`: A collection of Booleans.   The method selects the column’s elements that correspond to the   elements in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumn/subscript(_:)-3658g)*