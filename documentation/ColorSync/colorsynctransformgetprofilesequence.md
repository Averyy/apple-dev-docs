# ColorSyncTransformGetProfileSequence(_:)

**Framework**: ColorSync  
**Kind**: func

Returns the profile sequence used to create a color transform.

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
func ColorSyncTransformGetProfileSequence(_ transform: ColorSyncTransform!) -> Unmanaged<CFArray>?
```

## Parameters

- `transform`: The transform from which to get the profile sequence used to create the transform.

## See Also

- [func ColorSyncTransformCreate(CFArray?, CFDictionary?) -> Unmanaged<ColorSyncTransform>?](colorsynctransformcreate(_:_:).md)
  Creates a color transform from a sequence of profiles.
- [func ColorSyncTransformConvert(ColorSyncTransform!, Int, Int, UnsafeMutableRawPointer!, ColorSyncDataDepth, ColorSyncDataLayout, Int, UnsafeRawPointer!, ColorSyncDataDepth, ColorSyncDataLayout, Int, CFDictionary?) -> Bool](colorsynctransformconvert(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Converts color data from a source layout to a destination layout using a color transform.
- [func ColorSyncTransformCopyProperty(ColorSyncTransform!, CFTypeRef!, CFDictionary?) -> Unmanaged<CFTypeRef>?](colorsynctransformcopyproperty(_:_:_:).md)
  Copies a property from a color transform.
- [func ColorSyncTransformSetProperty(ColorSyncTransform!, CFTypeRef!, CFTypeRef?)](colorsynctransformsetproperty(_:_:_:).md)
  Sets a property on a color transform.
- [func ColorSyncTransformGetTypeID() -> CFTypeID](colorsynctransformgettypeid().md)
  Returns the type identifier for the `ColorSyncTransform` opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsynctransformgetprofilesequence(_:))*