# StatusContentCacheParentsParentsItemObject

**Framework**: Device Management  
**Kind**: dictionary

A parent Content Cache.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
object StatusContentCacheParentsParentsItemObject
```

## Properties

- `_removed` (boolean): If `true`, the system removed the parent entry and only this key and the `identifier` key are present in the status item object.
- `address` (string) *(required)*: The local IPv4 address of the parent Content Cache.
- `healthy` (boolean) *(required)*: If `true,` the parent Content Cache is able to respond to requests from this Content Cache.
- `identifier` (string) *(required)*: The unique identifier of the parent Content Cache.
- `port` (integer) *(required)*: The IP port number the parent Content Cache listens to for requests.
- `version` (string) *(required)*: The version number of the parent Content Cache software.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statuscontentcacheparentsparentsitemobject)*