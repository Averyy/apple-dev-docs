# containsAttachments(in:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates if the attributed string contains an attachment in the specified range.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func containsAttachments(in range: NSRange) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the attributed string contains a property configured as [`attachment`](nsattributedstring/key/attachment.md) with [`character`](https://developer.apple.com/documentation/AppKit/NSTextAttachment/character) in `range`; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `range`: The range.

## See Also

- [func size() -> CGSize](nsattributedstring/size.md)
  Returns the size necessary to draw the string.
- [func boundingRect(with: CGSize, options: NSStringDrawingOptions, context: NSStringDrawingContext?) -> CGRect](nsattributedstring/boundingrect(with:options:context:).md)
  Returns the bounding rectangle necessary to draw the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/containsattachments(in:))*