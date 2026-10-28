# PreviewPlatform

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

Platforms that can run the preview.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.0+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.0
- tvOS 13.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

> **Deprecated**: Use [`Preview(_:body:)`](./preview%28_,body%29.md) instead.

## Declaration

```swift
enum PreviewPlatform
```

## Overview

Xcode infers the platform for a preview based on the currently selected target. If you have a multiplatform target and want to suggest a particular target for a preview, implement the [`platform`](./previewprovider/platform.md) computed property as a hint, and specify one of the preview platforms:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
    }

    static var platform: PreviewPlatform? {
        PreviewPlatform.tvOS
    }
}
```

## Topics

### Getting an operating system
- [PreviewPlatform.iOS](./previewplatform/ios.md)
  Specifies iOS as the preview platform.
- [PreviewPlatform.macOS](./previewplatform/macos.md)
  Specifies macOS as the preview platform.
- [PreviewPlatform.tvOS](./previewplatform/tvos.md)
  Specifies tvOS as the preview platform.
- [PreviewPlatform.watchOS](./previewplatform/watchos.md)
  Specifies watchOS as the preview platform.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Defining a preview
- [protocol PreviewProvider](./previewprovider.md)
  A type that produces view previews in Xcode.
- [func previewDisplayName(String?) -> some View](./view/previewdisplayname%28_%29.md)
  Sets a user visible name to show in the canvas for a preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/previewplatform)*