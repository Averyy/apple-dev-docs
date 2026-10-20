# ManifestURL.ItemsItem

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

An array of dictionaries representing what the manifest installs.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- macOS 10.9+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```
object ManifestURL.ItemsItem
```

## Topics

### Objects
- [object ManifestURL.ItemsItem.AssetsItem](./itemsitem/assetsitem.md)
  An array of dictionaries that describe an item to install.
- [object ManifestURL.ItemsItem.Metadata](./itemsitem/metadata-data.dictionary.md)
  The metadata for an application or package manifest item.

## Properties

- `assets` ([ManifestURL.ItemsItem.AssetsItem]) *(required)*: An array of dictionaries that describe an item to install.
- `metadata` (ManifestURL.ItemsItem.Metadata) *(required)*: The metadata for an application or package manifest item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/manifesturl/itemsitem)*