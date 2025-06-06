# init(anchor:content:)

**Framework**: MapKit  
**Kind**: init

Creates an annotation that displays a person’s current location using the system styled user location indicator with the specified anchor point using a custom view.

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
@preconcurrency init(anchor: UnitPoint = .center, @ViewBuilder content: @escaping (UserLocation) -> Content)
```

#### Return Value

Returns  a [`UserAnnotation`](userannotation.md) that displays a persons current location using the specified anchor location.

## Parameters

- `anchor`: A UnitPoint value that describes how to anchor the user location indicator to the person’s location. The default is  .
- `content`: The custom view to show at the person’s location.

## See Also

- [init()](userannotation/init.md)
  Creates an annotation that displays the person’s current location.
- [init(anchor: UnitPoint)](userannotation/init(anchor:).md)
  Creates an annotation that displays the person’s current location using the system styled user location indicator with the specified anchor point.
- [init(anchor: UnitPoint, content: () -> Content)](userannotation/init(anchor:content:)-3e78j.md)
  Create an annotation that displays the person’s current location of the user using a custom view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/userannotation/init(anchor:content:)-8u3r4)*