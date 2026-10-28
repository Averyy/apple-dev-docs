# location(_:offsetBy:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a new location from location with offset you provide.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
optional func location(_ location: any NSTextLocation, offsetBy offset: Int) -> (any NSTextLocation)?
```

```objc
- (id<NSTextLocation>) locationFromLocation:(id<NSTextLocation>) location withOffset:(NSInteger) offset;
```

## Return Value

An new `NSTextLocation`, or `nil` of the offset exceeds the bounds of the text.

## Parameters

- `location`: An [`NSTextLocation`](../nstextlocation.md) in the text element.
- `offset`: An offset of the number of characters to or from `location`.

## See Also

### Accessing and updating the text
- [func enumerateTextElements(from: (any NSTextLocation)?, options: NSTextContentManager.EnumerationOptions, using: (NSTextElement) -> Bool) -> (any NSTextLocation)?](./enumeratetextelements%28from,options,using%29.md)
  Enumerates text elements starting at the text location you provide.
- [NSTextLayoutFragment.EnumerationOptions](../nstextlayoutfragment/enumerationoptions.md)
  Values that describe options for enumerating text layout fragments.
- [func replaceContents(in: NSTextRange, with: [NSTextElement]?)](./replacecontents%28in,with%29.md)
  Replaces the characters specified by range with the text elements you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextelementprovider/location(_:offsetby:))*