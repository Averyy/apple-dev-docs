# Working with content from your Mac app using Spatial Preview

**Framework**: Spatial Preview

Send and update documents, and work with 3D content live from your macOS app to a visionOS device through the Spatial Preview framework.

**Availability**:
- macOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

#### Overview

The Spatial Preview framework lets Mac apps send content to a nearby Apple Vision Pro so people can view it spatially and immersively. This sample includes two examples that illustrate the main session types:

- **`DocumentPreviewSession`**: A spatial photo gallery example that streams stereo HEIC images to Apple Vision Pro so people can browse spatial photos immersively without leaving the Mac workflow.
- **`USDPreviewSession`**: A 3D interior design example that uses USD to adjust furniture layouts live with override layers, and an asset-review workflow that uses text annotations.

> **Note**: This sample code project is associated with WWDC26 session 282: [`Discover the Spatial Preview framework`](https://developer.apple.comhttps://developer.apple.com/wwdc26/282/)

## See Also

- [Bridging an external USD runtime to Spatial Preview](bridging-an-external-usd-runtime-to-spatial-preview.md)
  Sync edits between an app with its own OpenUSD runtime and a Spatial Preview session using a shared layer as the exchange mechanism.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/working-with-content-from-your-mac-app-using-spatial-preview)*