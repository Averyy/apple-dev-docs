# ar_hand_tracking_provider_set_update_handler_f

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Sets the function for receiving hand tracking updates.

**Availability**:
- visionOS 1.0+

## Declaration

```c
extern void ar_hand_tracking_provider_set_update_handler_f(ar_hand_tracking_provider_t hand_tracking_provider, dispatch_queue_t hand_anchor_updates_queue, void *context, ar_hand_tracking_update_handler_function_t hand_tracking_update_handler_function);
```

## Discussion

> **Note**: Setting this function will override the handler set using `ar_hand_tracking_provider_set_update_handler`.

## Parameters

- `hand_tracking_provider`: The hand tracking provider.
- `hand_anchor_updates_queue`: The queue on which the function will be called. Passing NULL will default to the main queue.
- `context`: The application-defined context parameter to pass to the function.
- `hand_tracking_update_handler_function`: The function to be called when new data arrives.

## See Also

### Hand tracking
- [ar_hand_chirality_t](./ar_hand_chirality_t.md)
  The values identifying hand chirality.
- [ar_hand_anchor_create](./ar_hand_anchor_create.md)
  Creates a hand anchor.
- [ar_hand_anchor_get_chirality](./ar_hand_anchor_get_chirality.md)
  Gets the value that indicates whether the hand is a left or right hand.
- [ar_hand_anchor_get_fidelity](./ar_hand_anchor_get_fidelity.md)
  Get the fidelity of the hand anchor.
- [ar_hand_anchor_get_origin_from_anchor_transform_with_correction](./ar_hand_anchor_get_origin_from_anchor_transform_with_correction.md)
  Get the transform from an anchor to the origin coordinate system.
- [ar_hand_tracking_configuration_t](./ar_hand_tracking_configuration_t.md)
  Configuration for hand tracking.
- [ar_hand_tracking_provider_create](./ar_hand_tracking_provider_create.md)
  Creates a hand tracking provider.
- [ar_hand_tracking_provider_is_supported](./ar_hand_tracking_provider_is_supported.md)
  Returns a Boolean value that indicates whether the current runtime environment supports hand tracking providers.
- [ar_hand_tracking_provider_get_latest_anchors](./ar_hand_tracking_provider_get_latest_anchors.md)
  Fetches the most recent hand anchors for each hand.
- [ar_hand_tracking_provider_get_required_authorization_type](./ar_hand_tracking_provider_get_required_authorization_type.md)
  Gets the types of authorizations required to track hands.
- [ar_hand_tracking_configuration_create](./ar_hand_tracking_configuration_create.md)
  Create a hand tracking configuration.
- [ar_hand_tracking_provider_set_update_handler](./ar_hand_tracking_provider_set_update_handler.md)
  Sets the handler for receiving hand tracking updates.
- [ar_hand_skeleton_joint_name_forearm_arm](./ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_forearm_arm.md)
  Joint names in the hand skeleton.
- [ar_hand_skeleton_joint_name_forearm_wrist](./ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_forearm_wrist.md)
  Joint names in the hand skeleton.
- [ar_hand_skeleton_joint_name_index_finger_intermediate_base](./ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_index_finger_intermediate_base.md)
  Joint names in the hand skeleton.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_hand_tracking_provider_set_update_handler_f)*