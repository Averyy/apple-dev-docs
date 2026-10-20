# ParentalControlsContentFilter.SiteAllowListItem

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

A dictionary defining a site for the allow list.

**Availability**:
- macOS 15.2+

## Declaration

```
object ParentalControlsContentFilter.SiteAllowListItem
```

## Properties

- `address` (string) *(required)*: The site prefix, including the `http(s)` scheme.
- `pageTitle` (string): The site page title.

## See Also

### Objects
- [object ParentalControlsContentFilter.SiteWhitelistItem](./sitewhitelistitem.md)
  A dictionary defining a site for the allow list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/parentalcontrolscontentfilter/siteallowlistitem)*