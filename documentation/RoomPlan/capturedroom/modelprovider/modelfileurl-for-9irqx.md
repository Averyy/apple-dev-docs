# modelFileURL(for:)

**Framework**: RoomPlan  
**Kind**: method

Provides a URL to the 3D model for the given category.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
func modelFileURL(for category: CapturedRoom.Object.Category) throws -> URL?
```

#### Return Value

The 3D model that the app associates to the given object’s category via [`setModelFileURL(_:for:)`](capturedroom/modelprovider/setmodelfileurl(_:for:)-4law9.md); or, `nil` if no 3D model URL associates to the given category.

#### Discussion

This function throws [`CapturedRoom.ModelProvider.Error.nonExistingFile(url:)`](capturedroom/modelprovider/error/nonexistingfile(url:).md) if a 3D model doesn’t exist at the given URL.

## Parameters

- `category`: An object type that represents criteria for the model-URL query.

## See Also

- [var modelFileURLs: [URL]](capturedroom/modelprovider/modelfileurls.md)
  An array of URLs to 3D models for all categories and attributes.
- [func modelFileURL(for: CapturedRoom.Object) throws -> URL?](capturedroom/modelprovider/modelfileurl(for:)-96rvb.md)
  Provides a URL to a 3D model based on the given object’s attributes or category.
- [func modelFileURL(for: [any CapturedRoomAttribute]) throws -> URL?](capturedroom/modelprovider/modelfileurl(for:)-58ykp.md)
  Provides a URL to the 3D model for the given attributes.
- [func setModelFileURL(URL?, for: [any CapturedRoomAttribute]) throws](capturedroom/modelprovider/setmodelfileurl(_:for:)-8xio.md)
  Associates a URL to the given attributes.
- [func setModelFileURL(URL?, for: CapturedRoom.Object.Category) throws](capturedroom/modelprovider/setmodelfileurl(_:for:)-4law9.md)
  Associates a URL to the given object category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/modelprovider/modelfileurl(for:)-9irqx)*