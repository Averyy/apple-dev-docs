# generate()

**Framework**: RealityKit  
**Kind**: method

Creates a 3D representation of the image if one does not already exist.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
func generate() async throws
```

#### Discussion

This method checks for cancellation of an enclosing `Task` during generation, and cancels its own async generation early (by throwing an error) if task cancellation is detected.

> **Note**: Throws an error if the underlying monoscopic image does not contain valid data to generate a spatial 3D representation; or if a spatial 3D representation has already been generated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagepresentationcomponent/spatial3dimage/generate())*