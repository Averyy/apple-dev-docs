# nw_retain

**Framework**: Network  
**Kind**: func  
**Role**: Function

Adds a reference count to a Network.framework object.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```c
void *nw_retain(void *obj);
```

## See Also

### Related Documentation
- [os_retain](../os/os_retain-c.func.md)
### Memory Management
- [nw_release](./nw_release.md)
  Releases a reference count on a Network.framework object.
- [typealias nw_object_t](./nw_object_t.md)
  The generic type for objects in the Network framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_retain)*