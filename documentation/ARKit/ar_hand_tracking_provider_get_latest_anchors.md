# ar_hand_tracking_provider_get_latest_anchors

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Fetches the most recent hand anchors for each hand.

**Availability**:
- visionOS 1.0+

## Declaration

```c
extern bool ar_hand_tracking_provider_get_latest_anchors(ar_hand_tracking_provider_t hand_tracking_provider, ar_hand_anchor_t hand_anchor_left, ar_hand_anchor_t hand_anchor_right);
```

## Return Value

`true` on success while the `hand_tracking_provider` is running, `false` otherwise.

## Discussion

Subsequent calls will continue returning the latest hand tracking data. New anchor data will be returned when the hand tracking data is updated.

> **Note**: For apps compiled with a visionOS 1.0 SDK, subsequent calls to this function will not update the given `ar_hand_anchor_t` instances, and will return `false` until the latest hand tracking data has arrived.

## Parameters

- `hand_tracking_provider`: The hand tracking provider.
- `hand_anchor_left`: The `ar_hand_anchor_t` instance for the left hand to be updated.
- `hand_anchor_right`: The `ar_hand_anchor_t` instance for the right hand to be updated.

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
- [ar_hand_tracking_provider_get_required_authorization_type](./ar_hand_tracking_provider_get_required_authorization_type.md)
  Gets the types of authorizations required to track hands.
- [ar_hand_tracking_configuration_create](./ar_hand_tracking_configuration_create.md)
  Create a hand tracking configuration.
- [ar_hand_tracking_provider_set_update_handler](./ar_hand_tracking_provider_set_update_handler.md)
  Sets the handler for receiving hand tracking updates.
- [ar_hand_tracking_provider_set_update_handler_f](./ar_hand_tracking_provider_set_update_handler_f.md)
  Sets the function for receiving hand tracking updates.
- [ar_hand_skeleton_joint_name_forearm_arm](./ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_forearm_arm.md)
  Joint names in the hand skeleton.
- [ar_hand_skeleton_joint_name_forearm_wrist](./ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_forearm_wrist.md)
  Joint names in the hand skeleton.
- [ar_hand_skeleton_joint_name_index_finger_intermediate_base](./ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_index_finger_intermediate_base.md)
  Joint names in the hand skeleton.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_hand_tracking_provider_get_latest_anchors)*