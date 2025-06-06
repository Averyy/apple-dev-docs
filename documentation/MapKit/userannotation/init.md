# init()

**Framework**: MapKit  
**Kind**: init

Creates an annotation that displays the person’s current location.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency init() where Content == DefaultUserAnnotationContent
```

## See Also

- [init(anchor: UnitPoint)](userannotation/init(anchor:).md)
  Creates an annotation that displays the person’s current location using the system styled user location indicator with the specified anchor point.
- [init(anchor: UnitPoint, content: (UserLocation) -> Content)](userannotation/init(anchor:content:)-8u3r4.md)
  Creates an annotation that displays a person’s current location using the system styled user location indicator with the specified anchor point using a custom view.
- [init(anchor: UnitPoint, content: () -> Content)](userannotation/init(anchor:content:)-3e78j.md)
  Create an annotation that displays the person’s current location of the user using a custom view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/userannotation/init())*