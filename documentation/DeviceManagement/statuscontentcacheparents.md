# StatusContentCacheParents

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports information about the Content Cache service parent caches.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
object StatusContentCacheParents
```

#### Discussion

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | macOS |
| Allowed in device enrollment | N/A |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | macOS |
| Allowed in system scope | macOS |
| Allowed in user scope | N/A |

##### Status Item Example

**New or updated parent**:

Reports a new or updated parent.

```json
{
    "content-cache": {
        "parents": [
            {
                "identifier": "A1B2C3D4-E5F6-7890-ABCD-EF1234567890",
                "address": "192.168.1.10",
                "port": 51194,
                "healthy": true,
                "version": "2.0"
            }
        ]
    }
}
```

**Removed parent**:

Reports a removed parent.

```json
{
    "content-cache": {
        "parents": [
            {
                "identifier": "A1B2C3D4-E5F6-7890-ABCD-EF1234567890",
                "_removed": true
            }
        ]
    }
}
```

## Topics

### Objects
- [object StatusContentCacheParentsParentsItemObject](statuscontentcacheparentsparentsitemobject.md)
  A parent Content Cache.

## Properties

- `content-cache.parents` ([StatusContentCacheParentsParentsItemObject]): An array of dictionaries that describes parent Content Caches.

## See Also

- [object StatusContentCacheInfo](statuscontentcacheinfo.md)
  The status item that reports information about the Content Cache service.
- [object StatusContentCachePeers](statuscontentcachepeers.md)
  The status item that reports information about the Content Cache service peer caches.
- [object StatusContentCacheService](statuscontentcacheservice.md)
  The status item that reports the status of the Content Cache service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statuscontentcacheparents)*