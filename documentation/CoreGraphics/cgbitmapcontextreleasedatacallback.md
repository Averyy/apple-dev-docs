# CGBitmapContextReleaseDataCallback

**Framework**: Core Graphics  
**Kind**: typealias  
**Role**: Type Alias

A callback function used to release data associate with the bitmap context.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias CGBitmapContextReleaseDataCallback = (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*)(void *, void *) CGBitmapContextReleaseDataCallback;
```

## Discussion

The `releaseInfo` parameter contains the contextual data that you passed to the [`init(data:width:height:bitsPerComponent:bytesPerRow:space:bitmapInfo:releaseCallback:releaseInfo:)`](./cgcontext/init%28data,width,height,bitspercomponent,bytesperrow,space,bitmapinfo,releasecallback,releaseinfo%29-4yzt5.md) function. The `data` parameter contains a pointer to the bitmap data for you to release.

## See Also

### Creating Bitmap Graphics Contexts
- [init?(data: UnsafeMutableRawPointer?, width: Int, height: Int, bitsPerComponent: Int, bytesPerRow: Int, space: CGColorSpace?, bitmapInfo: CGBitmapInfo)](./cgcontext/init%28data,width,height,bitspercomponent,bytesperrow,space,bitmapinfo%29-10b3i.md)
  Creates a bitmap graphics context.
- [init?(data: UnsafeMutableRawPointer?, width: Int, height: Int, bitsPerComponent: Int, bytesPerRow: Int, space: CGColorSpace?, bitmapInfo: CGBitmapInfo, releaseCallback: CGBitmapContextReleaseDataCallback?, releaseInfo: UnsafeMutableRawPointer?)](./cgcontext/init%28data,width,height,bitspercomponent,bytesperrow,space,bitmapinfo,releasecallback,releaseinfo%29-4yzt5.md)
  Creates a bitmap graphics context with the specified callback function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgbitmapcontextreleasedatacallback)*