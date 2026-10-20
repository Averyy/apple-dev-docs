# prepareForDisplay()

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Notifies the annotation view that the map view is about to display it.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func prepareForDisplay()
```

```objc
- (void) prepareForDisplay;
```

#### Discussion

Use this method to prepare the content of your annotation view.

## See Also

### Creating and preparing an annotation view
- [init(annotation: (any MKAnnotation)?, reuseIdentifier: String?)](./init%28annotation,reuseidentifier%29.md)
  Creates and returns a new annotation view.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates an annotation view using data from the specified unarchiver.
- [func prepareForReuse()](./prepareforreuse%28%29.md)
  Calls this method when removing the view from the reuse queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/preparefordisplay())*