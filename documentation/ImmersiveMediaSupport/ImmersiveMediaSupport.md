# Immersive Media Support

**Framework**: Immersive Media Support  
**Kind**: module

Read and write essential Apple Immersive Video metadata.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

#### Overview

Immersive Media Support enables you to create custom workflows for processing Apple Immersive Video (AIV). Use it to read and write AIV-specific metadata and enable previewing content in editorial workflows.

## Topics

### Essentials
- [Authoring Apple Immersive Video](authoring-apple-immersive-video.md)
  Prepare and package immersive video content for delivery.
### Camera metadata
- [actor VenueDescriptor](venuedescriptor.md)
  The Apple Immersive Media Venue Descriptor is a collection of static metadata necessary for every Apple Immersive Video.
- [struct ImmersiveCamera](immersivecamera.md)
  A structure that holds the required information for an immersive media camera to process and render video frames.
- [struct ImmersiveCameraCalibration](immersivecameracalibration.md)
  A structure that represents immersive media camera calibration data.
- [enum ImmersiveCameraMask](immersivecameramask.md)
  A structure that holds the camera mask type information and its relevant mask name.
- [struct ImmersiveDynamicMask](immersivedynamicmask.md)
  A type that holds the information required to dynamically generate an immersive media mask at load time.
### Presentation commands
- [enum PresentationCommand](presentationcommand.md)
  A set of properties that define the interface for a presentation command.
- [struct FadeCommand](fadecommand.md)
  A command type for color fading during immersive media playback.
- [struct FadeEnvironmentCommand](fadeenvironmentcommand.md)
  A command type for opacity fading environment backdrops during immersive media playback.
- [struct SetCameraCommand](setcameracommand.md)
  A command type for immersive camera switching during playback.
- [struct ShotFlopCommand](shotflopcommand.md)
  A command type to flip the video frames horizontally (mirrored horizontally) during playback for the duration of the command.
- [struct PresentationDescriptor](presentationdescriptor.md)
  A structure that represents dynamic metadata used during playback or when outputting the metadata track for an immersive video file.
- [class PresentationDescriptorReader](presentationdescriptorreader.md)
  An object that provides the functionality required to understand and process immersive presentation commands.
### Parametric immersive support
- [class ParametricImmersiveAssetInfo](parametricimmersiveassetinfo.md)
  An object that helps convert the original wide field of view video asset to parametric immersive asset.
### Immersive video rendering support
- [struct ImmersiveCameraViewModel](immersivecameraviewmodel.md)
  A view model that holds all the resources needed to render an immersive camera view.
- [struct ImmersiveVideoMask](immersivevideomask.md)
  A video mask to use during video rendering to smooth the edges of the mesh.
### Preview
- [class ImmersiveMediaPreviewMessagingProtocol](immersivemediapreviewmessagingprotocol.md)
  An object that represents the messaging protocol a remote preview sender and receiver use to communicate.
### Validation
- [struct AIVUValidator](aivuvalidator.md)
  A type to validate existing AIVU files to ensure that they meet the minimum requirements for AIV.
### Classes
- [class ImmersiveCameraMeshCalibration](immersivecamerameshcalibration.md)
  Calibration mesh geometry based on USDZ data.
- [class ImmersiveImageMask](immersiveimagemask.md)
  An object that holds all the information needed to load immersive media masks from image data or from a file.
- [class ImmersiveMediaRemotePreviewReceiver](immersivemediaremotepreviewreceiver.md)
  An observable object that helps apps handle receiving commands and data sent from an immersive media remote preview sender object.
- [class ImmersiveMediaRemotePreviewSender](immersivemediaremotepreviewsender.md)
  An observable object that helps an app send the required data to all connected receiver apps to help facilitate the complete preview of the immersive media playback.
### Structures
- [struct ImmersiveCameraLensDefinition](immersivecameralensdefinition.md)
  This type holds the ILPD lens configuration parameters to generate camera calibration type instance.
- [struct ImmersiveVideoFrame](immersivevideoframe.md)
  A type that represents an immersive video frame. An immersive video frame contains: - layout (SideBySide, OverUnder, Separate, Mono) - presentationTime: frame presentation time - pixelBuffers: an array with one or more images representing the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ImmersiveMediaSupport)*