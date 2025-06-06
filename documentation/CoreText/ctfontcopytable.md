# CTFontCopyTable(_:_:_:)

**Framework**: Core Text  
**Kind**: func

Returns a reference to the font table data.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTFontCopyTable(_ font: CTFont, _ table: CTFontTableTag, _ options: CTFontTableOptions) -> CFData?
```

#### Return Value

A retained reference to the font table data as a [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData) object. The table data is not actually copied; however, the data reference must be released.

## Parameters

- `font`: The font reference.
- `table`: The font table identifier as a   constant. See   for possible values.
- `options`: The font table options.

## See Also

- [func CTFontCopyAvailableTables(CTFont, CTFontTableOptions) -> CFArray?](ctfontcopyavailabletables(_:_:).md)
  Returns an array of font table tags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcopytable(_:_:_:))*