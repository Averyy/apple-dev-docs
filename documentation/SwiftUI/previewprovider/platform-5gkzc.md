# platform

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The platform to run the provider on.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.0+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.0
- tvOS 13.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

> **Deprecated**: Use #Preview instead.

## Declaration

```swift
@MainActor
@preconcurrency static var platform: PreviewPlatform? { get }
```

#### Discussion

This default implementation of the [`platform`](./platform.md) computed property returns `nil`. Rely on this implementation unless you have a multiplatform target and want to suggest a particular platform for a preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/previewprovider/platform-5gkzc)*