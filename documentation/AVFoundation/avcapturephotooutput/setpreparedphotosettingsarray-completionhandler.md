# setPreparedPhotoSettingsArray(_:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Tells the photo capture output to prepare resources for future capture requests with the specified settings.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
func setPreparedPhotoSettingsArray(_ preparedPhotoSettingsArray: [AVCapturePhotoSettings]) async throws
```

#### Discussion

Some types of photo capture, such as bracketed captures and RAW captures, require the photo output to allocate additional buffers or prepare other resources. To prevent photo capture requests from executing slowly due to lazy resource allocation, you may call this method with an array of settings objects representative of the types of capture you will be performing (such as settings for a bracketed capture, RAW capture, or capture with still image stabilization).

By default, the photo output prepares sufficient resources to capture photos with default settings (as defined by the [`AVCapturePhotoSettings`](avcapturephotosettings.md) default initializer). To reclaim all possible resources, call this method with an empty array.

Each time you call this method with an array of settings, the photo output evaluates what additional resources it needs to allocate, as well as existing resources that can be reclaimed, and calls your `completionHandler` block when it has finished preparing (and possibly reclaiming) needed resources. To provide an early hint as to which capture features you intend to use, you can call this method even before calling the [`startRunning()`](avcapturesession/startrunning().md) method on your capture session.

Preparation for photo capture is always optional. You may call the [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method without first calling this method—however, some of your photo captures may execute slowly as the capture system allocates additional resources on a just-in-time basis.

If you call this method while your capture session is not running, your `completionHandler` block is not immediately called. The photo output calls your completion handler only after you’ve called the [`startRunning()`](avcapturesession/startrunning().md) method on your capture session and the needed resources have actually been prepared. If you call the [`setPreparedPhotoSettingsArray(_:completionHandler:)`](avcapturephotooutput/setpreparedphotosettingsarray(_:completionhandler:).md) method with an array of settings, and then call it a second time, the first call’s completion handler fires immediately with a `prepared` argument of [`false`](https://developer.apple.com/documentation/swift/false).

Prepared settings persist across session starts/stops and committed configuration changes and participate in the deferred work behavior defined by the [`AVCaptureSession`](avcapturesession.md) class. That is, if you call your capture session’s [`beginConfiguration()`](avcapturesession/beginconfiguration().md) method, change your session’s input/output topology, and then call this method, the capture session defers any preparation work until you call the [`commitConfiguration()`](avcapturesession/commitconfiguration().md) method. This pattern lets you atomically commit a new configuration as well as prepare to take photos in that new configuration.

After you call this method and your `completionHandler` block has fired, the [`preparedPhotoSettingsArray`](avcapturephotooutput/preparedphotosettingsarray.md) property lists the photo settings for which the capture system has prepared resources.

## Parameters

- `preparedPhotoSettingsArray`: An array of photo capture settings objects indicating the types of capture for which the photo output should prepare resources.
- `completionHandler`: A completion block to be called on a serial dispatch queue after the photo output has finished preparing resources. Pass   if you do not wish to be notified when preparation is complete.

## See Also

- [var preparedPhotoSettingsArray: [AVCapturePhotoSettings]](avcapturephotooutput/preparedphotosettingsarray.md)
  An array of photo settings for which the photo output has prepared capture resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/setpreparedphotosettingsarray(_:completionhandler:))*