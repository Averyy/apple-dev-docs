# prepareForDisplay()

**Framework**: MapKit  
**Kind**: method

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
@MainActor
func prepareForDisplay()
```

#### Discussion

Use this method to prepare the content of your annotation view.

## See Also

- [init(annotation: (any MKAnnotation)?, reuseIdentifier: String?)](mkannotationview/init(annotation:reuseidentifier:).md)
  Creates and returns a new annotation view.
- [init?(coder: NSCoder)](mkannotationview/init(coder:).md)
  Creates an annotation view using data from the specified unarchiver.
- [func prepareForReuse()](mkannotationview/prepareforreuse.md)
  Calls this method when removing the view from the reuse queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/preparefordisplay())*