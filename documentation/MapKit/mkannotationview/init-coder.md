# init(coder:)

**Framework**: MapKit  
**Kind**: init

Creates an annotation view using data from the specified unarchiver.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init?(coder aDecoder: NSCoder)
```

## Parameters

- `aDecoder`: The unarchiver to read data from.

## See Also

- [init(annotation: (any MKAnnotation)?, reuseIdentifier: String?)](mkannotationview/init(annotation:reuseidentifier:).md)
  Creates and returns a new annotation view.
- [func prepareForReuse()](mkannotationview/prepareforreuse.md)
  Calls this method when removing the view from the reuse queue.
- [func prepareForDisplay()](mkannotationview/preparefordisplay.md)
  Notifies the annotation view that the map view is about to display it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/init(coder:))*