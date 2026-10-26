# setProjectPreviewImage(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Updates the project preview in Photos.

**Availability**:
- macOS 10.14+

## Declaration

```swift
func setProjectPreviewImage(_ previewImage: NSImage)
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (void) setProjectPreviewImage:(UIImage *) previewImage;
```

*macOS*

```objc
- (void) setProjectPreviewImage:(NSImage *) previewImage;
```

#### Discussion

PhotoKit requires that you set a project preview in the following situations:

- Whenever the project changes in a way that requires a new preview.
- During or after execution of the [`beginProject(with:projectInfo:completion:)`](../../PhotosUI/phprojectextensioncontroller/beginproject%28with,projectinfo,completion%29.md) protocol method.
- During or after execution of the [`resumeProject(with:completion:)`](../../PhotosUI/phprojectextensioncontroller/resumeproject%28with,completion%29.md) protocol method.

## Parameters

- `previewImage`: A rendered project preview with dimensions of 1024 x 1024.

## See Also

### Responding to Change Requests
- [func setKeyAsset(PHAsset?)](./setkeyasset%28_%29.md)
  Sets the key asset representing the project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phprojectchangerequest/setprojectpreviewimage(_:))*