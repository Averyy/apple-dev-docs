# modelFileURL(for:)

**Framework**: RoomPlan  
**Kind**: method  
**Role**: Instance Method

Provides a URL to the 3D model for the given attributes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
func modelFileURL(for attributes: [any CapturedRoomAttribute]) throws -> URL?
```

#### Return Value

The 3D model that the app associates to the given object’s attributes via [`setModelFileURL(_:for:)`](./setmodelfileurl%28_,for%29-8xio.md). If no 3D model URL associates to the given attribute combination, this function returns `nil`.

#### Discussion

In error conditions, this function throws:

- [`CapturedRoom.ModelProvider.Error.nonExistingFile(url:)`](./error/nonexistingfile%28url%29.md) if a 3D model doesn’t exist at the given URL.
- [`CapturedRoom.ModelProvider.Error.attributeCombinationNotSupported`](./error/attributecombinationnotsupported.md) if no object category supports all of the argument attributes.

Query [`supportedCombinations`](../object/category-swift.enum/supportedcombinations.md) to check the attributes that an object category supports.

## Parameters

- `attributes`: An array of attributes that represent criteria for the model-URL query.

## See Also

### Managing models
- [var modelFileURLs: [URL]](./modelfileurls.md)
  An array of URLs to 3D models for all categories and attributes.
- [func modelFileURL(for: CapturedRoom.Object.Category) throws -> URL?](./modelfileurl%28for%29-9irqx.md)
  Provides a URL to the 3D model for the given category.
- [func modelFileURL(for: CapturedRoom.Object) throws -> URL?](./modelfileurl%28for%29-96rvb.md)
  Provides a URL to a 3D model based on the given object’s attributes or category.
- [func setModelFileURL(URL?, for: [any CapturedRoomAttribute]) throws](./setmodelfileurl%28_,for%29-8xio.md)
  Associates a URL to the given attributes.
- [func setModelFileURL(URL?, for: CapturedRoom.Object.Category) throws](./setmodelfileurl%28_,for%29-4law9.md)
  Associates a URL to the given object category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/modelprovider/modelfileurl(for:)-58ykp)*