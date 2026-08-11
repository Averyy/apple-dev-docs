# kColorSyncTransformCreator

**Framework**: ColorSync  
**Kind**: var

A key for the name of the CMM that created the transform.

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
var kColorSyncTransformCreator: Unmanaged<CFString>!
```

## See Also

- [var kColorSyncProfile: Unmanaged<CFString>!](kcolorsyncprofile.md)
  A key for the profile object in a profile-sequence dictionary passed to [`ColorSyncTransformCreate(_:_:)`](colorsynctransformcreate(_:_:).md).
- [var kColorSyncTransformDeviceToPCS: Unmanaged<CFString>!](kcolorsynctransformdevicetopcs.md)
  A [`kColorSyncTransformTag`](kcolorsynctransformtag.md) value selecting the device-to-PCS conversion direction.
- [var kColorSyncTransformDstSpace: Unmanaged<CFString>!](kcolorsynctransformdstspace.md)
  A key for the transform’s destination color space.
- [var kColorSyncTransformInfo: Unmanaged<CFString>!](kcolorsynctransforminfo.md)
  A key for a dictionary of information about the transform.
- [var kColorSyncTransformPCSToDevice: Unmanaged<CFString>!](kcolorsynctransformpcstodevice.md)
  A [`kColorSyncTransformTag`](kcolorsynctransformtag.md) value selecting the PCS-to-device conversion direction.
- [var kColorSyncTransformPCSToPCS: Unmanaged<CFString>!](kcolorsynctransformpcstopcs.md)
  A [`kColorSyncTransformTag`](kcolorsynctransformtag.md) value selecting the PCS-to-PCS conversion direction.
- [var kColorSyncTransformProfileSequnce: Unmanaged<CFString>!](kcolorsynctransformprofilesequnce.md)
  A key for the profile sequence used to create the transform.
- [var kColorSyncTransformSrcSpace: Unmanaged<CFString>!](kcolorsynctransformsrcspace.md)
  A key for the transform’s source color space.
- [var kColorSyncTransformTag: Unmanaged<CFString>!](kcolorsynctransformtag.md)
  A key for the tag identifying which tags of the profile to use in a profile-sequence dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsynctransformcreator)*