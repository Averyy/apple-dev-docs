# init(_:symbolName:numberOfIndexes:localizedTitleTransform:)

**Framework**: AVFoundation  
**Kind**: init

Creates a control to pick a value from the specified number of indices.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
init(_ localizedTitle: String, symbolName: String, numberOfIndexes: Int, localizedTitleTransform: (Int) -> String)
```

#### Discussion

Create a picker with this initializer if your app requires specifying a title for each value lazily.

## Parameters

- `localizedTitle`: A localized title that describes the picker’s action.
- `symbolName`: The name of the symbol from the SF Symbols library to use to represent this control.
- `numberOfIndexes`: The number of indexes to pick between. This value must be greater than  .
- `localizedTitleTransform`: A transformation from index to localized title.

## See Also

- [init(String, symbolName: String, numberOfIndexes: Int)](avcaptureindexpicker/init(_:symbolname:numberofindexes:).md)
  Creates a control to pick a value from the specified number of indexes.
- [init(String, symbolName: String, localizedIndexTitles: [String])](avcaptureindexpicker/init(_:symbolname:localizedindextitles:).md)
  Creates an object to select an index from a set of values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureindexpicker/init(_:symbolname:numberofindexes:localizedtitletransform:))*