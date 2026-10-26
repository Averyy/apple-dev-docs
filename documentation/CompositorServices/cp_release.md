# cp_release

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Decrements the reference count of the specified object.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
void cp_release(void *obj);
```

#### Discussion

Don’t call this function in Swift code or on types you manage using automatic reference counting (ARC).

## Parameters

- `obj`: The object to release. If this parameter is an Objective-C object, the function is equivalent to calling the [`release`](../ObjectiveC/nsobject-c.protocol/release.md) method of that object.

## See Also

### Retaining and releasing types
- [cp_retain](./cp_retain.md)
  Increments the reference count of the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_release)*