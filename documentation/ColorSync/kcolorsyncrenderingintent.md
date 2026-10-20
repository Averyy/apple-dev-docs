# kColorSyncRenderingIntent

**Framework**: ColorSync  
**Kind**: var  
**Role**: Global Variable

A key for the rendering intent to use for the profile in a profile-sequence dictionary.

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
var kColorSyncRenderingIntent: Unmanaged<CFString>!
```

```c
extern CFStringRef kColorSyncRenderingIntent;
```

## See Also

### Choosing rendering intents
- [var kColorSyncRenderingIntentPerceptual: Unmanaged<CFString>!](./kcolorsyncrenderingintentperceptual.md)
  A [`kColorSyncRenderingIntent`](./kcolorsyncrenderingintent.md) value selecting the perceptual rendering intent.
- [var kColorSyncRenderingIntentRelative: Unmanaged<CFString>!](./kcolorsyncrenderingintentrelative.md)
  A [`kColorSyncRenderingIntent`](./kcolorsyncrenderingintent.md) value selecting the media-relative colorimetric rendering intent.
- [var kColorSyncRenderingIntentSaturation: Unmanaged<CFString>!](./kcolorsyncrenderingintentsaturation.md)
  A [`kColorSyncRenderingIntent`](./kcolorsyncrenderingintent.md) value selecting the saturation rendering intent.
- [var kColorSyncRenderingIntentAbsolute: Unmanaged<CFString>!](./kcolorsyncrenderingintentabsolute.md)
  A [`kColorSyncRenderingIntent`](./kcolorsyncrenderingintent.md) value selecting the ICC-absolute colorimetric rendering intent.
- [var kColorSyncRenderingIntentUseProfileHeader: Unmanaged<CFString>!](./kcolorsyncrenderingintentuseprofileheader.md)
  A [`kColorSyncRenderingIntent`](./kcolorsyncrenderingintent.md) value selecting the rendering intent stored in the profile header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsyncrenderingintent)*