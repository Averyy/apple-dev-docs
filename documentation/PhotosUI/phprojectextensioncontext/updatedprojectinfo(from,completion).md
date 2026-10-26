# updatedProjectInfo(from:completion:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method

Creates an updated [`PHProjectInfo`](../phprojectinfo.md) instance from existing project information and current assets.

**Availability**:
- macOS 10.14+

## Declaration

```swift
func updatedProjectInfo(from existingProjectInfo: PHProjectInfo?, completion: @escaping (PHProjectInfo?) -> Void) -> Progress
```

```objc
- (NSProgress *) updatedProjectInfoFromProjectInfo:(PHProjectInfo *) existingProjectInfo completion:(void (^)(PHProjectInfo *updatedProjectInfo)) completion;
```

## Parameters

- `existingProjectInfo`: The project information to update. If this is not `nil`, a new [`PHProjectInfo`](../phprojectinfo.md) instance is created from all assets in the [`PHProject`](https://developer.apple.com/documentation/photos/phproject).
- `completion`: A closure with code you provide that runs on completion.

## See Also

### Updating Assets
- [func showEditor(for: PHAsset)](./showeditor%28for%29.md)
  Invokes the built-in photo editor for the given asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectextensioncontext/updatedprojectinfo(from:completion:))*