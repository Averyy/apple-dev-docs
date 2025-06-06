# Additional data capture

**Framework**: AVFoundation

Capture additional data including depth and metadata, and synchronize capture from multiple outputs.

## Topics

### Depth data capture
- [Capturing Photos with Depth](capturing-photos-with-depth.md)
  Get a depth map with a photo to create effects like the system camera’s Portrait mode (on compatible devices).
- [Creating Auxiliary Depth Data Manually](creating-auxiliary-depth-data-manually.md)
  Generate a depth image and attach it to your own image.
- [Capturing depth using the LiDAR camera](capturing-depth-using-the-lidar-camera.md)
  Access the LiDAR camera on supporting devices to capture precise depth data.
- [AVCamFilter: Applying Filters to a Capture Stream](avcamfilter-applying-filters-to-a-capture-stream.md)
  Render a capture stream with rose-colored filtering and depth effects.
- [Streaming Depth Data from the TrueDepth Camera](streaming-depth-data-from-the-truedepth-camera.md)
  Visualize depth data in 2D and 3D from the TrueDepth camera.
- [Enhancing Live Video by Leveraging TrueDepth Camera Data](enhancing-live-video-by-leveraging-truedepth-camera-data.md)
  Apply your own background to a live capture feed streamed from the front-facing TrueDepth camera.
- [class AVCaptureDepthDataOutput](avcapturedepthdataoutput.md)
  A capture output that records scene depth information on compatible camera devices.
- [class AVDepthData](avdepthdata.md)
  A container for per-pixel distance or disparity information captured by compatible camera devices.
- [class AVCameraCalibrationData](avcameracalibrationdata.md)
  Information about the camera characteristics used to capture images and depth data.
### Metadata capture
- [class AVCaptureMetadataInput](avcapturemetadatainput.md)
  A capture input for providing timed metadata to a capture session.
- [class AVCaptureMetadataOutput](avcapturemetadataoutput.md)
  A capture output for processing timed metadata produced by a capture session.
- [class AVMetadataObject](avmetadataobject.md)
  The abstract superclass for objects provided by a metadata capture output.
- [Metadata Types](metadata-types.md)
  Inspect the supported metadata object types that the framework supports.
### Synchronized capture
- [class AVCaptureDataOutputSynchronizer](avcapturedataoutputsynchronizer.md)
  An object that coordinates time-matched delivery of data from multiple capture outputs.
- [class AVCaptureSynchronizedDataCollection](avcapturesynchronizeddatacollection.md)
  A set of data samples collected simultaneously from multiple capture outputs.
- [class AVCaptureSynchronizedSampleBufferData](avcapturesynchronizedsamplebufferdata.md)
  A container for video or audio samples collected using synchronized capture.
- [class AVCaptureSynchronizedMetadataObjectData](avcapturesynchronizedmetadataobjectdata.md)
  A container for metadata objects collected using synchronized capture.
- [class AVCaptureSynchronizedDepthData](avcapturesynchronizeddepthdata.md)
  A container for scene depth information collected using synchronized capture.
- [class AVCaptureSynchronizedData](avcapturesynchronizeddata.md)
  The abstract superclass for media samples collected using synchronized capture.

## See Also

- [Capture setup](capture-setup.md)
  Configure built-in cameras and microphones, and external capture devices, for media capture.
- [Photo capture](photo-capture.md)
  Capture high-quality still images, Live Photos, and supporting photo data.
- [Audio and video capture](audio-and-video-capture.md)
  Capture audio and video directly to media files, or capture streams of media for direct access to media sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/additional-data-capture)*