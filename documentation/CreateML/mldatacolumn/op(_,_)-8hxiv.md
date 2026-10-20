# /(_:_:)

**Framework**: Create ML  
**Kind**: op

Creates a column of doubles by dividing the given double by each element of the given column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func / (a: Double, b: MLDataColumn<Double>) -> MLDataColumn<Double>
```

#### Return Value

A new column of doubles.

## Parameters

- `a`: A double.
- `b`: A column of doubles.

## See Also

- [static +(_:_:)](mldatacolumn/+(_:_:).md)
  Creates a column of doubles by adding the given double to each element of the given column.
- [static -(_:_:)](mldatacolumn/-(_:_:).md)
  Creates a column of doubles by subtracting each element of the given column from the given double.
- [static *(_:_:)](mldatacolumn/*(_:_:).md)
  Creates a column of doubles by multiplying the given double by each element of the given column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/_(_:_:)-8hxiv)*