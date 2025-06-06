# kQLThumbnailOptionIconModeKey

**Framework**: Quick Look  
**Kind**: var

The Quick Look generator produces the thumbnail as an icon with decor.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kQLThumbnailOptionIconModeKey: CFString!
```

#### Discussion

The default value is [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse). If you use the default, the Quick Look feature creates a thumbnail image with no icon decor. To create the thumbnail as an icon, set the value to [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue). The icon’s image includes all the typical icon decor, such as shadows and a curled corner.

## See Also

- [var kQLReturnMask: Int32](kqlreturnmask.md)
  The Quick Look generator can create a preview.
- [var kQLReturnHasMore: Int32](kqlreturnhasmore.md)
  The Quick Look generator has more content to display as part of the preview.
- [let kQLThumbnailOptionScaleFactorKey: CFString!](kqlthumbnailoptionscalefactorkey.md)
  The scale factor for the thumbnail.
- [var QUICKLOOK_VERSION: Int32](quicklook_version.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/kqlthumbnailoptioniconmodekey)*