# cp_retain

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Increments the reference count of the specified object.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
void *cp_retain(void *obj);
```

#### Return Value

The retained object.

#### Discussion

Don’t call this function in Swift code or on types you manage using automatic reference counting (ARC).

## Parameters

- `obj`: The object to retain. If this parameter is an Objective-C object, the function is equivalent to calling the [`retain`](../ObjectiveC/nsobject-c.protocol/retain.md) method of that object.

## See Also

### Retaining and releasing types
- [cp_release](./cp_release.md)
  Decrements the reference count of the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_retain)*