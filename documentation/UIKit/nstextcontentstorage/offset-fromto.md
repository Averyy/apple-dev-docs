# offset(from:to:)

**Framework**: UIKit  
**Kind**: method

Returns the number of characters between the specified locations.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func offset(from: any NSTextLocation, to: any NSTextLocation) -> Int
```

#### Return Value

The number of characters between the start and end locations. If the to location comes before the from location, the returned value is negative.

#### Discussion

You can get [`NSTextLocation`](nstextlocation.md) objects for the start and end of the text storage from the [`documentRange`](nstextelementprovider/documentrange.md) property of the [`NSTextElementProvider`](nstextelementprovider.md) protocol, which [`NSTextContentStorage`](nstextcontentstorage.md) implements. If you provide an [`NSTextLocation`](nstextlocation.md) object doesn’t match the type of the ones in the [`documentRange`](nstextelementprovider/documentrange.md) property, this method throws an exception.

## Parameters

- `from`: The starting location in the text storage. For example, you might specify the beginning of the document as the starting location.
- `to`: The end location in the text storage.

## See Also

- [func location(any NSTextLocation, offsetBy: Int) -> (any NSTextLocation)?](nstextcontentstorage/location(_:offsetby:).md)
  Returns a new text location object based on an existing location and offset you provide.
- [func adjustedRange(from: NSTextRange, forEditingTextSelection: Bool) -> NSTextRange?](nstextcontentstorage/adjustedrange(from:foreditingtextselection:).md)
  Returns the text range, if any, in the backing store that required manual adjustment after editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontentstorage/offset(from:to:))*