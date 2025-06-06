# init(someCount:noneCount:uniqueCount:mode:)

**Framework**: TabularData  
**Kind**: init

Creates a categorical summary.

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
init(someCount: Int, noneCount: Int, uniqueCount: Int, mode: [Element])
```

## Parameters

- `someCount`: The number of elements in a column, excluding missing elements.
- `noneCount`: The number of missing elements in the column.
- `uniqueCount`: The number of elements with distinct values in a column, ignoring missing elements.
- `mode`: The most common values in a column, ignoring missing elements.

## See Also

- [init()](categoricalsummary/init.md)
  Creates a categorical summary with default values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/categoricalsummary/init(somecount:nonecount:uniquecount:mode:))*