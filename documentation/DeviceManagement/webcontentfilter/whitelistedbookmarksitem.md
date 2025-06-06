# WebContentFilter.WhitelistedBookmarksItem

**Framework**: Device Management  
**Kind**: dictionary

The bookmark in the allow list of the web content filter.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 10.15+
- visionOS 1.1+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object WebContentFilter.WhitelistedBookmarksItem
```

#### Discussion

This device management profile adds any URLs in the allow list to the browser’s bookmarks. The browser prevents the user from visiting any sites not bookmarked. The number of bookmarks on the allow list should be limited to about 500.

## See Also

- [object WebContentFilter.AllowListBookmarksItem](webcontentfilter/allowlistbookmarksitem.md)
  The bookmark in the allow list of the web content filter.
- [object WebContentFilter.VendorConfig](webcontentfilter/vendorconfig-data.dictionary.md)
  A custom dictionary for the filtering service plug-in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/webcontentfilter/whitelistedbookmarksitem)*