# removeGestureRecognizer(_:)

**Framework**: AppKit  
**Kind**: method

Detaches a gesture recognizer from the view.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func removeGestureRecognizer(_ gestureRecognizer: NSGestureRecognizer)
```

#### Discussion

Removing a gesture recognizer also removes the strong reference to it held by the view.

## Parameters

- `gestureRecognizer`: The gesture recognizer to remove. This parameter must not be  .

## See Also

- [var gestureRecognizers: [NSGestureRecognizer]](nsview/gesturerecognizers.md)
  The gesture recognize objects currently attached to the view.
- [func addGestureRecognizer(NSGestureRecognizer)](nsview/addgesturerecognizer(_:).md)
  Attaches a gesture recognizer to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/removegesturerecognizer(_:))*