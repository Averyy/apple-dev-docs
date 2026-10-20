# WebContentFilter.WhitelistedBookmarksItem

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

The bookmark in the allow list of the web content filter.

**Availability**:
- iOS 7.0+ - Deprecated in 14.5
- iPadOS 7.0+ - Deprecated in 14.5
- Mac Catalyst 7.0+ - Deprecated in 14.5

## Declaration

```
object WebContentFilter.WhitelistedBookmarksItem
```

## Properties

- `Title` (string) *(required)* *(deprecated)*: The title of the bookmark.

  Deprecated: iOS 14.5+ | iPadOS 14.5+
- `URL` (string) *(required)* *(deprecated)*: The URL of the bookmark in the allow list.

  Deprecated: iOS 14.5+ | iPadOS 14.5+

## See Also

### Objects
- [object WebContentFilter.AllowListBookmarksItem](./allowlistbookmarksitem.md)
  The bookmark in the allow list of the web content filter.
- [object WebContentFilter.URLFilterParameters](./urlfilterparameters-data.dictionary.md)
  A dictionary containing URL filter parameters.
- [object WebContentFilter.VendorConfig](./vendorconfig-data.dictionary.md)
  A custom dictionary for the filtering service plug-in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/webcontentfilter/whitelistedbookmarksitem)*