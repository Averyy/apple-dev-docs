# ManifestURL.ItemsItem

**Framework**: Device Management  
**Kind**: dictionary

An array of dictionaries representing what the manifest installs.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- macOS 10.9+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ManifestURL.ItemsItem
```

## Topics

### Objects
- [object ManifestURL.ItemsItem.AssetsItem](manifesturl/itemsitem/assetsitem.md)
  An array of dictionaries that describe an item to install.
- [object ManifestURL.ItemsItem.Metadata](manifesturl/itemsitem/metadata-data.dictionary.md)
  The metadata for an application or package manifest item.

## Properties

- `assets` ([ManifestURL.ItemsItem.AssetsItem]) *(required)*: An array of dictionaries that describe an item to install.
- `metadata` (ManifestURL.ItemsItem.Metadata) *(required)*: The metadata for an application or package manifest item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/manifesturl/itemsitem)*