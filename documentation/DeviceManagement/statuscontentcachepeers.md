# StatusContentCachePeers

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports information about the Content Cache service peer caches.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
object StatusContentCachePeers
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

**New or updated peer**:

Reports a new or updated peer.

```json
{
    "content-cache": {
        "peers": [
            {
                "identifier": "B2C3D4E5-F6A7-8901-BCDE-F01234567891",
                "address": "192.168.1.20",
                "port": 51194,
                "friendly": true,
                "healthy": true,
                "version": "2.0"
            }
        ]
    }
}
```

**Removed peer**:

Reports a removed peer.

```json
{
    "content-cache": {
        "peers": [
            {
                "identifier": "B2C3D4E5-F6A7-8901-BCDE-F01234567891",
                "_removed": true
            }
        ]
    }
}
```

## Topics

### Objects
- [object StatusContentCachePeersPeerItemObject](statuscontentcachepeerspeeritemobject.md)
  A peer Content Cache.

## Properties

- `content-cache.peers` ([StatusContentCachePeersPeerItemObject]) *(required)*: An array of dictionaries that describes peer Content Caches.

## See Also

- [object StatusContentCacheInfo](statuscontentcacheinfo.md)
  The status item that reports information about the Content Cache service.
- [object StatusContentCacheParents](statuscontentcacheparents.md)
  The status item that reports information about the Content Cache service parent caches.
- [object StatusContentCacheService](statuscontentcacheservice.md)
  The status item that reports the status of the Content Cache service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statuscontentcachepeers)*