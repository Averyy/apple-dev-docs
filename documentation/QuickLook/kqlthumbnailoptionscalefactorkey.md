# kQLThumbnailOptionScaleFactorKey

**Framework**: Quick Look  
**Kind**: var

The scale factor for the thumbnail.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kQLThumbnailOptionScaleFactorKey: CFString!
```

#### Discussion

The scale factor is a `float` value that’s encapsulated in a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) object. If this option is absent, the default value is `1.0`.

## See Also

- [var kQLReturnMask: Int32](kqlreturnmask.md)
  The Quick Look generator can create a preview.
- [var kQLReturnHasMore: Int32](kqlreturnhasmore.md)
  The Quick Look generator has more content to display as part of the preview.
- [let kQLThumbnailOptionIconModeKey: CFString!](kqlthumbnailoptioniconmodekey.md)
  The Quick Look generator produces the thumbnail as an icon with decor.
- [var QUICKLOOK_VERSION: Int32](quicklook_version.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/kqlthumbnailoptionscalefactorkey)*