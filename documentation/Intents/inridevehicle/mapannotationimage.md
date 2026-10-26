# mapAnnotationImage

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The image to use for the vehicle when displaying its position on the map.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var mapAnnotationImage: INImage? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INImage * mapAnnotationImage;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INImage * mapAnnotationImage;
```

## Mentions

- [Providing Live Status Updates](../../SiriKit/providing-live-status-updates.md)

#### Discussion

The image you provide should be a top-down image of your vehicle, and the front of the vehicle should be at the top of your image. When added to the map, Maps centers the image on the vehicle’s [`location`](./location.md). Maps rotates the image to match the current direction in which the vehicle is going.

## See Also

### Specifying the Vehicle’s Location
- [var location: CLLocation?](./location.md)
  The most recent location of the vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridevehicle/mapannotationimage)*