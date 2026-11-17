# ar_world_tracking_provider_copy_all_world_anchors_f

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Copies all known world anchors from the world tracking provider asynchronously.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern void ar_world_tracking_provider_copy_all_world_anchors_f(ar_world_tracking_provider_t world_tracking_provider, void *context, ar_world_tracking_provider_copy_all_world_anchors_completion_function_t copy_all_anchors_completion_handler_function);
```

## Discussion

> **Note**: This is not a blocking call. It will return all anchors that have been added successfully before the completion handler is called.

## Parameters

- `world_tracking_provider`: The world tracking provider.
- `context`: The application-defined context parameter to pass to the function.
- `copy_all_anchors_completion_handler_function`: The function to be called with the result of the request for all known world anchors.

## See Also

### World anchor functions
- [ar_world_anchor_get_identifier](./ar_world_anchor_get_identifier.md)
  Get the identifier of an anchor.
- [ar_world_anchor_get_origin_from_anchor_transform](./ar_world_anchor_get_origin_from_anchor_transform.md)
  Get the transform from an anchor to the origin coordinate system.
- [ar_world_anchor_get_timestamp](./ar_world_anchor_get_timestamp.md)
  Get the timestamp corresponding to an anchor.
- [ar_world_anchor_is_equal_to_world_anchor](./ar_world_anchor_is_equal_to_world_anchor.md)
  Returns a bool value that indicates whether the two world anchors are equal.
- [ar_world_anchor_is_tracked](./ar_world_anchor_is_tracked.md)
  Determine whether an anchor is tracked.
- [ar_world_tracking_provider_copy_all_world_anchors](./ar_world_tracking_provider_copy_all_world_anchors.md)
  Copies all known world anchors from the world tracking provider asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_world_tracking_provider_copy_all_world_anchors_f)*