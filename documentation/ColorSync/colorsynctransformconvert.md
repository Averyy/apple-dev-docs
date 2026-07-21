# ColorSyncTransformConvert(_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: ColorSync  
**Kind**: func

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func ColorSyncTransformConvert(_ transform: ColorSyncTransform!, _ width: Int, _ height: Int, _ dst: UnsafeMutableRawPointer!, _ dstDepth: ColorSyncDataDepth, _ dstLayout: ColorSyncDataLayout, _ dstBytesPerRow: Int, _ src: UnsafeRawPointer!, _ srcDepth: ColorSyncDataDepth, _ srcLayout: ColorSyncDataLayout, _ srcBytesPerRow: Int, _ options: CFDictionary?) -> Bool
```

## See Also

- [func ColorSyncTransformCreate(CFArray?, CFDictionary?) -> Unmanaged<ColorSyncTransform>?](colorsynctransformcreate(_:_:).md)
- [func ColorSyncTransformGetProfileSequence(ColorSyncTransform!) -> Unmanaged<CFArray>?](colorsynctransformgetprofilesequence(_:).md)
- [func ColorSyncTransformCopyProperty(ColorSyncTransform!, CFTypeRef!, CFDictionary?) -> Unmanaged<CFTypeRef>?](colorsynctransformcopyproperty(_:_:_:).md)
- [func ColorSyncTransformSetProperty(ColorSyncTransform!, CFTypeRef!, CFTypeRef?)](colorsynctransformsetproperty(_:_:_:).md)
- [func ColorSyncTransformGetTypeID() -> CFTypeID](colorsynctransformgettypeid().md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsynctransformconvert(_:_:_:_:_:_:_:_:_:_:_:_:))*