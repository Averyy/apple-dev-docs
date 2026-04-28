# Dock.StaticItem.Tile-data

**Framework**: Device Management  
**Kind**: dictionary

The dictionary that contains details about a Dock item.

**Availability**:
- macOS 10.7+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object Dock.StaticItem.Tile-data
```

## Topics

### Objects
- [object Dock.StaticItem.Tile-data.File-data](dock/staticitem/tile-data-data.dictionary/file-data-data.dictionary.md)
  For Apple use only.

## Properties

- `file-data` (Dock.StaticItem.Tile-data.File-data): The data in a file. For Apple use only.
- `file-type` (integer) *(required)*: The type of tile: - `0`: URL
- `1`: File
- `3`: Directory
- `label` (string) *(required)*: The label of the Dock item.
- `url` (string): The URL string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/dock/staticitem/tile-data-data.dictionary)*