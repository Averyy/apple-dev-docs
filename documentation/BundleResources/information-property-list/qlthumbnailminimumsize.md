# QLThumbnailMinimumSize

**Framework**: Bundle Resources  
**Kind**: typealias

The minimum size, in points, along one dimension of thumbnails for a Quick Look app’s generator.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.0+
- visionOS 1.0+

#### Discussion

If you set this key, Quick Look uses the [`GenerateThumbnailForURL`](https://developer.apple.com/documentation/QuickLook/QLGeneratorInterfaceStruct/GenerateThumbnailForURL) property for thumbnail sizes greater than this value. If your app’s generator is fast, you can omit this key so that the thumbnail appears in standard lists.

## See Also

- [QLNeedsToBeRunInMainThread](information-property-list/qlneedstoberuninmainthread.md)
  A Boolean value indicating whether a Quick Look app’s generator can be run in threads other than the main thread.
- [QLPreviewHeight](information-property-list/qlpreviewheight.md)
  A hint at the height, in points, of a Quick Look app’s previews.
- [QLPreviewWidth](information-property-list/qlpreviewwidth.md)
  A hint at the width, in points, of a Quick Look app’s previews.
- [QLSupportsConcurrentRequests](information-property-list/qlsupportsconcurrentrequests.md)
  A Boolean value indicating whether a Quick Look app’s  generator can handle concurrent thumbnail and preview requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/qlthumbnailminimumsize)*