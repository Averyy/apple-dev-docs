# CTFontCopyTable(_:_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

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

```c
extern CFDataRefCTFontCopyTable(CTFontRef font, CTFontTableTag table, CTFontTableOptions options);
```

## Return Value

A retained reference to the font table data as a [`CFData`](../CoreFoundation/cfdata.md) object. The table data is not actually copied; however, the data reference must be released.

## Parameters

- `font`: The font reference.
- `table`: The font table identifier as a [`CTFontTableTag`](./ctfonttabletag.md) constant. See [`CTFontTableTag`](./ctfonttabletag.md) for possible values.
- `options`: The font table options.

## See Also

### Getting Font Table Data
- [func CTFontCopyAvailableTables(CTFont, CTFontTableOptions) -> CFArray?](./ctfontcopyavailabletables%28_,_%29.md)
  Returns an array of font table tags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcopytable(_:_:_:))*