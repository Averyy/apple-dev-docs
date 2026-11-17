# ARKit Data Types

**Framework**: ARKit  
**Role**: API Collection

## Topics

### Barcode data types
- [ar_barcode_anchor_t](./ar_barcode_anchor_t.md)
  An anchor that tracks a barcode’s position and orientation in the physical environment.
- [ar_barcode_anchors_enumerator_function_t](./ar_barcode_anchors_enumerator_function_t.md)
  Function for enumerating a collection of barcode anchors.
- [ar_barcode_anchors_enumerator_t](./ar_barcode_anchors_enumerator_t.md)
  Handler for enumerating a collection of barcode anchors.
- [ar_barcode_anchors_t](./ar_barcode_anchors_t.md)
  A collection of barcode anchors.
- [ar_barcode_detection_callbacks_t](./ar_barcode_detection_callbacks_t.md)
  Callbacks for barcode detection events.
- [ar_barcode_detection_configuration_t](./ar_barcode_detection_configuration_t.md)
  Configuration for barcode detection.
- [ar_barcode_detection_provider_t](./ar_barcode_detection_provider_t.md)
  A data provider for barcode detection.
- [ar_barcode_detection_update_handler_function_t](./ar_barcode_detection_update_handler_function_t.md)
  Function called when there are updates to barcode anchors.
- [ar_barcode_detection_update_handler_t](./ar_barcode_detection_update_handler_t.md)
  Handler called when there are updates to barcode anchors.
### Camera data types
- [ar_camera_frame_parameters_t](./ar_camera_frame_parameters_t.md)
  Parameters for a camera frame including intrinsics, extrinsics, and timestamps.
- [ar_camera_frame_provider_t](./ar_camera_frame_provider_t.md)
  A data provider that delivers camera frames.
- [ar_camera_frame_sample_t](./ar_camera_frame_sample_t.md)
  A single camera frame sample with pixel buffer and metadata.
- [ar_camera_frame_t](./ar_camera_frame_t.md)
  A camera frame containing one or more camera frame samples.
- [ar_camera_frame_update_handler_function_t](./ar_camera_frame_update_handler_function_t.md)
  Function for observing an updated camera frame.
- [ar_camera_frame_update_handler_t](./ar_camera_frame_update_handler_t.md)
  Handler for observing an updated camera frame.
- [ar_camera_video_format_enumerator_function_t](./ar_camera_video_format_enumerator_function_t.md)
  Function for enumerating camera video formats.
- [ar_camera_video_format_enumerator_t](./ar_camera_video_format_enumerator_t.md)
  Handler for enumerating camera video formats.
- [ar_camera_video_format_t](./ar_camera_video_format_t.md)
  Describes a camera video format with frame rate, size, and pixel format.
- [ar_camera_video_formats_t](./ar_camera_video_formats_t.md)
  A collection of camera video formats.
### General data type functions
- [ar_data_t](./ar_data_t.md)
  A container for binary data.
### Environment light estimation data types
- [ar_environment_light_estimation_configuration_t](./ar_environment_light_estimation_configuration_t.md)
  Configuration for environment light estimation.
- [ar_environment_light_estimation_provider_t](./ar_environment_light_estimation_provider_t.md)
  A data provider for environment light estimation.
- [ar_environment_light_estimation_update_handler_function_t](./ar_environment_light_estimation_update_handler_function_t.md)
  Function to be called when there are updates to environment probe anchors.
- [ar_environment_light_estimation_update_handler_t](./ar_environment_light_estimation_update_handler_t.md)
  Handler triggered when there are updates to environment probe anchors.
- [ar_environment_probe_anchor_t](./ar_environment_probe_anchor_t.md)
  An anchor providing environment lighting information for realistic rendering.
- [ar_environment_probe_anchors_enumerator_function_t](./ar_environment_probe_anchors_enumerator_function_t.md)
  Function for enumerating a collection of environment probe anchors.
- [ar_environment_probe_anchors_enumerator_t](./ar_environment_probe_anchors_enumerator_t.md)
  Handler for enumerating a collection of environment probe anchors.
- [ar_environment_probe_anchors_t](./ar_environment_probe_anchors_t.md)
  A collection of environment probe anchors.
- [ar_environment_probe_anchor_get_camera_scale_reference](./ar_environment_probe_anchor_get_camera_scale_reference.md)
  Get the camera scale reference of an environment probe anchor.
### Hand skeleton data types
- [ar_hand_skeleton_t](./ar_hand_skeleton_t.md)
  Represents a hand skeleton with joints and their transforms.
### Identifier data types
- [ar_identifiers_enumerator_function_t](./ar_identifiers_enumerator_function_t.md)
  Function for enumerating a collection of identifiers.
- [ar_identifiers_enumerator_t](./ar_identifiers_enumerator_t.md)
  Handler for enumerating a collection of identifiers.
- [ar_identifiers_t](./ar_identifiers_t.md)
  A collection of UUID identifiers.
### Mesh geometry data types
- [ar_mesh_geometries_enumerator_function_t](./ar_mesh_geometries_enumerator_function_t.md)
  Function for enumerating a collection of mesh geometries.
- [ar_mesh_geometries_enumerator_t](./ar_mesh_geometries_enumerator_t.md)
  Handler for enumerating a collection of mesh geometries.
- [ar_mesh_geometries_t](./ar_mesh_geometries_t.md)
  A collection of mesh geometries.
### Object anchor data types
- [ar_object_anchor_t](./ar_object_anchor_t.md)
  An object that was detected in the environment.
- [ar_object_anchors_enumerator_function_t](./ar_object_anchors_enumerator_function_t.md)
  Function for enumerating a collection of object anchors.
- [ar_object_anchors_enumerator_t](./ar_object_anchors_enumerator_t.md)
  Handler for enumerating a collection of object anchors.
- [ar_object_anchors_t](./ar_object_anchors_t.md)
  A collection of object anchors.
### Object bounding box data types
- [ar_object_axis_aligned_bounding_box_t](./ar_object_axis_aligned_bounding_box_t.md)
  An axis-aligned bounding box for the extent of an object.
### Object tracking data types
- [ar_object_tracking_configuration_t](./ar_object_tracking_configuration_t.md)
  Object tracking configuration.
- [ar_object_tracking_provider_t](./ar_object_tracking_provider_t.md)
  Object tracking provider.
- [ar_object_tracking_update_handler_function_t](./ar_object_tracking_update_handler_function_t.md)
  Function called when there are updates to object anchors.
- [ar_object_tracking_update_handler_t](./ar_object_tracking_update_handler_t.md)
  Handler called when there are updates to object anchors.
### Reference object data types
- [ar_reference_object_bundle_load_completion_handler_function_t](./ar_reference_object_bundle_load_completion_handler_function_t.md)
  Function called when a request to load a reference object from a bundle has completed.
- [ar_reference_object_bundle_load_completion_handler_t](./ar_reference_object_bundle_load_completion_handler_t.md)
  Handler triggered when a request to load a reference object from a bundle has completed.
- [ar_reference_object_t](./ar_reference_object_t.md)
  Defines a physical object to detect in the environment.
- [ar_reference_object_url_load_completion_handler_function_t](./ar_reference_object_url_load_completion_handler_function_t.md)
  Function called when a request to load a reference object from a URL has completed.
- [ar_reference_object_url_load_completion_handler_t](./ar_reference_object_url_load_completion_handler_t.md)
  Handler triggered when a request to load a reference object from a URL has completed.
- [ar_reference_objects_enumerator_function_t](./ar_reference_objects_enumerator_function_t.md)
  Function for enumerating a collection of reference objects.
- [ar_reference_objects_enumerator_t](./ar_reference_objects_enumerator_t.md)
  Handler for enumerating a collection of reference objects.
- [ar_reference_objects_t](./ar_reference_objects_t.md)
  A collection of reference objects.
### Room anchor data types
- [ar_room_anchor_t](./ar_room_anchor_t.md)
  An anchor representing a physical room.
- [ar_room_anchors_enumerator_function_t](./ar_room_anchors_enumerator_function_t.md)
  Function for enumerating a collection of room anchors.
- [ar_room_anchors_enumerator_t](./ar_room_anchors_enumerator_t.md)
  Handler for enumerating a collection of room anchors.
- [ar_room_anchors_t](./ar_room_anchors_t.md)
  A collection of room anchors.
### Room tracking data types
- [ar_room_tracking_configuration_t](./ar_room_tracking_configuration_t.md)
  Configuration for room tracking.
- [ar_room_tracking_provider_t](./ar_room_tracking_provider_t.md)
  A data provider for room tracking.
- [ar_room_tracking_update_handler_function_t](./ar_room_tracking_update_handler_function_t.md)
  Function called when there are updates to room anchors.
- [ar_room_tracking_update_handler_t](./ar_room_tracking_update_handler_t.md)
  Handler called when there are updates to room anchors.
### Skeleton joint data types
- [ar_skeleton_joint_enumerator_function_t](./ar_skeleton_joint_enumerator_function_t.md)
  Function for enumerating skeleton joints.
- [ar_skeleton_joint_enumerator_t](./ar_skeleton_joint_enumerator_t.md)
  Handler for enumerating skeleton joints.
- [ar_skeleton_joint_t](./ar_skeleton_joint_t.md)
  Represents a joint in a skeleton with its transform and tracking state.
### World tracking data types
- [ar_world_tracking_provider_copy_all_world_anchors_completion_function_t](./ar_world_tracking_provider_copy_all_world_anchors_completion_function_t.md)
  Function called when a request to copy all known world anchors has completed (successfully or not).
- [ar_world_tracking_provider_copy_all_world_anchors_completion_handler_t](./ar_world_tracking_provider_copy_all_world_anchors_completion_handler_t.md)
  A handler that the provider calls when a request to copy all known world anchors has completed (successfully or not).

## See Also

### Objective-C compatibility
- [ARKit Functions](./arkit-functions.md)
- [Objective-C compatibility](./objective-c-compatibility.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkit-data-types)*