# modelFileURLs

**Framework**: RoomPlan  
**Kind**: property

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

- [func modelFileURL(for: CapturedRoom.Object.Category) throws -> URL?](capturedroom/modelprovider/modelfileurl(for:)-9irqx.md)
  Provides a URL to the 3D model for the given category.
- [func modelFileURL(for: CapturedRoom.Object) throws -> URL?](capturedroom/modelprovider/modelfileurl(for:)-96rvb.md)
  Provides a URL to a 3D model based on the given object’s attributes or category.
- [func modelFileURL(for: [any CapturedRoomAttribute]) throws -> URL?](capturedroom/modelprovider/modelfileurl(for:)-58ykp.md)
  Provides a URL to the 3D model for the given attributes.
- [func setModelFileURL(URL?, for: [any CapturedRoomAttribute]) throws](capturedroom/modelprovider/setmodelfileurl(_:for:)-8xio.md)
  Associates a URL to the given attributes.
- [func setModelFileURL(URL?, for: CapturedRoom.Object.Category) throws](capturedroom/modelprovider/setmodelfileurl(_:for:)-4law9.md)
  Associates a URL to the given object category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/modelprovider/modelfileurls)*