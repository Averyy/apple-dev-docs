# Captured Object Attributes

**Framework**: RoomPlan

Determine details about the objects and surfaces that the framework identifies in a scan.

#### Overview

Each [`CapturedRoom.Object`](capturedroom/object.md) contains attributes that the framework observes during a scan that convey details about the object. For example, an object of category [`CapturedRoom.Object.Category.chair`](capturedroom/object/category-swift.enum/chair.md) may contain the attributes [`ChairType.stool`](chairtype/stool.md) and [`ChairLegType.star`](chairlegtype/star.md), which describes the framework’s observations of the chair during the scan. An object exposes these details through its [`attributes`](capturedroom/object/attributes.md) array.

By reading the attribute information the framework sets on objects, your app can provide more informed utility with a scanned room, such as:

- A filtered list of product selections in a furniture catalog that matches just the categories and attributes of the present objects in the room.
- A more accurate visual representation, for example when rendering a virtual reality experience, by substituting the default object bounding boxes with detailed 3D models that your app chooses.

> 💡 **Tip**: If you export a scan result to USDZ, for example, with [`export(to:metadataURL:modelProvider:exportOptions:)`](capturedroom/export(to:metadataurl:modelprovider:exportoptions:).md), objects output as bounding boxes. To substitute the boxes with detailed 3D models based on object attributes, see [`CapturedRoom.ModelProvider`](capturedroom/modelprovider.md).

## Topics

### Accessing object details
- [protocol CapturedRoomAttribute](capturedroomattribute.md)
  Details about an object in the room that the framework observes during a scan.
- [enum CapturedElementCategory](capturedelementcategory.md)
  The category of the particular object or surface.
### Describing chairs
- [enum ChairType](chairtype.md)
  Types of chair that the framework identifies in a captured room.
- [enum ChairArmType](chairarmtype.md)
  Types of armchair the framework identifies in a captured room.
- [enum ChairLegType](chairlegtype.md)
  Types of chair legs the framework identifies in a captured room.
- [enum ChairBackType](chairbacktype.md)
  Types of chair back the framework identifies in a captured room.
### Describing sofas
- [enum SofaType](sofatype.md)
  Types of sofa the framework identifies in a captured room.
### Describing closets
- [enum StorageType](storagetype.md)
  Types of storage area that the framework identifies in a captured room.
### Describing tables
- [enum TableType](tabletype.md)
  Types of table the framework identifies in a captured room.
- [enum TableShapeType](tableshapetype.md)
  Different table shapes that the framework identifies in a captured room.

## See Also

- [Merging multiple scans into a single structure](merging-multiple-scans-into-a-single-structure.md)
  Export a 3D model that consists of multiple rooms captured in the same physical vicinity.
- [Scanning the rooms of a single structure](scanning-the-rooms-of-a-single-structure.md)
  Create an AR experience that enables people to scan a building that contains multiple rooms.
- [struct CapturedRoom](capturedroom.md)
  A structure that provides the key details of a scanned room.
- [struct CapturedStructure](capturedstructure.md)
  An object that holds the results of the merger of multiple capture sessions.
- [struct CapturedRoomData](capturedroomdata.md)
  An opaque object that holds the raw results of a scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/captured-object-attributes)*