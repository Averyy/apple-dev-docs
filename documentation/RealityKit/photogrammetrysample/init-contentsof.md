# init(contentsOf:)

**Framework**: RealityKit  
**Kind**: init

Asynchronously loads the image file located at URL into a `PhotogrammetrySample` with as many data fields populated as can be found in the target file.  HEIC images captured with the `ObjectCaptureSession` will contain more advanced data fields beyond just the image.  Which properties are populated depends on how the images were captured. The `id` of the sample will be automatically created to be unique to the current process. Throws:  If `url` does not point to a file URL or there is a problem  loading `url`.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
init(contentsOf url: URL) async throws
```

#### Discussion

This function is useful for making a capture image inspector or other system that needs to operate in an asynchronous context, such as operating within the main actor.

For example:

```None
func loadDepthData(contentsOf url: URL) async -> CVPixelBuffer? {
   return try? await PhotogrammetrySample(contentsOf: url).depthDataMap
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysample/init(contentsof:))*