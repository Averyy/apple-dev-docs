# init(placeholderForCreatedAsset:)

**Framework**: Photos  
**Kind**: init  
**Role**: Initializer

Creates an editing output for use in adding a new asset to the photo library.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(placeholderForCreatedAsset: PHObjectPlaceholder)
```

```objc
- (instancetype) initWithPlaceholderForCreatedAsset:(PHObjectPlaceholder *) placeholderForCreatedAsset;
```

#### Return Value

An initialized content editing output.

#### Discussion

Use this method to add a new asset to the Photos library with edited content, as opposed to editing the content of an asset after adding it to the library. For example, you might use this option if your app applies filters to photos it captures with the device camera — instead of saving only the filtered image to the Photos library, your app can save both the filtered and the original image, allowing the user to revert to the original image or apply different filters later. The code below illustrates such a workflow.

**Swift**:

```swift
PHPhotoLibrary.shared().performChanges {
    
    // Make a change request for adding an asset.
    let changeRequest = PHAssetChangeRequest.creationRequestForAssetFromImage(atFileURL: originalJPEGFileURL)
    
    // Make a content editing output for use with the change request.
    let placeholder = changeRequest!.placeholderForCreatedAsset
    let contentEditingOutput = PHContentEditingOutput(placeholderForCreatedAsset: placeholder!)
    
    // Apply content adjustments to the newly created asset.
    contentEditingOutput.adjustmentData = adjustmentData
    try! adjustedJPEGData.write(to: contentEditingOutput.renderedContentURL)
    changeRequest!.contentEditingOutput = contentEditingOutput
    
} completionHandler: { success, error in
    if !success {
        print("Can't create asset: \(String(describing: error))")
    }
}
```

**Objective-C**:

```objc
[[PHPhotoLibrary sharedPhotoLibrary] performChanges:^{
 
    // Make a change request for adding an asset.
    PHAssetChangeRequest *changeRequest =
        [PHAssetChangeRequest creationRequestForAssetFromImageAtFileURL:originalJPEGFileURL];
 
    // Make a content editing output for use with the change request.
    PHObjectPlaceholder *placeholder = changeRequest.placeholderForCreatedAsset;
    PHContentEditingOutput *contentEditingOutput =
        [[PHContentEditingOutput alloc] initWithPlaceholderForCreatedAsset:placeholder];
 
    // Apply content adjustments to the newly created asset.
    contentEditingOutput.adjustmentData = adjustmentData;
    [adjustedJPEGData writeToURL:contentEditingOutput.renderedContentURL atomically:YES];
    changeRequest.contentEditingOutput = contentEditingOutput;
 
} completionHandler:^(BOOL success, NSError *error) {
    if (!success) NSLog(@"Can't create asset: %@", error);
}];
```

In this example, the app first uses a [`PHAssetChangeRequest`](../phassetchangerequest.md) object to request creation of a new asset with the unedited image captured from the camera (`originalJPEGFileURL`). Then, it creates a [`PHContentEditingOutput`](../phcontenteditingoutput.md) object with the [`placeholderForCreatedAsset`](../phassetchangerequest/placeholderforcreatedasset.md) object provided by the change request. Finally, it provides filtered image data (`adjustedJPEGData`) and adjustment data describing the filters (`adjustmentData`) to the editing output and adds the editing output to the change request.

> **Note**:  If your app edits the contents of assets already in the Photos library — including assets your app has itself recently added — Photos prompts the user for permission to change the asset’s content. If instead your app uses the [`init(placeholderForCreatedAsset:)`](./init%28placeholderforcreatedasset%29.md) method to create an asset with edited content, Photos recognizes your app’s ownership of the content and therefore doesn’t need to prompt the user for permission to edit it.

## Parameters

- `placeholderForCreatedAsset`: A placeholder object that ties the editing output to a [`PHAssetChangeRequest`](../phassetchangerequest.md) object for creating a new asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcontenteditingoutput/init(placeholderforcreatedasset:))*