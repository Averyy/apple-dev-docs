# Providing custom models for captured rooms and structure exports

**Framework**: RoomPlan

Enhance the look of an exported 3D model by substituting object bounding boxes with detailed 3D renditions.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.2+
- Xcode 16.2+

#### Overview

> **Note**: This sample code project is associated with WWDC23 session 10192: [`Explore enhancements to RoomPlan`](https://developer.apple.comhttps://developer.apple.com/wwdc23/10192).

##### Configure the Sample Code Project

Before you run the `RoomPlanExporter` target in Xcode:

1. Set the run destination to an iOS 17 or later device; this app doesn’t support Simulator.
2. Export a scanned room in JSON format, which you generate with the [`Create a 3D model of an interior room by guiding the user through an AR experience`](create-a-3d-model-of-an-interior-room-by-guiding-the-user-through-an-ar-experience.md). Alternatively, you can generate a JSON export of several rooms merged into a single structure by using the [`Merging multiple scans into a single structure`](merging-multiple-scans-into-a-single-structure.md).

To run the app:

1. Run the `RoomPlanExporter` target.
2. Tap Open a CapturedRoom and choose a scanned room or structure in JSON format in the Open File dialog.
3. Tap Export and choose the Model option.
4. Tap Share Export and observe the output files in the resulting `Export` folder. The USDZ output file features a detailed 3D model in replacement for any object in the room that the framework recognizes during the scan as being one of the known object types from the target’s `RoomPlanCatalog.bundle`.

The `RoomPlanCatalogGenerator` target in Xcode provides a command-line tool that enables you to generate your own catalog of 3D models similar to the `RoomPlanCatalog.bundle` in this sample code project. Before running the tool, set the run destination to a macOS 14 or later device with Mac Catalyst, and enable the command-line argument as follows:

1. Select the `RoomPlanCatalogGenerator` scheme and choose Edit Scheme.
2. Select the Run task’s Arguments tab.
3. Click or tap the checkbox to enable just the first argument:

```None
create-folders -i "~/RoomPlan/Catalog/"
```

1. Run the scheme in Xcode, which creates a folder structure at the `~/RoomPlan/Catalog` location on disk.
2. Fill the folder structure with 3D models that correspond to the folder names. The folder names correspond to the types of objects and attributes that RoomPlan recognizes during a scan. The framework supports 3D models in `.usdc` format (preferred), and `.abc`, `.obj`, `.ply`, or `.stl` formats.
3. If you don’t have your own 3D models, you can use the 3D models that this sample code project provides by substituting the `~/RoomPlan/Catalog/Resources` folder on disk for the sample code project’s `/RoomPlanExporter/RoomPlanCatalog.bundle/Resources` folder.
4. Select the `RoomPlanCatalogGenerator` scheme and choose ‘Edit Scheme’.
5. In the Run task’s Arguments pane, click or tap the checkbox to enable just the second argument:

```None
generate -i "~/RoomPlan/Catalog" \
         -o "~/RoomPlan/RoomPlanCatalog.bundle"
```

1. Run the scheme in Xcode, which generates a `RoomPlanCatalog.bundle` file from the folder structure filled with 3D models.
2. Place a scanned room in JSON format at the `~/RoomPlan/Room.json` path on disk. You generate the file by exporting a scanned room with the [`Create a 3D model of an interior room by guiding the user through an AR experience`](create-a-3d-model-of-an-interior-room-by-guiding-the-user-through-an-ar-experience.md), or by exporting several rooms merged into a single structure with the [`Merging multiple scans into a single structure`](merging-multiple-scans-into-a-single-structure.md).
3. Select the `RoomPlanCatalogGenerator` scheme and choose ‘Edit Scheme’.
4. In the Run task’s Arguments pane, click or tap the checkbox to enable just the third argument:

```None
convert -i "~/RoomPlan/Room.json" \
        -c "~/RoomPlan/RoomPlanCatalog.bundle" \ 
        -o "~/RoomPlan/Room.usdz"
```

1. Run the scheme in Xcode, which converts the serialized room or structure to a USDZ file at path `~/RoomPlan/Room.usdz` on disk that includes substituted 3D models from the catalog bundle.

## See Also

- [class RoomBuilder](roombuilder.md)
  An object that generates a 3D asset from room-capture data.
- [class StructureBuilder](structurebuilder.md)
  An object that combines multiple scan sessions into a single captured result.
- [CapturedRoom.USDExportOptions](capturedroom/usdexportoptions.md)
  Options that determine the underlying data format of a scan export.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/providing-custom-models-for-captured-rooms-and-structure-exports)*