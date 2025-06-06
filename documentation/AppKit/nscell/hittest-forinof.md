# hitTest(for:in:of:)

**Framework**: AppKit  
**Kind**: method

Returns hit testing information for the receiver.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func hitTest(for event: NSEvent, in cellFrame: NSRect, of controlView: NSView) -> NSCell.HitResult
```

#### Return Value

A constant that specifies the type of area in which the event occurred—see [`NSCell.HitResult`](nscell/hitresult.md) for values.

#### Discussion

You can use a bit-wise mask to look for a specific value when calling this method—see [`NSCell.HitResult`](nscell/hitresult.md) for values.

Generally, this method should be overridden by custom `NSCell` subclasses to return the correct result. Currently, it is called by some multi-cell views, such as `NSTableView`.

By default, `NSCell` looks at the cell type and does the following:

- `NSImageCellType`: If the image exists and the event point is in the image returns `NSCellHitContentArea`, otherwise `NSCellHitNone`.
- `NSTextCellType` (also applies to `NSTextFieldCell`):

If there is text: If the event point hits in the text, return `NSCellHitContentArea`. Additionally, if the cell is enabled return `NSCellHitContentArea` `|` `NSCellHitEditableTextArea`.

If there is not text: return `NSCellHitNone`.

- `NSNullCellType` (this is the default that applies to non text or image cells who don’t override [`hitTest(for:in:of:)`](nscell/hittest(for:in:of:).md)):

Return `NSCellHitContentArea` by default;

If the cell not disabled, and it would track, return `NSCellHitContentArea` `|` `NSCellHitTrackableArea`.

## Parameters

- `event`: The current event.
- `cellFrame`: The cell’s frame.
- `controlView`: The control object in which the cell is located.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/hittest(for:in:of:))*