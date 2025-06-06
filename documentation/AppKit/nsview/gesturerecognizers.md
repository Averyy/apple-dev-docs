# gestureRecognizers

**Framework**: AppKit  
**Kind**: property

The gesture recognize objects currently attached to the view.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var gestureRecognizers: [NSGestureRecognizer] { get set }
```

#### Discussion

The objects in the array are concrete implementations of the `NSGestureRecognizer` class. If the view has no attached gesture recognizers, the array is empty.

## See Also

- [func addGestureRecognizer(NSGestureRecognizer)](nsview/addgesturerecognizer(_:).md)
  Attaches a gesture recognizer to the view.
- [func removeGestureRecognizer(NSGestureRecognizer)](nsview/removegesturerecognizer(_:).md)
  Detaches a gesture recognizer from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/gesturerecognizers)*