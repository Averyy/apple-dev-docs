# StatusContentCacheStatus

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports the status of the Content Cache service.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
object StatusContentCacheStatus
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
        "status": {
            "server-guid": "C3D4E5F6-A7B8-9012-CDEF-012345678912",
            "activated": true,
            "active": true,
            "cache-status": "OK",
            "private-addresses": [
                "192.168.1.5"
            ],
            "public-address": "203.0.113.5",
            "port": 51194,
            "registration-status": 1,
            "startup-status": "OK",
            "tetherator-status": 0,
            "sending-reports": false,
            "version": "2.0"
        }
    }
}
```

## Topics

### Objects
- [object StatusContentCacheStatusContentCacheStatusObject](statuscontentcachestatuscontentcachestatusobject.md)
  The basic set of AssetCache status items

## Properties

- `content-cache.status` (StatusContentCacheStatusContentCacheStatusObject) *(required)*: The basic set of AssetCache status items

## See Also

- [object StatusContentCacheInfo](statuscontentcacheinfo.md)
  The status item that reports information about the Content Cache service.
- [object StatusContentCacheParents](statuscontentcacheparents.md)
  The status item that reports information about the Content Cache service parent caches.
- [object StatusContentCachePeers](statuscontentcachepeers.md)
  The status item that reports information about the Content Cache service peer caches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statuscontentcachestatus)*