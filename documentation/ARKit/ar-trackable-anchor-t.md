# ar_trackable_anchor_t

**Framework**: ARKit  
**Kind**: typealias

An anchor that can gain and lose its tracking state over the course of a session.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
typedef NSObject<OS_ar_trackable_anchor> * ar_trackable_anchor_t;
```

## See Also

- [ar_anchor_get_identifier](ar_anchor_get_identifier.md)
  Gets the unique identifier that distinguishes this anchor from all other anchors.
- [ar_anchor_get_timestamp](ar_anchor_get_timestamp.md)
  Gets the timestamp corresponding to the anchor.
- [ar_anchor_get_origin_from_anchor_transform](ar_anchor_get_origin_from_anchor_transform.md)
  Gets the transform from the anchor to the origin coordinate system.
- [ar_trackable_anchor_is_tracked](ar_trackable_anchor_is_tracked.md)
  Returns a Boolean value that indicates whether ARKit is tracking an anchor.
- [ar_anchor_t](ar_anchor_t.md)
  The identity, location, and orientation of an object in world space.
- [ar_mesh_anchor_t](ar_mesh_anchor_t.md)
  A surface’s position in a person’s surroundings.
- [ar_mesh_anchors_t](ar_mesh_anchors_t.md)
  A collection of mesh anchors.
- [ar_mesh_anchors_enumerator_t](ar_mesh_anchors_enumerator_t.md)
  A handler for enumerating a collection of mesh anchors.
- [ar_image_anchor_t](ar_image_anchor_t.md)
  A 2D image’s position in a person’s surroundings.
- [ar_image_anchors_t](ar_image_anchors_t.md)
  A collection of image anchors.
- [ar_image_anchors_enumerator_t](ar_image_anchors_enumerator_t.md)
  A handler for enumerating a collection of image anchors.
- [ar_hand_anchor_t](ar_hand_anchor_t.md)
  A hand’s position in a person’s surroundings.
- [ar_world_anchor_t](ar_world_anchor_t.md)
  A fixed location in a person’s surroundings.
- [ar_world_anchors_t](ar_world_anchors_t.md)
  A collection of world anchors.
- [ar_world_anchors_enumerator_t](ar_world_anchors_enumerator_t.md)
  A handler for enumerating a collection of world anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_trackable_anchor_t)*