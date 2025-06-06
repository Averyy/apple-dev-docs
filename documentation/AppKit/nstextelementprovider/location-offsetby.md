# location(_:offsetBy:)

**Framework**: AppKit  
**Kind**: method

Returns a new location from location with offset you provide.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func location(_ location: any NSTextLocation, offsetBy offset: Int) -> (any NSTextLocation)?
```

#### Return Value

An new `NSTextLocation`, or `nil` of the offset exceeds the bounds of the text.

## Parameters

- `location`: An   in the text element.
- `offset`: An offset of the number of characters to or from  .

## See Also

- [func enumerateTextElements(from: (any NSTextLocation)?, options: NSTextContentManager.EnumerationOptions, using: (NSTextElement) -> Bool) -> (any NSTextLocation)?](nstextelementprovider/enumeratetextelements(from:options:using:).md)
  Enumerates text elements starting at the text location you provide.
- [NSTextLayoutFragment.EnumerationOptions](nstextlayoutfragment/enumerationoptions.md)
  Values that describe options for enumerating text layout fragments.
- [func replaceContents(in: NSTextRange, with: [NSTextElement]?)](nstextelementprovider/replacecontents(in:with:).md)
  Replaces the characters specified by range with the text elements you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextelementprovider/location(_:offsetby:))*