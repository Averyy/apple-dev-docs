# range(of:options:in:)

**Framework**: Foundation  
**Kind**: method

Finds the range of the specified data as a subsequence of this data, if it exists.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func range(of dataToFind: Data, options: Data.SearchOptions = [], in range: Range<Data.Index>? = nil) -> Range<Data.Index>?
```

#### Return Value

A `Range` specifying the location of the found data, or nil if a match could not be found.

#### Discussion

Precondition: `range` must be in the bounds of the Data.

## Parameters

- `dataToFind`: The data to be searched for.
- `options`: Options for the search. Default value is  .
- `range`: The range of this data in which to perform the search. Default value is  , which means the entire content of this data.

## See Also

- [typealias SearchOptions](data/searchoptions.md)
  Options that control a data search operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/range(of:options:in:))*