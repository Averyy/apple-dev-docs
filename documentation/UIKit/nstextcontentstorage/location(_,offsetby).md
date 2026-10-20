# location(_:offsetBy:)

**Framework**: UIKit  
**Kind**: method

Returns a new text location object based on an existing location and offset you provide.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func location(_ location: any NSTextLocation, offsetBy offset: Int) -> (any NSTextLocation)?
```

#### Return Value

An [`NSTextLocation`](nstextlocation.md) object that corresponds to the new location, or `nil` if the new location exceeds the bounds of the text.

#### Discussion

You can get [`NSTextLocation`](nstextlocation.md) objects for the start and end of the text storage from the [`documentRange`](nstextelementprovider/documentrange.md) property of the [`NSTextElementProvider`](nstextelementprovider.md) protocol, which [`NSTextContentStorage`](nstextcontentstorage.md) implements. If you provide an [`NSTextLocation`](nstextlocation.md) object doesn’t match the type of the ones in the [`documentRange`](nstextelementprovider/documentrange.md) property, this method throws an exception.

## Parameters

- `location`: The starting location. For example, you might specify the beginning or end of the document as the starting location.
- `offset`: The number of characters from the starting location. Specify a positive integer to create a location object that comes after the starting location. Specify a negative number to create a location object that comes before the starting location.

## See Also

- [func offset(from: any NSTextLocation, to: any NSTextLocation) -> Int](nstextcontentstorage/offset(from:to:).md)
  Returns the number of characters between the specified locations.
- [func adjustedRange(from: NSTextRange, forEditingTextSelection: Bool) -> NSTextRange?](nstextcontentstorage/adjustedrange(from:foreditingtextselection:).md)
  Returns the text range, if any, in the backing store that required manual adjustment after editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontentstorage/location(_:offsetby:))*