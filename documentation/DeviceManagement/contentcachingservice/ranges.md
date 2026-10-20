# ContentCachingService.Ranges

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

A range of IP addresses to cache.

**Availability**:
- macOS 10.13.4+ - Deprecated in 27.0

> **Deprecated**: Use the declarative management `com.apple.configuration.content-cache.settings` configuration.

## Declaration

```
object ContentCachingService.Ranges
```

## Properties

- `first` (string) *(required)* *(deprecated)*: The first IP address in the range.

  Deprecated: macOS 27+
- `last` (string) *(required)* *(deprecated)*: The last IP address in the range.

  Deprecated: macOS 27+
- `type` (string) *(deprecated)*: The IP address type.

  Deprecated: macOS 27+

  **Default**: `IPv4`; **Allowed Values**: `IPv4`, `IPv6`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/contentcachingservice/ranges)*