# CVDisplayLinkRetain

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Retains a display link.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.4+ - Deprecated in 15.0

## Declaration

```c
extern CVDisplayLinkRefCVDisplayLinkRetain(CVDisplayLinkRef displayLink);
```

#### Return Value

For convenience, this function returns the retained display link if successful.

## Parameters

- `displayLink`: The display link to be retained. This function is `NULL`-safe.

## See Also

### Retaining and Releasing Display Links
- [CVDisplayLinkRelease](./cvdisplaylinkrelease.md)
  Releases a display link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinkretain)*