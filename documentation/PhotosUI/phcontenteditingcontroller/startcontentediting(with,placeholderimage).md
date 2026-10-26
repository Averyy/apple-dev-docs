# startContentEditing(with:placeholderImage:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells your extension that asset data is available for editing.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- macOS 10.11+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
func startContentEditing(with contentEditingInput: PHContentEditingInput, placeholderImage: UIImage)
```

*macOS*

```swift
func startContentEditing(with contentEditingInput: PHContentEditingInput, placeholderImage: NSImage)
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
- (void) startContentEditingWithInput:(PHContentEditingInput *) contentEditingInput placeholderImage:(UIImage *) placeholderImage;
```

*macOS*

```objc
- (void) startContentEditingWithInput:(PHContentEditingInput *) contentEditingInput placeholderImage:(NSImage *) placeholderImage;
```

#### Discussion

Photos calls this method before your extension view controller’s view appears.

For a photo asset, use the [`displaySizeImage`](../../Photos/phcontenteditinginput/displaysizeimage.md) property of the provided [`PHContentEditingInput`](../../Photos/phcontenteditinginput.md) object to perform editing in your extension’s UI. If your extension returned `true` from the [`canHandle(_:)`](./canhandle%28_%29.md) method, this image represents the previous version of the asset—you need to use the [`adjustmentData`](../../Photos/phcontenteditinginput/adjustmentdata.md) object to reconstruct the last edit made to the asset. Because asynchronously rendering the results of the previous edit may take some time, you can display the `placeholderImage` until your extension is ready to begin editing.

You don’t need to use the content editing input’s [`fullSizeImageURL`](../../Photos/phcontenteditinginput/fullsizeimageurl.md) property until the user has finished editing and you need to render final output.

For a video asset, use the [`PHContentEditingInput`](../../Photos/phcontenteditinginput.md) object to retrieve AVFoundation objects for editing audio and video content.

## Parameters

- `contentEditingInput`: An object that describes the asset to be edited.
- `placeholderImage`: An image representing the current state of the asset suitable for temporarily displaying in your extension’s UI.

## See Also

### Performing an Edit
- [func finishContentEditing(completionHandler: (PHContentEditingOutput?) -> Void)](./finishcontentediting%28completionhandler%29.md)
  Asks your extension for edited asset data to finish the editing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phcontenteditingcontroller/startcontentediting(with:placeholderimage:))*