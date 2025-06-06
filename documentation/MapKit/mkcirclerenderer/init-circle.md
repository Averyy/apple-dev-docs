# init(circle:)

**Framework**: MapKit  
**Kind**: init

Creates a new overlay view using the specified circle overlay object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
init(circle: MKCircle)
```

#### Return Value

An initialized circle renderer object.

## Parameters

- `circle`: The circle overlay containing the information about the circular area for the renderer to draw. The renderer maintains a strong reference to the object you provide. This parameter can’t be  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkcirclerenderer/init(circle:))*