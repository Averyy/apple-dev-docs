# finishContentEditing(completionHandler:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asks your extension for edited asset data to finish the editing session.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func finishContentEditing(completionHandler: @escaping (PHContentEditingOutput?) -> Void)
```

```swift
func finishContentEditing() async -> PHContentEditingOutput?
```

```objc
- (void) finishContentEditingWithCompletionHandler:(void (^)(PHContentEditingOutput *)) completionHandler;
```

## Discussion

Photos calls this method when the user chooses to end the editing session. Your extension view controller should:

1. Disable UI elements to prevent the user from editing further while you complete the remaining steps on a background queue.
2. Create a [`PHContentEditingOutput`](../../Photos/phcontenteditingoutput.md) object from the [`PHContentEditingInput`](../../Photos/phcontenteditinginput.md) object that Photos provided to your extension in the [`startContentEditing(with:placeholderImage:)`](./startcontentediting%28with,placeholderimage%29.md) method.

Use the content editing output to store the rendered photo or video data from the user’s edits and a [`PHAdjustmentData`](../../Photos/phadjustmentdata.md) object describing the edits.

> **Note**:  To end editing without committing changes to the asset, leave the content editing output’s [`adjustmentData`](../../Photos/phcontenteditingoutput/adjustmentdata.md) property set to `nil` and do not write to the location specified by its [`renderedContentURL`](../../Photos/phcontenteditingoutput/renderedcontenturl.md) property.

1. Call the `completionHandler` block with your content editing output, to notify Photos that the edit is complete.
2. After the `completionHandler` block finishes executing, you may safely clean up any data or files related to your edit.

## Parameters

- `completionHandler`: A block for your extension to call when you have finished editing.

  The block takes the following parameter:

  - **output**: The [`PHContentEditingOutput`](../../Photos/phcontenteditingoutput.md) object you created and populated before calling the completion handler.

## See Also

### Performing an Edit
- [func startContentEditing(with: PHContentEditingInput, placeholderImage: UIImage)](./startcontentediting%28with,placeholderimage%29.md)
  Tells your extension that asset data is available for editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phcontenteditingcontroller/finishcontentediting(completionhandler:))*