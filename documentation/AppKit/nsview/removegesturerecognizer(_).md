# removeGestureRecognizer(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Detaches a gesture recognizer from the view.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func removeGestureRecognizer(_ gestureRecognizer: NSGestureRecognizer)
```

```objc
- (void) removeGestureRecognizer:(NSGestureRecognizer *) gestureRecognizer;
```

## Discussion

Removing a gesture recognizer also removes the strong reference to it held by the view.

## Parameters

- `gestureRecognizer`: The gesture recognizer to remove. This parameter must not be `nil`.

## See Also

### Managing gesture recognizers
- [var gestureRecognizers: [NSGestureRecognizer]](./gesturerecognizers.md)
  The gesture recognize objects currently attached to the view.
- [func addGestureRecognizer(NSGestureRecognizer)](./addgesturerecognizer%28_%29.md)
  Attaches a gesture recognizer to the view.
- [var exclusiveGestureBehavior: NSView.ExclusiveGestureBehavior](./exclusivegesturebehavior-swift.property.md)
  Declares whether gesture recognizers should be exclusive in this view and its subviews.
- [NSView.ExclusiveGestureBehavior](./exclusivegesturebehavior-swift.enum.md)
  Exclusive gesture behavior


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/removegesturerecognizer(_:))*