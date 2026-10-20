# modelFileURLs

**Framework**: RoomPlan  
**Kind**: property  
**Role**: Instance Property

An array of URLs to 3D models for all categories and attributes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var modelFileURLs: [URL] { get }
```

## See Also

### Managing models
- [func modelFileURL(for: CapturedRoom.Object.Category) throws -> URL?](./modelfileurl%28for%29-9irqx.md)
  Provides a URL to the 3D model for the given category.
- [func modelFileURL(for: CapturedRoom.Object) throws -> URL?](./modelfileurl%28for%29-96rvb.md)
  Provides a URL to a 3D model based on the given object’s attributes or category.
- [func modelFileURL(for: [any CapturedRoomAttribute]) throws -> URL?](./modelfileurl%28for%29-58ykp.md)
  Provides a URL to the 3D model for the given attributes.
- [func setModelFileURL(URL?, for: [any CapturedRoomAttribute]) throws](./setmodelfileurl%28_,for%29-8xio.md)
  Associates a URL to the given attributes.
- [func setModelFileURL(URL?, for: CapturedRoom.Object.Category) throws](./setmodelfileurl%28_,for%29-4law9.md)
  Associates a URL to the given object category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/modelprovider/modelfileurls)*