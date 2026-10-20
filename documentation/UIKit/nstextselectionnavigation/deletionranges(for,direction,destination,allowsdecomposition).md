# deletionRanges(for:direction:destination:allowsDecomposition:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the ranges for deleting the text based on the current selection and movement arguments.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func deletionRanges(for textSelection: NSTextSelection, direction: NSTextSelectionNavigation.Direction, destination: NSTextSelectionNavigation.Destination, allowsDecomposition: Bool) -> [NSTextRange]
```

```objc
- (NSArray<NSTextRange *> *) deletionRangesForTextSelection:(NSTextSelection *) textSelection direction:(NSTextSelectionNavigationDirection) direction destination:(NSTextSelectionNavigationDestination) destination allowsDecomposition:(BOOL) allowsDecomposition;
```

#### Return Value

An array of text ranges to delete.

#### Discussion

The selection after deletion contains a zero-length range starting at the location of the first range returned. The framework ignores the destination when `textSelection` has a non-empty selection. The `allowsDecomposition` parameter only applies to the [`NSTextSelectionNavigation.Direction.backward`](./direction/backward.md) direction and [`NSTextSelectionNavigation.Destination.character`](./destination/character.md) with a zero-length selection.

## Parameters

- `textSelection`: The text selection.
- `direction`: The [`NSTextSelectionNavigation.Direction`](./direction.md) to consider when calculating the deletion ranges.
- `destination`: The [`NSTextSelectionNavigation.Destination`](./destination.md) that describes the scope of the text selection to consider when calculating the deletion ranges.
- `allowsDecomposition`: A Boolean value that determines if this method operates on composite characters which may be present depending on the characteristics of the script used by `textSelection`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectionnavigation/deletionranges(for:direction:destination:allowsdecomposition:))*