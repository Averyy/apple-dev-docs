# withUnsafeBackingIOSurfaceIfPresent(_:)

**Framework**: Core Video  
**Kind**: method

Access the IOSurface backing the pixel buffer if present.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func withUnsafeBackingIOSurfaceIfPresent<R>(_ block: (IOSurface) throws -> sending R) rethrows -> sending R?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferrepresentable/withunsafebackingiosurfaceifpresent(_:))*