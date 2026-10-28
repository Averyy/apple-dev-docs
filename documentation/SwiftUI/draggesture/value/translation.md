# translation

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The total translation from the start of the drag gesture to the current event of the drag gesture.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var translation: CGSize { get }
```

## Discussion

This is equivalent to `location.{x,y} - startLocation.{x,y}`.

## See Also

### Getting 2D position
- [var startLocation: CGPoint](./startlocation.md)
  The location of the drag gesture’s first event.
- [var location: CGPoint](./location.md)
  The location of the drag gesture’s current event.
- [var predictedEndLocation: CGPoint](./predictedendlocation.md)
  A prediction, based on the current drag velocity, of where the final location will be if dragging stopped now.
- [var predictedEndTranslation: CGSize](./predictedendtranslation.md)
  A prediction, based on the current drag velocity, of what the final translation will be if dragging stopped now.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/draggesture/value/translation)*