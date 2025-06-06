# ar_hand_tracking_provider_get_latest_anchors

**Framework**: ARKit  
**Kind**: func

Fetches the most recent hand anchors for each hand.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
extern bool ar_hand_tracking_provider_get_latest_anchors(ar_hand_tracking_provider_t hand_tracking_provider, ar_hand_anchor_t hand_anchor_left, ar_hand_anchor_t hand_anchor_right);
```

## See Also

- [ar_hand_chirality_t](ar_hand_chirality_t.md)
  The values identifying hand chirality.
- [ar_hand_anchor_create](ar_hand_anchor_create.md)
  Creates a hand anchor.
- [ar_hand_anchor_get_chirality](ar_hand_anchor_get_chirality.md)
  Gets the value that indicates whether the hand is a left or right hand.
- [ar_hand_tracking_configuration_t](ar_hand_tracking_configuration_t.md)
- [ar_hand_tracking_provider_create](ar_hand_tracking_provider_create.md)
  A source of live data about the position of a person’s hands and hand joints.
- [ar_hand_tracking_provider_is_supported](ar_hand_tracking_provider_is_supported.md)
  Returns a Boolean value that indicates whether the current runtime environment supports hand tracking providers.
- [ar_hand_tracking_provider_get_required_authorization_type](ar_hand_tracking_provider_get_required_authorization_type.md)
  Gets the types of authorizations required to track hands.
- [ar_hand_tracking_configuration_create](ar_hand_tracking_configuration_create.md)
- [ar_hand_tracking_provider_set_update_handler](ar_hand_tracking_provider_set_update_handler.md)
  Sets the handler for receiving hand tracking updates.
- [ar_hand_tracking_provider_set_update_handler_f](ar_hand_tracking_provider_set_update_handler_f.md)
  Sets the handler for receiving hand tracking updates.
- [ar_hand_skeleton_joint_name_forearm_arm](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_forearm_arm.md)
- [ar_hand_skeleton_joint_name_forearm_wrist](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_forearm_wrist.md)
- [ar_hand_skeleton_joint_name_index_finger_intermediate_base](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_index_finger_intermediate_base.md)
- [ar_hand_skeleton_joint_name_index_finger_intermediate_tip](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_index_finger_intermediate_tip.md)
- [ar_hand_skeleton_joint_name_index_finger_knuckle](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_index_finger_knuckle.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_hand_tracking_provider_get_latest_anchors)*