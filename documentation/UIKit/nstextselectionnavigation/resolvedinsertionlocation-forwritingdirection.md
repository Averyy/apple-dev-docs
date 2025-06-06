# resolvedInsertionLocation(for:writingDirection:)

**Framework**: UIKit  
**Kind**: method

Returns the location for inserting the next input depending on the state of the current and secondary selections.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func resolvedInsertionLocation(for textSelection: NSTextSelection, writingDirection: NSTextSelectionNavigation.WritingDirection) -> (any NSTextLocation)?
```

#### Return Value

Returns an `NSTextLocation` when the `textSelection.isLogical = false AND` `secondarySelectionLocation != nil`. Otherwise, returns nil.

## Parameters

- `textSelection`: The text selection.
- `writingDirection`: The   direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectionnavigation/resolvedinsertionlocation(for:writingdirection:))*