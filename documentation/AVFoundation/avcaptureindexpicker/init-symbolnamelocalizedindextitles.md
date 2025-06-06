# init(_:symbolName:localizedIndexTitles:)

**Framework**: AVFoundation  
**Kind**: init

Creates an object to select an index from a set of values.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
init(_ localizedTitle: String, symbolName: String, localizedIndexTitles: [String])
```

#### Discussion

Create a picker with this initializer when you already have an array containing a title for each picked value.

## Parameters

- `localizedTitle`: A localized title that describes the control’s action.
- `symbolName`: The name of an SF Symbol that represents the control.
- `localizedIndexTitles`: The titles to use for each index. The array must not be empty.

## See Also

- [init(String, symbolName: String, numberOfIndexes: Int)](avcaptureindexpicker/init(_:symbolname:numberofindexes:).md)
  Creates a control to pick a value from the specified number of indexes.
- [init(String, symbolName: String, numberOfIndexes: Int, localizedTitleTransform: (Int) -> String)](avcaptureindexpicker/init(_:symbolname:numberofindexes:localizedtitletransform:).md)
  Creates a control to pick a value from the specified number of indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureindexpicker/init(_:symbolname:localizedindextitles:))*