# ar_scene_reconstruction_update_handler_function_t

**Framework**: ARKit  
**Kind**: typealias

**Availability**:
- visionOS 1.0+

## Declaration

```swift
typedef void (*)(void *, NSObject<OS_ar_mesh_anchors> *, NSObject<OS_ar_mesh_anchors> *, NSObject<OS_ar_mesh_anchors> *) ar_scene_reconstruction_update_handler_function_t;
```

## See Also

- [ar_scene_reconstruction_configuration_t](ar_scene_reconstruction_configuration_t.md)
- [ar_scene_reconstruction_mode_t](ar_scene_reconstruction_mode_t.md)
  The additional kinds of information you can request about a person’s surroundings.
- [ar_scene_reconstruction_provider_create](ar_scene_reconstruction_provider_create.md)
  Creates a provider that reconstructs the person’s surroundings.
- [ar_scene_reconstruction_provider_is_supported](ar_scene_reconstruction_provider_is_supported.md)
  Returns a Boolean value that indicates whether the current runtime environment supports scene reconstruction providers.
- [ar_scene_reconstruction_provider_get_required_authorization_type](ar_scene_reconstruction_provider_get_required_authorization_type.md)
  Gets the types of authorizations needed to run scene reconstruction.
- [ar_scene_reconstruction_configuration_create](ar_scene_reconstruction_configuration_create.md)
  Creates a scene reconstruction configuration.
- [ar_scene_reconstruction_configuration_get_scene_reconstruction_mode](ar_scene_reconstruction_configuration_get_scene_reconstruction_mode.md)
  Gets the scene reconstruction mode.
- [ar_scene_reconstruction_configuration_set_scene_reconstruction_mode](ar_scene_reconstruction_configuration_set_scene_reconstruction_mode.md)
  Sets the scene reconstruction mode.
- [ar_scene_reconstruction_provider_set_update_handler](ar_scene_reconstruction_provider_set_update_handler.md)
  Sets the handler for receiving scene reconstruction updates.
- [ar_scene_reconstruction_provider_set_update_handler_f](ar_scene_reconstruction_provider_set_update_handler_f.md)
  Sets the handler for receiving scene reconstruction updates.
- [ar_mesh_classification_t](ar_mesh_classification_t.md)
  The kinds of classification a mesh anchor can have.
- [ar_mesh_anchor_get_geometry](ar_mesh_anchor_get_geometry.md)
  Gets the shape of a mesh anchor.
- [ar_mesh_anchors_enumerate_anchors](ar_mesh_anchors_enumerate_anchors.md)
  Enumerates a collection of mesh anchors.
- [ar_mesh_anchors_enumerate_anchors_f](ar_mesh_anchors_enumerate_anchors_f.md)
  Enumerates a collection of mesh anchors.
- [ar_mesh_anchors_get_count](ar_mesh_anchors_get_count.md)
  Gets the number of mesh anchors in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_scene_reconstruction_update_handler_function_t)*