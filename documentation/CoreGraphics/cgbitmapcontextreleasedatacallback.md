# CGBitmapContextReleaseDataCallback

**Framework**: Core Graphics  
**Kind**: typealias

A callback function used to release data associate with the bitmap context.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias CGBitmapContextReleaseDataCallback = (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

The `releaseInfo` parameter contains the contextual data that you passed to the [`init(data:width:height:bitsPerComponent:bytesPerRow:space:bitmapInfo:releaseCallback:releaseInfo:)`](cgcontext/init(data:width:height:bitspercomponent:bytesperrow:space:bitmapinfo:releasecallback:releaseinfo:).md) function. The `data` parameter contains a pointer to the bitmap data for you to release.

## See Also

- [init?(data: UnsafeMutableRawPointer?, width: Int, height: Int, bitsPerComponent: Int, bytesPerRow: Int, space: CGColorSpace, bitmapInfo: UInt32)](cgcontext/init(data:width:height:bitspercomponent:bytesperrow:space:bitmapinfo:).md)
  Creates a bitmap graphics context.
- [init?(data: UnsafeMutableRawPointer?, width: Int, height: Int, bitsPerComponent: Int, bytesPerRow: Int, space: CGColorSpace, bitmapInfo: UInt32, releaseCallback: CGBitmapContextReleaseDataCallback?, releaseInfo: UnsafeMutableRawPointer?)](cgcontext/init(data:width:height:bitspercomponent:bytesperrow:space:bitmapinfo:releasecallback:releaseinfo:).md)
  Creates a bitmap graphics context with the specified callback function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgbitmapcontextreleasedatacallback)*