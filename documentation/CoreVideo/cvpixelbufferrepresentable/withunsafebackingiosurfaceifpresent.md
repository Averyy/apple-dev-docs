# withUnsafeBackingIOSurfaceIfPresent(_:)

**Framework**: Core Video  
**Kind**: method

Access the IOSurface backing the pixel buffer if present.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func withUnsafeBackingIOSurfaceIfPresent<R>(_ block: (IOSurface) throws -> sending R) rethrows -> sending R?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferrepresentable/withunsafebackingiosurfaceifpresent(_:))*