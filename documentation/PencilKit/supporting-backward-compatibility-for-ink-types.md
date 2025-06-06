# Supporting backward compatibility for ink types

**Framework**: PencilKit

Leverage the latest PencilKit features while providing a good user experience in earlier versions of the OS that don’t support those features.

#### Overview

In iPadOS 17, PencilKit becomes even more expressive by introducing the monoline, fountain pen, watercolor, and crayon inks. Earlier versions of the OS can’t render [`PKDrawing`](pkdrawing-swift.struct.md) objects that use these inks because the system doesn’t contain a version of PencilKit that supports them. As a result, earlier versions of the OS throw an error when attempting to load a [`PKDrawing`](pkdrawing-swift.struct.md) object that contains these inks from data.

You can handle this situation in your app in one of two ways:

- Support backward compatibility. Let people use the new inks when your app runs in the latest version of the OS. Before you save a drawing and sync the data to other devices, check its required content version to determine if it uses the new inks. If it does, provide a good fallback experience for devices that can’t load that drawing, like syncing a fallback drawing that’s compatible with the earlier version of PencilKit.
- Restrict the use of new features. Limit which inks are available when your app runs in any version of the OS. This approach ensures that the PencilKit data your app saves is compatible with the earlier version of PencilKit, but it doesn’t let people take advantage of the new inks.

##### Support Backward Compatibility Using the Required Content Version

To support backward compatibility, PencilKit introduces content versioning through [`PKContentVersion`](pkcontentversion.md). Data model types like [`PKDrawing`](pkdrawing-swift.struct.md), [`PKStroke`](pkstroke-swift.struct.md), [`PKInkingTool`](pkinkingtool-swift.struct.md), and [`PKInk`](pkink-swift.struct.md) contain a [`requiredContentVersion`](pkink-swift.struct/requiredcontentversion.md) property that PencilKit populates automatically. The value of this property indicates which version of PencilKit is required to load the underlying data:

- [`PKContentVersion.version1`](pkcontentversion/version1.md) indicates that the data only contains inks introduced in iPadOS 14, and requires the device to run iPadOS 14 or later.
- [`PKContentVersion.version2`](pkcontentversion/version2.md) indicates that the data contains inks introduced in iPadOS 17, and requires the device to run iPadOS 17 or later.

Before you save these data model types, check their [`requiredContentVersion`](pkink-swift.struct/requiredcontentversion.md) to avoid syncing incompatible data to devices with earlier versions of the OS. For example, instead of syncing a [`PKDrawing`](pkdrawing-swift.struct.md) that features new inks, you can sync a fallback drawing and show a message that suggests updating the device’s OS to edit the latest drawing.

```swift
func updateDrawing(_ drawing: PKDrawing, at index: Int) {
    if #available(iOS 17.0, *) {
        // Before saving, check if this drawing uses new inks and requires a later
        // version of PencilKit than might be available on a person’s other devices.
        switch drawing.requiredContentVersion {
        case .version2:
            // This drawing is incompatible with the earlier version of PencilKit.
            // Sync a backward-compatible drawing to display on devices with earlier OS versions.
            dataModel.drawings[index] = fallbackDrawing
        default:
            // This drawing is compatible with the earlier version of PencilKit.
            // Sync the current drawing since there's no need to provide a 
            // backward-compatible drawing instead.
            dataModel.drawings[index] = drawing
        }
    } else {
        dataModel.drawings[index] = drawing
    }
    saveDataModel()
}
```

##### Limit Available Inks Using the Maximum Supported Content Version

If your app is unable to support backward compatibility for different versions of the OS, use the [`maximumSupportedContentVersion`](pktoolpicker/maximumsupportedcontentversion.md) property to limit which inks are available in your app. This limitation ensures that the data your app saves is compatible with the earlier version of PencilKit so you can load it on devices with earlier versions of the OS.

If you take this approach, you need to set [`maximumSupportedContentVersion`](pktoolpicker/maximumsupportedcontentversion.md) on both [`PKCanvasView`](pkcanvasview.md) and [`PKToolPicker`](pktoolpicker.md). For example, set this property to [`PKContentVersion.version1`](pkcontentversion/version1.md) to limit which kinds of edits the canvas views offers and which tools are available for a person to select when they create PencilKit content in your app.

```swift
// Set the maximum supported content version for the canvas view and any tool pickers.
@IBOutlet weak var canvasView: PKCanvasView!
var toolPicker = PKToolPicker()

// The canvas view limits the edits that a person can make so they’re compatible with the 
// the earlier version of PencilKit.
canvasView.maximumSupportedContentVersion = .version1

// The tool picker limits the tools that are available so they’re compatible with  
// the earlier version of PencilKit.
toolPicker.maximumSupportedContentVersion = .version1
```

> **Note**:  Session 10055: [`What’s new in UIKit`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10055/)

 Session 10055: [`What’s new in UIKit`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10055/)

## See Also

- [enum PKContentVersion](pkcontentversion.md)
  Constants that represent versions of PencilKit for backward compatibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/supporting-backward-compatibility-for-ink-types)*