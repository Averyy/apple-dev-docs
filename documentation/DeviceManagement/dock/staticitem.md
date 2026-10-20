# Dock.StaticItem

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

Items that are located on the Documents side of the Dock and cannot be removed from that location.

**Availability**:
- macOS 10.7+

## Declaration

```
object Dock.StaticItem
```

## Topics

### Objects
- [object Dock.StaticItem.Tile-data](./staticitem/tile-data-data.dictionary.md)
  The dictionary that contains details about a Dock item.

## Properties

- `tile-data` (Dock.StaticItem.Tile-data) *(required)*: The information about the Dock item.
- `tile-type` (string) *(required)*: The type of tile.

  **Allowed Values**: `file-tile`, `directory-tile`, `url-tile`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/dock/staticitem)*