# StatusContentCacheInfo

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports information about the Content Cache service.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
object StatusContentCacheInfo
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

```json
{
    "content-cache": {
        "info": {
            "cache-free": 10737418240,
            "cache-limit": 0,
            "cache-status": "OK",
            "cache-used": 5368709120,
            "max-cache-pressure-last-hour": 0.15,
            "personal-cache-free": 2147483648,
            "personal-cache-limit": 0,
            "personal-cache-used": 1073741824
        }
    }
}
```

## Topics

### Objects
- [object StatusContentCacheInfoContentCacheInfoObject](statuscontentcacheinfocontentcacheinfoobject.md)
  A dictionary that contains info about the usage of the Content Cache on the device

## Properties

- `content-cache.info` (StatusContentCacheInfoContentCacheInfoObject) *(required)*: A dictionary that contains info about the usage of the Content Cache on the device

## See Also

- [object StatusContentCacheParents](statuscontentcacheparents.md)
  The status item that reports information about the Content Cache service parent caches.
- [object StatusContentCachePeers](statuscontentcachepeers.md)
  The status item that reports information about the Content Cache service peer caches.
- [object StatusContentCacheService](statuscontentcacheservice.md)
  The status item that reports the status of the Content Cache service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statuscontentcacheinfo)*