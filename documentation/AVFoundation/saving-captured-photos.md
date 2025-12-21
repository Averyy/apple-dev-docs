# Saving captured photos

**Framework**: AVFoundation

Add an image and other data from a photo capture to the photo library.

#### Overview

When you complete a photo capture with [`AVCapturePhotoOutput`](avcapturephotooutput.md), you receive an [`AVCapturePhoto`](avcapturephoto.md) object that contains the image data, camera metadata, and any auxiliary images you requested, such as thumbnails or depth maps. You can retrieve this data individually from the [`AVCapturePhoto`](avcapturephoto.md) object. Or you can call its [`fileDataRepresentation()`](avcapturephoto/filedatarepresentation().md) method to get a [`Data`](https://developer.apple.com/documentation/Foundation/Data) object that’s ready to save using the codec and file format you requested for that photo in [`AVCapturePhotoSettings`](avcapturephotosettings.md).

After capturing a photo, use [`PhotoKit`](https://developer.apple.com/documentation/PhotoKit) to add that data to the user’s photo library.

> **Note**:  If your app only needs to access content in the photo library, you can use the [`PhotoKit`](https://developer.apple.com/documentation/PhotoKit) Photos picker instead, which doesn’t require you to request access from the user. To learn more, see [`Selecting Photos and Videos in iOS`](https://developer.apple.com/documentation/PhotoKit/selecting-photos-and-videos-in-ios).

##### Configure Properties and Capabilities for Your App Targets

You can use [`PhotoKit`](https://developer.apple.com/documentation/PhotoKit) to enable read/write access to the user’s photo library. To do so, provide a static message for the [`NSPhotoLibraryUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSPhotoLibraryUsageDescription) key in the `Info.plist` file to display to the user when your app requests access.

![A screenshot showing the photo library usage description in the Info tab of the app target. The highlighted string for Privacy Photo Library Usage Description reads This app accesses and saves media in your photo library. ](https://docs-assets.developer.apple.com/published/a6550471cb61ada376e926faac3b17a4/media-4132909%402x.png)

In macOS, you also need to enable the [`Photos Library Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.personal-information.photos-library) in the Signing & Capabilities tab for your app targets.

![A screenshot showing the macOS Photos Library entitlement enabled in the Signing & Capabilities tab of the app target.](https://docs-assets.developer.apple.com/published/1e8a0e60993966540c623b4f28eb1d8a/media-4132908%402x.png)

> ❗ **Important**:  Your app needs to contain the appropriate key in its `Info.plist` file, and the appropriate entitlement enabled in macOS, before it requests authorization or attempts to use a device. Otherwise, the system terminates your app.

##### Request Permission to Access the Users Photo Library

Use the [`PHPhotoLibrary`](https://developer.apple.com/documentation/Photos/PHPhotoLibrary) [`requestAuthorization(for:handler:)`](https://developer.apple.com/documentation/Photos/PHPhotoLibrary/requestAuthorization(for:handler:)) to request access to the photo library at an appropriate time, such as when the user first opens your app’s camera feature. Here’s an example:

```swift
var isPhotoLibraryReadWriteAccessGranted: Bool {
    get async {
        let status = PHPhotoLibrary.authorizationStatus(for: .readWrite)
        
        // Determine if the user previously authorized read/write access.
        var isAuthorized = status == .authorized
        
        // If the system hasn't determined the user's authorization status,
        // explicitly prompt them for approval.
        if status == .notDetermined {
            isAuthorized = await PHPhotoLibrary.requestAuthorization(for: .readWrite) == .authorized
        }
        
        return isAuthorized
    }
}
```

> **Note**:  Don’t wait to request access to the photo library until after the user takes their first photo because the permission alert prevents their ability to take multiple photos.

##### Use a Creation Request to Add a Photo Asset

Perform these steps to receive a captured photo and save it to the photo library:

1. Adopt the [`AVCapturePhotoCaptureDelegate`](avcapturephotocapturedelegate.md) protocol and implement its [`photoOutput(_:didFinishProcessingPhoto:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:error:).md) method to receive a callback for each photo delivered in a capture request.
2. Call [`fileDataRepresentation()`](avcapturephoto/filedatarepresentation().md) on the [`AVCapturePhoto`](avcapturephoto.md) object provided by the protocol method to receive a data object containing the photo image data and its attachments, such as camera metadata and auxilliary images.
3. Create a [`PHAssetCreationRequest`](https://developer.apple.com/documentation/Photos/PHAssetCreationRequest) to add the photo resource.

The following code provides an example of this workflow:

```swift
func photoOutput(_ output: AVCapturePhotoOutput, didFinishProcessingPhoto photo: AVCapturePhoto, error: Error?) {
    if let error {
        print("Error processing photo: \(error.localizedDescription)")
        return
    }
    
    Task {
        await save(photo: photo)
    }
}

func save(photo: AVCapturePhoto) async {
    // Confirm the user granted read/write access.
    guard await isPhotoLibraryReadWriteAccessGranted else { return }
    
    // Create a data representation of the photo and its attachments.
    if let photoData = photo.fileDataRepresentation() {
        PHPhotoLibrary.shared().performChanges {
            // Save the photo data.
            let creationRequest = PHAssetCreationRequest.forAsset()
            creationRequest.addResource(with: .photo, data: photoData, options: nil)
        } completionHandler: { success, error in
            if let error {
                print("Error saving photo: \(error.localizedDescription)")
                return
            }
        }
    }
}
```

## See Also

- [Tracking photo capture progress](tracking-photo-capture-progress.md)
  Monitor key events during capture to provide feedback in your camera UI.
- [Capturing and saving Live Photos](capturing-and-saving-live-photos.md)
  Capture Live Photos like those created in the system Camera app and save them to the Photos library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/saving-captured-photos)*