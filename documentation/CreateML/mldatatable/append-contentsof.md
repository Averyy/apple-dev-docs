# append(contentsOf:)

**Framework**: Create ML  
**Kind**: method

Appends the contents of the given data table to the end of this data table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
mutating func append(contentsOf newTable: MLDataTable)
```

#### Discussion

> ❗ **Important**: The columns of both data tables must have the same names and types. Otherwise, the data table will be invalidated.

## Parameters

- `newTable`: Another data table to append to the data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/append(contentsof:))*