# init(anchor:)

**Framework**: MapKit  
**Kind**: init

Creates an annotation that displays the person’s current location using the system styled user location indicator with the specified anchor point.

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
@preconcurrency init(anchor: UnitPoint = .center) where Content == EmptyView
```

## Parameters

- `anchor`: How to anchor the user location indicator around the user’s location. The default is  .

## See Also

- [init()](userannotation/init.md)
  Creates an annotation that displays the person’s current location.
- [init(anchor: UnitPoint, content: (UserLocation) -> Content)](userannotation/init(anchor:content:)-8u3r4.md)
  Creates an annotation that displays a person’s current location using the system styled user location indicator with the specified anchor point using a custom view.
- [init(anchor: UnitPoint, content: () -> Content)](userannotation/init(anchor:content:)-3e78j.md)
  Create an annotation that displays the person’s current location of the user using a custom view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/userannotation/init(anchor:))*