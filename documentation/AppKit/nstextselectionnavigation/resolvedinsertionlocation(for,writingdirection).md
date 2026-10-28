# resolvedInsertionLocation(for:writingDirection:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the location for inserting the next input depending on the state of the current and secondary selections.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func resolvedInsertionLocation(for textSelection: NSTextSelection, writingDirection: NSTextSelectionNavigation.WritingDirection) -> (any NSTextLocation)?
```

```objc
- (id<NSTextLocation>) resolvedInsertionLocationForTextSelection:(NSTextSelection *) textSelection writingDirection:(NSTextSelectionNavigationWritingDirection) writingDirection;
```

## Return Value

Returns an `NSTextLocation` when the `textSelection.isLogical = false AND` `secondarySelectionLocation != nil`. Otherwise, returns nil.

## Parameters

- `textSelection`: The text selection.
- `writingDirection`: The [`NSTextSelectionNavigation.WritingDirection`](./writingdirection.md) direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionnavigation/resolvedinsertionlocation(for:writingdirection:))*