# init(anchor:content:)

**Framework**: MapKit  
**Kind**: init

Create an annotation that displays the person’s current location of the user using a custom view.

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
@preconcurrency init(anchor: UnitPoint = .center, @ViewBuilder content: @escaping () -> Content)
```

## Parameters

- `anchor`: How to anchor the user location indicator around the person’s location. The default is  .
- `content`: The custom view used to indicate the person’s location.

## See Also

- [init()](userannotation/init.md)
  Creates an annotation that displays the person’s current location.
- [init(anchor: UnitPoint)](userannotation/init(anchor:).md)
  Creates an annotation that displays the person’s current location using the system styled user location indicator with the specified anchor point.
- [init(anchor: UnitPoint, content: (UserLocation) -> Content)](userannotation/init(anchor:content:)-8u3r4.md)
  Creates an annotation that displays a person’s current location using the system styled user location indicator with the specified anchor point using a custom view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/userannotation/init(anchor:content:)-3e78j)*