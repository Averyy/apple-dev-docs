# ColorSyncTransformCopyProperty(_:_:_:)

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

Copies a property from a color transform.

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
func ColorSyncTransformCopyProperty(_ transform: ColorSyncTransform!, _ key: CFTypeRef!, _ options: CFDictionary?) -> Unmanaged<CFTypeRef>?
```

```c
extern CFTypeRefColorSyncTransformCopyProperty(ColorSyncTransformRef transform, CFTypeRef key, CFDictionaryRef options);
```

## Parameters

- `transform`: The transform from which to copy the property.
- `key`: A `CFTypeRef` used as a key to identify the property.
- `options`: A dictionary with additional options.

## See Also

### Creating and applying a transform
- [func ColorSyncTransformCreate(CFArray?, CFDictionary?) -> Unmanaged<ColorSyncTransform>?](./colorsynctransformcreate%28_,_%29.md)
  Creates a color transform from a sequence of profiles.
- [func ColorSyncTransformConvert(ColorSyncTransform!, Int, Int, UnsafeMutableRawPointer!, ColorSyncDataDepth, ColorSyncDataLayout, Int, UnsafeRawPointer!, ColorSyncDataDepth, ColorSyncDataLayout, Int, CFDictionary?) -> Bool](./colorsynctransformconvert%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Converts color data from a source layout to a destination layout using a color transform.
- [func ColorSyncTransformGetProfileSequence(ColorSyncTransform!) -> Unmanaged<CFArray>?](./colorsynctransformgetprofilesequence%28_%29.md)
  Returns the profile sequence used to create a color transform.
- [func ColorSyncTransformSetProperty(ColorSyncTransform!, CFTypeRef!, CFTypeRef?)](./colorsynctransformsetproperty%28_,_,_%29.md)
  Sets a property on a color transform.
- [func ColorSyncTransformGetTypeID() -> CFTypeID](./colorsynctransformgettypeid%28%29.md)
  Returns the type identifier for the `ColorSyncTransform` opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsynctransformcopyproperty(_:_:_:))*