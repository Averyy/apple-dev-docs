# CTFontCopyAvailableTables(_:_:)

**Framework**: Core Text  
**Kind**: func

Returns an array of font table tags.

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
func CTFontCopyAvailableTables(_ font: CTFont, _ options: CTFontTableOptions) -> CFArray?
```

#### Return Value

An array of [`CTFontTableTag`](ctfonttabletag.md) values for the given font and the supplied options.

#### Discussion

The returned set will contain unboxed values, which can be extracted like so:

```objc
CTFontTableTag tag = (CTFontTableTag)(uintptr_t)CFArrayGetValueAtIndex(tags, index);
```

## Parameters

- `font`: The font reference.
- `options`: The font table options.

## See Also

- [func CTFontCopyTable(CTFont, CTFontTableTag, CTFontTableOptions) -> CFData?](ctfontcopytable(_:_:_:).md)
  Returns a reference to the font table data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcopyavailabletables(_:_:))*