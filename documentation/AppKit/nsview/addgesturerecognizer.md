# addGestureRecognizer(_:)

**Framework**: AppKit  
**Kind**: method

Attaches a gesture recognizer to the view.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func addGestureRecognizer(_ gestureRecognizer: NSGestureRecognizer)
```

#### Discussion

Attaching a gesture recognizer to a view defines the scope of the represented gesture, causing it to receive touches occurring only in the view or one of its subviews. The view establishes a strong reference to the specified gesture recognizer.

## Parameters

- `gestureRecognizer`: The gesture recognizer to attach to the view. This parameter must not be  .

## See Also

- [var gestureRecognizers: [NSGestureRecognizer]](nsview/gesturerecognizers.md)
  The gesture recognize objects currently attached to the view.
- [func removeGestureRecognizer(NSGestureRecognizer)](nsview/removegesturerecognizer(_:).md)
  Detaches a gesture recognizer from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/addgesturerecognizer(_:))*