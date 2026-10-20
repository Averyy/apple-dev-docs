# setModelFileURL(_:for:)

**Framework**: RoomPlan  
**Kind**: method  
**Role**: Instance Method

Associates a URL to the given object category.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
mutating func setModelFileURL(_ url: URL?, for category: CapturedRoom.Object.Category) throws
```

#### Discussion

This function throws [`CapturedRoom.ModelProvider.Error.nonExistingFile(url:)`](./error/nonexistingfile%28url%29.md) if a 3D model doesn’t exist at the given URL.

## Parameters

- `url`: A URL to a 3D model.
- `category`: The object type associated with the model URL.

## See Also

### Managing models
- [var modelFileURLs: [URL]](./modelfileurls.md)
  An array of URLs to 3D models for all categories and attributes.
- [func modelFileURL(for: CapturedRoom.Object.Category) throws -> URL?](./modelfileurl%28for%29-9irqx.md)
  Provides a URL to the 3D model for the given category.
- [func modelFileURL(for: CapturedRoom.Object) throws -> URL?](./modelfileurl%28for%29-96rvb.md)
  Provides a URL to a 3D model based on the given object’s attributes or category.
- [func modelFileURL(for: [any CapturedRoomAttribute]) throws -> URL?](./modelfileurl%28for%29-58ykp.md)
  Provides a URL to the 3D model for the given attributes.
- [func setModelFileURL(URL?, for: [any CapturedRoomAttribute]) throws](./setmodelfileurl%28_,for%29-8xio.md)
  Associates a URL to the given attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/modelprovider/setmodelfileurl(_:for:)-4law9)*