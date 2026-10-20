# MKLookAroundSceneRequest

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

A class you use to request a LookAround scene at the location you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MKLookAroundSceneRequest
```

```objc
@interface MKLookAroundSceneRequest : NSObject
```

## Topics

### Creating a LookAround scene
- [init(coordinate: CLLocationCoordinate2D)](./mklookaroundscenerequest/init%28coordinate%29.md)
  Creates a LookAround scene at the specified coordinates.
- [init(mapItem: MKMapItem)](./mklookaroundscenerequest/init%28mapitem%29.md)
  Creates a LookAround scene with the location described by the specified map item.
### Specifying the request’s location
- [var coordinate: CLLocationCoordinate2D](./mklookaroundscenerequest/coordinate.md)
  A coordinate value that describes the location of the LookAround scene.
- [var mapItem: MKMapItem?](./mklookaroundscenerequest/mapitem.md)
  A map item that describes the location of the LookAround scene.
### Starting and stopping scene requests
- [func cancel()](./mklookaroundscenerequest/cancel%28%29.md)
  Cancels the pending scene request.
- [func getSceneWithCompletionHandler((MKLookAroundScene?, (any Error)?) -> Void)](./mklookaroundscenerequest/getscenewithcompletionhandler%28_%29.md)
  Requests a LookAround scene and calls the specified completion handler.
### Monitoring the progress of scene requests
- [var isCancelled: Bool](./mklookaroundscenerequest/iscancelled.md)
  A Boolean value that indicates if the cancellation of a scene request was successful.
- [var isLoading: Bool](./mklookaroundscenerequest/isloading.md)
  A Boolean value that indicates whether a scene request is loading.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Exploring at street level
- [class MKLookAroundScene](./mklookaroundscene.md)
  A utility class that encapsulates information the framework requires to retrieve and display a specific Look Around location’s imagery.
- [class MKLookAroundViewController](./mklookaroundviewcontroller.md)
  A class that manages the presentation and display of a LookAround view.
- [class MKLookAroundSnapshotter](./mklookaroundsnapshotter.md)
  A utility class that you use to create a static image from a LookAround scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklookaroundscenerequest)*