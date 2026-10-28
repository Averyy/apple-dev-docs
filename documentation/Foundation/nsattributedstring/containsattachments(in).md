# containsAttachments(in:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) containsAttachmentsInRange:(NSRange) range;
```

## Return Value

[`true`](../../Swift/true.md) if the attributed string contains a property configured as [`attachment`](./key/attachment.md) with [`character`](../../AppKit/nstextattachment/character.md) in `range`; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `range`: The range.

## See Also

### Getting metrics for the string
- [func size() -> CGSize](./size%28%29.md)
  Returns the size necessary to draw the string.
- [func boundingRect(with: CGSize, options: NSStringDrawingOptions, context: NSStringDrawingContext?) -> CGRect](./boundingrect%28with,options,context%29.md)
  Returns the bounding rectangle necessary to draw the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/containsattachments(in:))*