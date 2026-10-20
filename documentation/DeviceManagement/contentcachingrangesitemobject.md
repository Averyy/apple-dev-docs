# ContentCachingRangesItemObject

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

A range of IP addresses to cache.

**Availability**:
- macOS 27.0+

## Declaration

```
object ContentCachingRangesItemObject
```

## Properties

- `first` (string) *(required)*: The first IP address in the range.
- `last` (string) *(required)*: The last IP address in the range.
- `type` (string): The IP address type.

  **Default**: `IPv4`; **Allowed Values**: `IPv4`, `IPv6`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/contentcachingrangesitemobject)*