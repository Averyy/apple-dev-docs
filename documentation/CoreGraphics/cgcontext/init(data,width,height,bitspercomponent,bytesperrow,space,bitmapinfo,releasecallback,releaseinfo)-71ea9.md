# init(data:width:height:bitsPerComponent:bytesPerRow:space:bitmapInfo:releaseCallback:releaseInfo:)

**Framework**: Core Graphics  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 4.0+ - Deprecated in 27.3
- iPadOS 4.0+ - Deprecated in 27.3
- Mac Catalyst 13.1+ - Deprecated in 27.3
- macOS 10.6+ - Deprecated in 27.3
- tvOS - Deprecated in 27.3
- visionOS 1.0+ - Deprecated in 27.3
- watchOS 2.0+ - Deprecated in 27.3

> **Deprecated**: update space parameter to CGColorSpace?, bitmapInfo parameter to CGBitmapInfo

## Declaration

```swift
init?(data: UnsafeMutableRawPointer?, width: Int, height: Int, bitsPerComponent: Int, bytesPerRow: Int, space: CGColorSpace, bitmapInfo: UInt32, releaseCallback: CGBitmapContextReleaseDataCallback?, releaseInfo: UnsafeMutableRawPointer?)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/init(data:width:height:bitspercomponent:bytesperrow:space:bitmapinfo:releasecallback:releaseinfo:)-71ea9)*