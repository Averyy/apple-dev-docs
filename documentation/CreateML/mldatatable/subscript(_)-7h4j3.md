# subscript(_:)

**Framework**: Create ML  
**Kind**: subscript

Creates a subset of the table given a range of rows.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
subscript(slice: Range<Int>) -> MLDataTable { get }
```

#### Return Value

A new data table.

## Parameters

- `slice`: A range of integers indicating which rows to include in the new data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/subscript(_:)-7h4j3)*