# setKeyAsset(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Sets the key asset representing the project.

**Availability**:
- macOS 10.13+ - Deprecated in 10.14

## Declaration

```swift
func setKeyAsset(_ keyAsset: PHAsset?)
```

```objc
- (void) setKeyAsset:(PHAsset *) keyAsset;
```

## Discussion

> **Note**:  Setting a key asset has been deprecated in macOS 10.14. Use [`setProjectPreviewImage(_:)`](./setprojectpreviewimage%28_%29.md) to provide a rendered preview image instead of designating a key asset.

## See Also

### Responding to Change Requests
- [func setProjectPreviewImage(NSImage)](./setprojectpreviewimage%28_%29.md)
  Updates the project preview in Photos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phprojectchangerequest/setkeyasset(_:))*