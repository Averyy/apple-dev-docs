# CVDisplayLinkRelease

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Releases a display link.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.4+ - Deprecated in 15.0

## Declaration

```c
extern void CVDisplayLinkRelease(CVDisplayLinkRef displayLink);
```

## Parameters

- `displayLink`: The display link to release. This function is `NULL`-safe.

## See Also

### Retaining and Releasing Display Links
- [CVDisplayLinkRetain](./cvdisplaylinkretain.md)
  Retains a display link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinkrelease)*