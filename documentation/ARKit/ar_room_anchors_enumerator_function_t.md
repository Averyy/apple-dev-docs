# ar_room_anchors_enumerator_function_t

**Framework**: ARKit  
**Kind**: typealias  
**Role**: Type Alias

Function for enumerating a collection of room anchors.

**Availability**:
- visionOS 2.0+

## Declaration

```c
typedef _Bool (*)(void *, NSObject<OS_ar_room_anchor> *) ar_room_anchors_enumerator_function_t;
```

## Return Value

`true` to continue enumerating, or `false` to stop enumerating.

## Parameters

- `context`: The application-defined context.
- `room_anchor`: The room anchor.

## See Also

### Room anchor data types
- [ar_room_anchor_t](./ar_room_anchor_t.md)
  An anchor representing a physical room.
- [ar_room_anchors_enumerator_t](./ar_room_anchors_enumerator_t.md)
  Handler for enumerating a collection of room anchors.
- [ar_room_anchors_t](./ar_room_anchors_t.md)
  A collection of room anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_room_anchors_enumerator_function_t)*