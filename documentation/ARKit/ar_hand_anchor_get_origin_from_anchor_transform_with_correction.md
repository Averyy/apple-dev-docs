# ar_hand_anchor_get_origin_from_anchor_transform_with_correction

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Get the transform from an anchor to the origin coordinate system.

**Availability**:
- visionOS 27.0+

## Declaration

```c
extern simd_float4x4 ar_hand_anchor_get_origin_from_anchor_transform_with_correction(ar_hand_anchor_t hand_anchor, ar_transform_correction_t transform_correction);
```

## Return Value

The origin from anchor transform.

## Parameters

- `hand_anchor`: The anchor.
- `transform_correction`: The transform correction that should be applied.

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
- [ar_hand_tracking_configuration_t](./ar_hand_tracking_configuration_t.md)
- [ar_hand_tracking_provider_create](./ar_hand_tracking_provider_create.md)
  A source of live data about the position of a person’s hands and hand joints.
- [ar_hand_tracking_provider_is_supported](./ar_hand_tracking_provider_is_supported.md)
  Returns a Boolean value that indicates whether the current runtime environment supports hand tracking providers.
- [ar_hand_tracking_provider_get_latest_anchors](./ar_hand_tracking_provider_get_latest_anchors.md)
  Fetches the most recent hand anchors for each hand.
- [ar_hand_tracking_provider_get_required_authorization_type](./ar_hand_tracking_provider_get_required_authorization_type.md)
  Gets the types of authorizations required to track hands.
- [ar_hand_tracking_configuration_create](./ar_hand_tracking_configuration_create.md)
- [ar_hand_tracking_provider_set_update_handler](./ar_hand_tracking_provider_set_update_handler.md)
  Sets the handler for receiving hand tracking updates.
- [ar_hand_tracking_provider_set_update_handler_f](./ar_hand_tracking_provider_set_update_handler_f.md)
  Sets the handler for receiving hand tracking updates.
- [ar_hand_skeleton_joint_name_forearm_arm](./ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_forearm_arm.md)
- [ar_hand_skeleton_joint_name_forearm_wrist](./ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_forearm_wrist.md)
- [ar_hand_skeleton_joint_name_index_finger_intermediate_base](./ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_index_finger_intermediate_base.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_hand_anchor_get_origin_from_anchor_transform_with_correction)*