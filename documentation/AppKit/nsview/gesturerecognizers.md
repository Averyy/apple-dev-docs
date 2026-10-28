# gestureRecognizers

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The gesture recognize objects currently attached to the view.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var gestureRecognizers: [NSGestureRecognizer] { get set }
```

```objc
@property (copy) NSArray<__kindof NSGestureRecognizer *> * gestureRecognizers;
```

## Discussion

The objects in the array are concrete implementations of the `NSGestureRecognizer` class. If the view has no attached gesture recognizers, the array is empty.

## See Also

### Managing gesture recognizers
- [func addGestureRecognizer(NSGestureRecognizer)](./addgesturerecognizer%28_%29.md)
  Attaches a gesture recognizer to the view.
- [func removeGestureRecognizer(NSGestureRecognizer)](./removegesturerecognizer%28_%29.md)
  Detaches a gesture recognizer from the view.
- [var exclusiveGestureBehavior: NSView.ExclusiveGestureBehavior](./exclusivegesturebehavior-swift.property.md)
  Declares whether gesture recognizers should be exclusive in this view and its subviews.
- [NSView.ExclusiveGestureBehavior](./exclusivegesturebehavior-swift.enum.md)
  Exclusive gesture behavior


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/gesturerecognizers)*