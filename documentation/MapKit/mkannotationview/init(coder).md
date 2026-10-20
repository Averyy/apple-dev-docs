# init(coder:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

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
init?(coder aDecoder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) aDecoder;
```

## Parameters

- `aDecoder`: The unarchiver to read data from.

## See Also

### Creating and preparing an annotation view
- [init(annotation: (any MKAnnotation)?, reuseIdentifier: String?)](./init%28annotation,reuseidentifier%29.md)
  Creates and returns a new annotation view.
- [func prepareForReuse()](./prepareforreuse%28%29.md)
  Calls this method when removing the view from the reuse queue.
- [func prepareForDisplay()](./preparefordisplay%28%29.md)
  Notifies the annotation view that the map view is about to display it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/init(coder:))*