# ColorSyncTransformGetTypeID()

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

Returns the type identifier for the `ColorSyncTransform` opaque type.

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
func ColorSyncTransformGetTypeID() -> CFTypeID
```

```c
extern CFTypeID ColorSyncTransformGetTypeID();
```

## Return Value

The `CFTypeID` for `ColorSyncTransform` objects.

## See Also

### Creating and applying a transform
- [func ColorSyncTransformCreate(CFArray?, CFDictionary?) -> Unmanaged<ColorSyncTransform>?](./colorsynctransformcreate%28_,_%29.md)
  Creates a color transform from a sequence of profiles.
- [func ColorSyncTransformConvert(ColorSyncTransform!, Int, Int, UnsafeMutableRawPointer!, ColorSyncDataDepth, ColorSyncDataLayout, Int, UnsafeRawPointer!, ColorSyncDataDepth, ColorSyncDataLayout, Int, CFDictionary?) -> Bool](./colorsynctransformconvert%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Converts color data from a source layout to a destination layout using a color transform.
- [func ColorSyncTransformGetProfileSequence(ColorSyncTransform!) -> Unmanaged<CFArray>?](./colorsynctransformgetprofilesequence%28_%29.md)
  Returns the profile sequence used to create a color transform.
- [func ColorSyncTransformCopyProperty(ColorSyncTransform!, CFTypeRef!, CFDictionary?) -> Unmanaged<CFTypeRef>?](./colorsynctransformcopyproperty%28_,_,_%29.md)
  Copies a property from a color transform.
- [func ColorSyncTransformSetProperty(ColorSyncTransform!, CFTypeRef!, CFTypeRef?)](./colorsynctransformsetproperty%28_,_,_%29.md)
  Sets a property on a color transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsynctransformgettypeid())*