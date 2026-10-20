# CapturedRoom.ModelProvider

**Framework**: RoomPlan  
**Kind**: struct  
**Role**: Structure

A structure that assigns detailed 3D models to captured objects for an export.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
struct ModelProvider
```

#### Overview

This structure provides a way for your app to assign detailed shape to specific areas within a captured room.

RoomPlan approximates the size and shape of objects it observes in a scan by using bounding boxes. In iOS 17 and later, the framework categorizes those objects that it recognizes by tagging them with specific attributes ([Captured Object Attributes](../captured-object-attributes.md)).

`ModelProvider` enables your app to export the categorized objects with unique 3D models. For example, you can assign a specific 3D model to a combination of attributes, such as all `.stool` objects with a `.star` base.

## Topics

### Creating a model provider
- [init()](./modelprovider/init%28%29.md)
  Creates a model provider.
### Managing models
- [var modelFileURLs: [URL]](./modelprovider/modelfileurls.md)
  An array of URLs to 3D models for all categories and attributes.
- [func modelFileURL(for: CapturedRoom.Object.Category) throws -> URL?](./modelprovider/modelfileurl%28for%29-9irqx.md)
  Provides a URL to the 3D model for the given category.
- [func modelFileURL(for: CapturedRoom.Object) throws -> URL?](./modelprovider/modelfileurl%28for%29-96rvb.md)
  Provides a URL to a 3D model based on the given object’s attributes or category.
- [func modelFileURL(for: [any CapturedRoomAttribute]) throws -> URL?](./modelprovider/modelfileurl%28for%29-58ykp.md)
  Provides a URL to the 3D model for the given attributes.
- [func setModelFileURL(URL?, for: [any CapturedRoomAttribute]) throws](./modelprovider/setmodelfileurl%28_,for%29-8xio.md)
  Associates a URL to the given attributes.
- [func setModelFileURL(URL?, for: CapturedRoom.Object.Category) throws](./modelprovider/setmodelfileurl%28_,for%29-4law9.md)
  Associates a URL to the given object category.
### Handling errors
- [CapturedRoom.ModelProvider.Error](./modelprovider/error.md)
  Errors that can occur when managing 3D model association with categories and attributes.

## See Also

### Generating a USDZ file
- [func export(to: URL, exportOptions: CapturedRoom.USDExportOptions) throws](./export%28to,exportoptions%29.md)
  Produces a 3D asset from the captured room.
- [func export(to: URL, metadataURL: URL?, modelProvider: CapturedRoom.ModelProvider?, exportOptions: CapturedRoom.USDExportOptions) throws](./export%28to,metadataurl,modelprovider,exportoptions%29.md)
  Produces a 3D asset from the captured room with the given metadata output URL and model provider.
- [CapturedRoom.USDExportOptions](./usdexportoptions.md)
  Options that determine the underlying data format of a scan export.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/modelprovider)*