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

The `releaseInfo` parameter contains the contextual data that you passed to the `CGContext/init(data:width:height:bitsPerComponent:bytesPerRow:space:bitmapInfo:releaseCallback:releaseInfo:)` function. The `data` parameter contains a pointer to the bitmap data for you to release.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgbitmapcontextreleasedatacallback)*