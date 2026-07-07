# LockedCameraCaptureExtension

**Framework**: LockedCameraCapture  
**Kind**: protocol

A protocol that creates a locked camera capture extension.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
@MainActor
protocol LockedCameraCaptureExtension : AppExtension
```

## Topics

### Associated Types
- [associatedtype Body : LockedCameraCaptureExtensionScene](lockedcameracaptureextension/body-swift.associatedtype.md)
### Instance Properties
- [var body: Self.Body](lockedcameracaptureextension/body-swift.property.md)
  The content for the locked camera capture extension.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)

## See Also

- [protocol LockedCameraCaptureExtensionScene](lockedcameracaptureextensionscene.md)
  A protocol that provides the UI for the locked camera capture extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lockedcameracapture/lockedcameracaptureextension)*