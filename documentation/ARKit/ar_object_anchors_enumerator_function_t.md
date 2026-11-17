# ar_object_anchors_enumerator_function_t

**Framework**: ARKit  
**Kind**: typealias  
**Role**: Type Alias

Function for enumerating a collection of object anchors.

**Availability**:
- visionOS 2.0+

## Declaration

```c
typedef _Bool (*)(void *, NSObject<OS_ar_object_anchor> *) ar_object_anchors_enumerator_function_t;
```

## Return Value

`true` to continue enumerating, or `false` to stop enumerating.

## Parameters

- `context`: The application-defined context.
- `object_anchor`: The object anchor.

## See Also

### Object anchor data types
- [ar_object_anchor_t](./ar_object_anchor_t.md)
  An object that was detected in the environment.
- [ar_object_anchors_enumerator_t](./ar_object_anchors_enumerator_t.md)
  Handler for enumerating a collection of object anchors.
- [ar_object_anchors_t](./ar_object_anchors_t.md)
  A collection of object anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_object_anchors_enumerator_function_t)*