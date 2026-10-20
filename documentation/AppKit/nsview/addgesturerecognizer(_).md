# addGestureRecognizer(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Attaches a gesture recognizer to the view.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func addGestureRecognizer(_ gestureRecognizer: NSGestureRecognizer)
```

```objc
- (void) addGestureRecognizer:(NSGestureRecognizer *) gestureRecognizer;
```

#### Discussion

Attaching a gesture recognizer to a view defines the scope of the represented gesture, causing it to receive touches occurring only in the view or one of its subviews. The view establishes a strong reference to the specified gesture recognizer.

## Parameters

- `gestureRecognizer`: The gesture recognizer to attach to the view. This parameter must not be `nil`.

## See Also

### Managing gesture recognizers
- [var gestureRecognizers: [NSGestureRecognizer]](./gesturerecognizers.md)
  The gesture recognize objects currently attached to the view.
- [func removeGestureRecognizer(NSGestureRecognizer)](./removegesturerecognizer%28_%29.md)
  Detaches a gesture recognizer from the view.
- [var exclusiveGestureBehavior: NSView.ExclusiveGestureBehavior](./exclusivegesturebehavior-swift.property.md)
  Declares whether gesture recognizers should be exclusive in this view and its subviews.
- [NSView.ExclusiveGestureBehavior](./exclusivegesturebehavior-swift.enum.md)
  Exclusive gesture behavior


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/addgesturerecognizer(_:))*