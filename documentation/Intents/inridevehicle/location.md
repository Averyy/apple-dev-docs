# location

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The most recent location of the vehicle.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var location: CLLocation? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) CLLocation * location;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) CLLocation * location;
```

#### Discussion

Siri uses this information to display the vehicle’s approximate location on the map. Siri and Maps use the image in the [`mapAnnotationImage`](./mapannotationimage.md) property to display the vehicle on the map.

## See Also

### Specifying the Vehicle’s Location
- [var mapAnnotationImage: INImage?](./mapannotationimage.md)
  The image to use for the vehicle when displaying its position on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridevehicle/location)*