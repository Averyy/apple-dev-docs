# ARKit Functions

**Framework**: ARKit  
**Role**: API Collection

## Topics

### Barcode functions
- [ar_barcode_anchor_copy_payload_data](./ar_barcode_anchor_copy_payload_data.md)
  Get a copy of a barcode anchor’s payload data.
- [ar_barcode_anchor_get_extent](./ar_barcode_anchor_get_extent.md)
  Get the extent of a detected barcode’s bounding box.
- [ar_barcode_anchor_get_identifier](./ar_barcode_anchor_get_identifier.md)
  Get the identifier of an anchor.
- [ar_barcode_anchor_get_origin_from_anchor_transform](./ar_barcode_anchor_get_origin_from_anchor_transform.md)
  Get the transform from an anchor to the origin coordinate system.
- [ar_barcode_anchor_get_payload_string_value](./ar_barcode_anchor_get_payload_string_value.md)
  Get the payload string value of a barcode anchor.
- [ar_barcode_anchor_get_symbology](./ar_barcode_anchor_get_symbology.md)
  Get the symbology of a barcode anchor.
- [ar_barcode_anchor_get_timestamp](./ar_barcode_anchor_get_timestamp.md)
  Get the timestamp corresponding to an anchor.
- [ar_barcode_anchors_enumerate_anchors](./ar_barcode_anchors_enumerate_anchors.md)
  Enumerate a collection of barcode anchors.
- [ar_barcode_anchors_enumerate_anchors_f](./ar_barcode_anchors_enumerate_anchors_f.md)
  Enumerates a collection of barcode anchors using a function.
- [ar_barcode_anchors_get_count](./ar_barcode_anchors_get_count.md)
  Get the count of barcode anchors in a collection.
- [ar_barcode_detection_configuration_create](./ar_barcode_detection_configuration_create.md)
  Create a barcode detection configuration.
- [ar_barcode_detection_configuration_set_detection_symbology](./ar_barcode_detection_configuration_set_detection_symbology.md)
  Set the desired symbologies to detect.
- [ar_barcode_detection_provider_create](./ar_barcode_detection_provider_create.md)
  Create a barcode detection provider.
- [ar_barcode_detection_provider_get_required_authorization_type](./ar_barcode_detection_provider_get_required_authorization_type.md)
  Get the authorization type required by the barcode detection provider.
- [ar_barcode_detection_provider_is_supported](./ar_barcode_detection_provider_is_supported.md)
  Determines whether this device supports the barcode detection provider.
- [ar_barcode_detection_provider_set_update_handler](./ar_barcode_detection_provider_set_update_handler.md)
  Set the handler for receiving barcode detection updates.
- [ar_barcode_detection_provider_set_update_handler_f](./ar_barcode_detection_provider_set_update_handler_f.md)
  Set the function for receiving barcode detection updates.
- [ar_barcode_anchor_get_origin_from_anchor_transform_with_correction](./ar_barcode_anchor_get_origin_from_anchor_transform_with_correction.md)
  Get the transform from an anchor to the origin coordinate system with a transform correction option.
- [ar_barcode_detection_symbology_t](./ar_barcode_detection_symbology_t.md)
  Option set describing possible symbologies of a detected barcode.
### Camera functions
- [ar_camera_video_format_copy_supported_video_formats](./ar_camera_video_format_copy_supported_video_formats.md)
  Returns a collection of supported video formats for a given camera type and position.
- [ar_camera_frame_get_primary_frame_sample](./ar_camera_frame_get_primary_frame_sample.md)
  Get the primary frame sample for this camera frame.
- [ar_camera_video_format_get_maximum_frame_duration](./ar_camera_video_format_get_maximum_frame_duration.md)
  Get the maximum frame duration for this video format.
- [ar_camera_video_format_get_minimum_frame_duration](./ar_camera_video_format_get_minimum_frame_duration.md)
  Get the minimum frame duration for this video format.
- [ar_camera_frame_is_equal_to_camera_frame](./ar_camera_frame_is_equal_to_camera_frame.md)
  Returns a bool value that indicates whether the two camera frames are equal.
- [ar_camera_frame_parameters_get_camera_position](./ar_camera_frame_parameters_get_camera_position.md)
  Get the camera position.
- [ar_camera_frame_parameters_get_camera_type](./ar_camera_frame_parameters_get_camera_type.md)
  Get the camera type.
- [ar_camera_frame_parameters_get_capture_timestamp](./ar_camera_frame_parameters_get_capture_timestamp.md)
  Get the frame capture timestamp.
- [ar_camera_frame_parameters_get_color_temperature](./ar_camera_frame_parameters_get_color_temperature.md)
  Get the white balance correlated color temperature in kelvin.
- [ar_camera_frame_parameters_get_exposure_duration](./ar_camera_frame_parameters_get_exposure_duration.md)
  Get the frame exposure duration.
- [ar_camera_frame_parameters_get_extrinsics](./ar_camera_frame_parameters_get_extrinsics.md)
  Get the camera extrinsics.
- [ar_camera_frame_parameters_get_intrinsics](./ar_camera_frame_parameters_get_intrinsics.md)
  Get the camera intrinsics.
- [ar_camera_frame_parameters_get_mid_exposure_timestamp](./ar_camera_frame_parameters_get_mid_exposure_timestamp.md)
  Get the frame mid exposure timestamp.
- [ar_camera_frame_parameters_is_equal_to_camera_frame_parameters](./ar_camera_frame_parameters_is_equal_to_camera_frame_parameters.md)
  Returns a bool value that indicates whether the two camera frame parameters are equal.
- [ar_camera_frame_provider_create](./ar_camera_frame_provider_create.md)
  Create a camera frame provider.
- [ar_camera_frame_provider_get_required_authorization_type](./ar_camera_frame_provider_get_required_authorization_type.md)
  Get the authorization type required by the camera frame provider.
- [ar_camera_frame_provider_is_supported](./ar_camera_frame_provider_is_supported.md)
  Determine whether this device supports the camera frame provider.
- [ar_camera_frame_provider_set_update_handler](./ar_camera_frame_provider_set_update_handler.md)
  Set the handler for receiving camera frame updates for the given video format.
- [ar_camera_frame_provider_set_update_handler_f](./ar_camera_frame_provider_set_update_handler_f.md)
  Set the function for receiving camera frame updates for the given video format.
- [ar_camera_frame_sample_get_camera_frame_parameters](./ar_camera_frame_sample_get_camera_frame_parameters.md)
  Get the camera frame parameters for this camera frame sample.
- [ar_camera_frame_sample_get_pixel_buffer](./ar_camera_frame_sample_get_pixel_buffer.md)
  Get the `CVPixelBufferRef` for this frame buffer.
- [ar_camera_frame_sample_is_equal_to_camera_frame_sample](./ar_camera_frame_sample_is_equal_to_camera_frame_sample.md)
  Returns a bool value that indicates whether the two camera frame samples are equal.
- [ar_camera_frame_get_frame_sample](./ar_camera_frame_get_frame_sample.md)
  Get the camera frame sample for a given camera position.
- [ARTrackingState](./artrackingstate.md)
  Possible values for position-tracking quality.
- [ar_camera_video_format_get_camera_position](./ar_camera_video_format_get_camera_position.md)
  Get the camera position for this video format.
- [ar_camera_video_format_get_camera_type](./ar_camera_video_format_get_camera_type.md)
  Get the camera type for this video format.
- [ar_camera_video_format_get_frame_size](./ar_camera_video_format_get_frame_size.md)
  Get the frame size for this video format in pixels.
- [ar_camera_video_format_get_pixel_format](./ar_camera_video_format_get_pixel_format.md)
  Get the pixel format for this video format.
- [ar_camera_video_format_is_equal_to_camera_video_format](./ar_camera_video_format_is_equal_to_camera_video_format.md)
  Returns a bool value that indicates whether the two camera video formats are equal.
- [ar_camera_video_formats_enumerate_video_formats](./ar_camera_video_formats_enumerate_video_formats.md)
  Enumerate all supported video formats for this configuration.
- [ar_camera_video_formats_enumerate_video_formats_f](./ar_camera_video_formats_enumerate_video_formats_f.md)
  Enumerates all supported camera video formats for this configuration using a function.
- [ar_camera_video_formats_get_count](./ar_camera_video_formats_get_count.md)
  Get the count of camera video formats in the collection.
### Data functions
- [ar_data_get_bytes](./ar_data_get_bytes.md)
  Get a pointer to the data’s bytes.
- [ar_data_get_length](./ar_data_get_length.md)
  Get the length of the data, in bytes.
### Device anchor functions
- [ar_device_anchor_get_identifier](./ar_device_anchor_get_identifier.md)
  Get the identifier of an anchor.
- [ar_device_anchor_get_origin_from_anchor_transform](./ar_device_anchor_get_origin_from_anchor_transform.md)
  Get the transform from an anchor to the origin coordinate system.
- [ar_device_anchor_get_timestamp](./ar_device_anchor_get_timestamp.md)
  Get the timestamp corresponding to an anchor.
- [ar_device_anchor_is_tracked](./ar_device_anchor_is_tracked.md)
  Determine whether an anchor is tracked.
- [ar_device_anchor_get_tracking_state](./ar_device_anchor_get_tracking_state.md)
  Gets the tracking state of the device anchor.
- [ar_device_anchor_get_origin_from_anchor_transform_with_correction](./ar_device_anchor_get_origin_from_anchor_transform_with_correction.md)
  Get the transform from an anchor to the origin coordinate system.
### Environment lighting estimation functions
- [ar_environment_light_estimation_configuration_create](./ar_environment_light_estimation_configuration_create.md)
  Create an environment light estimation configuration.
- [ar_environment_light_estimation_provider_create](./ar_environment_light_estimation_provider_create.md)
  Create an environment light estimation provider.
- [ar_environment_light_estimation_provider_get_required_authorization_type](./ar_environment_light_estimation_provider_get_required_authorization_type.md)
  Get the authorization type required by the environment light estimation provider.
- [ar_environment_light_estimation_provider_is_supported](./ar_environment_light_estimation_provider_is_supported.md)
  Determines whether this device supports the environment light estimation provider.
- [ar_environment_light_estimation_provider_set_update_handler](./ar_environment_light_estimation_provider_set_update_handler.md)
  Set the handler for receiving environment light estimation updates.
- [ar_environment_light_estimation_provider_set_update_handler_f](./ar_environment_light_estimation_provider_set_update_handler_f.md)
  Set the function for receiving environment light estimation updates.
### Environment probe functions
- [ar_environment_probe_anchor_get_environment_texture](./ar_environment_probe_anchor_get_environment_texture.md)
  Get the environment texture of an environment probe anchor.
- [ar_environment_probe_anchor_get_identifier](./ar_environment_probe_anchor_get_identifier.md)
  Get the identifier of an anchor.
- [ar_environment_probe_anchor_get_origin_from_anchor_transform](./ar_environment_probe_anchor_get_origin_from_anchor_transform.md)
  Get the transform from an anchor to the origin coordinate system.
- [ar_environment_probe_anchor_get_timestamp](./ar_environment_probe_anchor_get_timestamp.md)
  Get the timestamp corresponding to an anchor.
- [ar_environment_probe_anchor_is_equal_to_environment_probe_anchor](./ar_environment_probe_anchor_is_equal_to_environment_probe_anchor.md)
  Returns a bool value that indicates whether the two environment probe anchors are equal.
- [ar_environment_probe_anchors_enumerate_anchors](./ar_environment_probe_anchors_enumerate_anchors.md)
  Enumerates a collection of environment probe anchors.
- [ar_environment_probe_anchors_enumerate_anchors_f](./ar_environment_probe_anchors_enumerate_anchors_f.md)
  Enumerates a collection of environment probe anchors using a function.
- [ar_environment_probe_anchors_get_count](./ar_environment_probe_anchors_get_count.md)
  Get the count of environment probe anchors in the collection.
- [ar_environment_probe_anchor_get_origin_from_anchor_transform_with_correction](./ar_environment_probe_anchor_get_origin_from_anchor_transform_with_correction.md)
  Get the transform from an anchor to the origin coordinate system.
### Geometry functions
- [ar_geometry_element_is_equal_to_geometry_element](./ar_geometry_element_is_equal_to_geometry_element.md)
  Returns a bool value that indicates whether the two geometry elements are equal.
- [ar_geometry_source_is_equal_to_geometry_source](./ar_geometry_source_is_equal_to_geometry_source.md)
  Returns a bool value that indicates whether the two geometry sources are equal.
### Hand anchor functions
- [ar_hand_anchor_get_hand_skeleton](./ar_hand_anchor_get_hand_skeleton.md)
  Get the hand skeleton of a hand anchor.
- [ar_hand_anchor_get_identifier](./ar_hand_anchor_get_identifier.md)
  Get the identifier of an anchor.
- [ar_hand_anchor_get_origin_from_anchor_transform](./ar_hand_anchor_get_origin_from_anchor_transform.md)
  Get the transform from an anchor to the origin coordinate system.
- [ar_hand_anchor_get_timestamp](./ar_hand_anchor_get_timestamp.md)
  Get the timestamp corresponding to an anchor.
- [ar_hand_anchor_is_equal_to_hand_anchor](./ar_hand_anchor_is_equal_to_hand_anchor.md)
  Returns a bool value that indicates whether the two hand anchors are equal.
- [ar_hand_anchor_is_tracked](./ar_hand_anchor_is_tracked.md)
  Determine whether an anchor is tracked.
### Hand skeleton functions
- [ar_hand_skeleton_create](./ar_hand_skeleton_create.md)
  Create a hand skeleton in a neutral pose that allows access to constants like joint indices, names, counts, etc.
- [ar_hand_skeleton_enumerate_joints](./ar_hand_skeleton_enumerate_joints.md)
  Enumerate the names of joints in an `ar_hand_skeleton_t` using an enumeration block.
- [ar_hand_skeleton_enumerate_joints_f](./ar_hand_skeleton_enumerate_joints_f.md)
  Enumerates the joints in an `ar_hand_skeleton_t` using a function.
- [ar_hand_skeleton_get_joint_count](./ar_hand_skeleton_get_joint_count.md)
  Get the total number of joints in the hand skeleton.
- [ar_hand_skeleton_get_joint_named](./ar_hand_skeleton_get_joint_named.md)
  Get a joint by it’s name from the hand skeleton.
- [ar_hand_skeleton_is_equal_to_hand_skeleton](./ar_hand_skeleton_is_equal_to_hand_skeleton.md)
  Returns a bool value that indicates whether the two hand skeletons are equal.
### Hand tracking functions
- [ar_hand_tracking_provider_query_anchors_at_timestamp](./ar_hand_tracking_provider_query_anchors_at_timestamp.md)
  The provided `timestamp`when rendering should be obtained from `cp_frame_timing_get_trackable_anchor_time`.
### Identifier functions
- [ar_identifiers_enumerate_identifiers](./ar_identifiers_enumerate_identifiers.md)
  Enumerate a collection of identifiers.
- [ar_identifiers_enumerate_identifiers_f](./ar_identifiers_enumerate_identifiers_f.md)
  Enumerates a collection of identifiers using a function.
- [ar_identifiers_get_count](./ar_identifiers_get_count.md)
  Get the count of identifiers in a collection.
- [ar_identifiers_is_equal_to_identifiers](./ar_identifiers_is_equal_to_identifiers.md)
  Returns a bool value that indicates whether the two collections of identifiers are equal.
### Image anchor functions
- [ar_image_anchor_get_identifier](./ar_image_anchor_get_identifier.md)
  Get the identifier of an anchor.
- [ar_image_anchor_get_origin_from_anchor_transform](./ar_image_anchor_get_origin_from_anchor_transform.md)
  Get the transform from an anchor to the origin coordinate system.
- [ar_image_anchor_get_timestamp](./ar_image_anchor_get_timestamp.md)
  Get the timestamp corresponding to an anchor.
- [ar_image_anchor_is_equal_to_image_anchor](./ar_image_anchor_is_equal_to_image_anchor.md)
  Returns a bool value that indicates whether the two image anchors are equal.
- [ar_image_anchor_is_tracked](./ar_image_anchor_is_tracked.md)
  Determine whether an anchor is tracked.
### Mesh anchor functions
- [ar_mesh_anchor_get_identifier](./ar_mesh_anchor_get_identifier.md)
  Get the identifier of an anchor.
- [ar_mesh_anchor_get_origin_from_anchor_transform](./ar_mesh_anchor_get_origin_from_anchor_transform.md)
  Get the transform from an anchor to the origin coordinate system.
- [ar_mesh_anchor_get_timestamp](./ar_mesh_anchor_get_timestamp.md)
  Get the timestamp corresponding to an anchor.
- [ar_mesh_anchor_is_equal_to_mesh_anchor](./ar_mesh_anchor_is_equal_to_mesh_anchor.md)
  Returns a bool value that indicates whether the two mesh anchors are equal.
### Mesh geometry functions
- [ar_mesh_geometries_enumerate_geometries](./ar_mesh_geometries_enumerate_geometries.md)
  Enumerate a collection of mesh geometries.
- [ar_mesh_geometries_enumerate_geometries_f](./ar_mesh_geometries_enumerate_geometries_f.md)
  Enumerates a collection of mesh geometries using a function.
- [ar_mesh_geometries_get_count](./ar_mesh_geometries_get_count.md)
  Get the count of mesh geometries in a collection.
- [ar_mesh_geometry_is_equal_to_mesh_geometry](./ar_mesh_geometry_is_equal_to_mesh_geometry.md)
  Returns a bool value that indicates whether the two mesh geometries are equal.
### Object anchor functions
- [ar_object_anchor_get_bounding_box](./ar_object_anchor_get_bounding_box.md)
  Get bounding box for the object. Aligned with frame defining object’s center and axes.
- [ar_object_anchor_get_identifier](./ar_object_anchor_get_identifier.md)
  Get the identifier of an anchor.
- [ar_object_anchor_get_origin_from_anchor_transform](./ar_object_anchor_get_origin_from_anchor_transform.md)
  Get the transform from an anchor to the origin coordinate system.
- [ar_object_anchor_get_reference_object](./ar_object_anchor_get_reference_object.md)
  Get the underlying tracked reference object from an object anchor.
- [ar_object_anchor_get_timestamp](./ar_object_anchor_get_timestamp.md)
  Get the timestamp corresponding to an anchor.
- [ar_object_anchor_is_equal_to_object_anchor](./ar_object_anchor_is_equal_to_object_anchor.md)
  Returns a bool value that indicates whether the two object anchors are equal.
- [ar_object_anchor_is_tracked](./ar_object_anchor_is_tracked.md)
  Determine whether an anchor is tracked.
- [ar_object_anchors_enumerate_anchors](./ar_object_anchors_enumerate_anchors.md)
  Enumerates a collection of object anchors.
- [ar_object_anchors_enumerate_anchors_f](./ar_object_anchors_enumerate_anchors_f.md)
  Enumerates a collection of object anchors using a function.
- [ar_object_anchors_get_count](./ar_object_anchors_get_count.md)
  Get the count of object anchors in a collection.
- [ar_object_anchor_get_origin_from_anchor_transform_with_correction](./ar_object_anchor_get_origin_from_anchor_transform_with_correction.md)
  Get the transform from an anchor to the origin coordinate system.
### Object bounding box functions
- [ar_object_axis_aligned_bounding_box_get_center](./ar_object_axis_aligned_bounding_box_get_center.md)
  Get center coordinates for the bounding box.
- [ar_object_axis_aligned_bounding_box_get_extent](./ar_object_axis_aligned_bounding_box_get_extent.md)
  Get extent for the bounding box.
- [ar_object_axis_aligned_bounding_box_get_max](./ar_object_axis_aligned_bounding_box_get_max.md)
  Get maximum X, Y, Z coordinates for the bounding box.
- [ar_object_axis_aligned_bounding_box_get_min](./ar_object_axis_aligned_bounding_box_get_min.md)
  Get minimum X, Y, Z coordinates for the bounding box.
- [ar_object_axis_aligned_bounding_box_is_equal_to_bounding_box](./ar_object_axis_aligned_bounding_box_is_equal_to_bounding_box.md)
  Returns a bool value that indicates whether the two bounding boxes are equal.
### Object tracking configuration functions
- [ar_object_tracking_configuration_add_reference_objects](./ar_object_tracking_configuration_add_reference_objects.md)
  Add reference objects to the set of objects to be tracked. Object tracking will run without any reference objects, but will detect nothing.
- [ar_object_tracking_configuration_create](./ar_object_tracking_configuration_create.md)
  Create an object tracking configuration.
- [ar_object_tracking_configuration_get_detection_rate](./ar_object_tracking_configuration_get_detection_rate.md)
  Get the frequency to be configured for running object detection.
- [ar_object_tracking_configuration_get_maximum_instances_per_reference_object](./ar_object_tracking_configuration_get_maximum_instances_per_reference_object.md)
  Get the number to be configured for the maximum number of instances of each reference object type to track.
- [ar_object_tracking_configuration_get_maximum_trackable_instances](./ar_object_tracking_configuration_get_maximum_trackable_instances.md)
  Get the number to be configured for the maximum number of reference object instances to track.
- [ar_object_tracking_configuration_get_moving_object_tracking_rate](./ar_object_tracking_configuration_get_moving_object_tracking_rate.md)
  Get the frequency to be configured for object tracking to run for a moving object.
- [ar_object_tracking_configuration_get_stationary_object_tracking_rate](./ar_object_tracking_configuration_get_stationary_object_tracking_rate.md)
  Get the frequency to be configured for object tracking to run for a stationary object.
- [ar_object_tracking_configuration_set_detection_rate](./ar_object_tracking_configuration_set_detection_rate.md)
  Set the frequency at which object detection runs until it starts to track an object.
- [ar_object_tracking_configuration_set_maximum_instances_per_reference_object](./ar_object_tracking_configuration_set_maximum_instances_per_reference_object.md)
  Set the maximum number of instances of any one reference object type that can be tracked.
- [ar_object_tracking_configuration_set_maximum_trackable_instances](./ar_object_tracking_configuration_set_maximum_trackable_instances.md)
  Set the total number of instances of reference objects that can be tracked at one time.
- [ar_object_tracking_configuration_set_moving_object_tracking_rate](./ar_object_tracking_configuration_set_moving_object_tracking_rate.md)
  Set the frequency at which object tracking runs for a moving object that is detected.
- [ar_object_tracking_configuration_set_stationary_object_tracking_rate](./ar_object_tracking_configuration_set_stationary_object_tracking_rate.md)
  Set the frequency at which object tracking runs for a stationary object that is detected.
### Object tracking provider functions
- [ar_object_tracking_provider_copy_all_object_anchors](./ar_object_tracking_provider_copy_all_object_anchors.md)
  Copy all object anchors.
- [ar_object_tracking_provider_create](./ar_object_tracking_provider_create.md)
  Create an object tracking provider.
- [ar_object_tracking_provider_get_required_authorization_type](./ar_object_tracking_provider_get_required_authorization_type.md)
  Get the authorization type required by the object tracking provider.
- [ar_object_tracking_provider_is_supported](./ar_object_tracking_provider_is_supported.md)
  Determine whether this device supports the object tracking provider.
- [ar_object_tracking_provider_set_update_handler](./ar_object_tracking_provider_set_update_handler.md)
  Set the handler for receiving object tracking updates.
- [ar_object_tracking_provider_set_update_handler_f](./ar_object_tracking_provider_set_update_handler_f.md)
  Set the handler for receiving object tracking updates.
- [ar_object_tracking_error_code_t](./ar_object_tracking_error_code_t.md)
  Error codes that describe object tracking failures.
### Plane anchor functions
- [ar_plane_detection_provider_copy_all_plane_anchors](./ar_plane_detection_provider_copy_all_plane_anchors.md)
  Copy all plane anchors.
- [ar_plane_extent_is_equal_to_plane_extent](./ar_plane_extent_is_equal_to_plane_extent.md)
  Returns a bool value that indicates whether the two plane extents are equal.
- [ar_plane_geometry_is_equal_to_plane_geometry](./ar_plane_geometry_is_equal_to_plane_geometry.md)
  Returns a bool value that indicates whether the two plane geometries are equal.
- [ar_plane_anchor_get_identifier](./ar_plane_anchor_get_identifier.md)
  Get the identifier of an anchor.
- [ar_plane_anchor_get_origin_from_anchor_transform](./ar_plane_anchor_get_origin_from_anchor_transform.md)
  Get the transform from an anchor to the origin coordinate system.
- [ar_plane_anchor_get_timestamp](./ar_plane_anchor_get_timestamp.md)
  Get the timestamp corresponding to an anchor.
- [ar_plane_anchor_is_equal_to_plane_anchor](./ar_plane_anchor_is_equal_to_plane_anchor.md)
  Returns a bool value that indicates whether the two plane anchors are equal.
- [ar_plane_anchor_get_origin_from_anchor_transform_with_correction](./ar_plane_anchor_get_origin_from_anchor_transform_with_correction.md)
  Get the transform from an anchor to the origin coordinate system.
- [ar_plane_alignment_t](./ar_plane_alignment_t.md)
  Option set describing possible orientation alignments of a detected plane.
### Reference image functions
- [ar_reference_image_get_resource_group_name](./ar_reference_image_get_resource_group_name.md)
  Get a reference image’s resource group name.
- [ar_reference_image_is_equal_to_reference_image](./ar_reference_image_is_equal_to_reference_image.md)
  Returns a bool value that indicates whether the two reference images are equal.
### Reference object functions
- [ar_reference_object_get_identifier](./ar_reference_object_get_identifier.md)
  Get identifier for the reference object.
- [ar_reference_object_get_input_file_path](./ar_reference_object_get_input_file_path.md)
  Get the input file path used to load the reference object.
- [ar_reference_object_get_name](./ar_reference_object_get_name.md)
  Get a reference object’s name.
- [ar_reference_object_get_usdz_file_path](./ar_reference_object_get_usdz_file_path.md)
  Get path to a copy of the USDZ file for the object, if the object has one.
- [ar_reference_object_is_equal_to_reference_object](./ar_reference_object_is_equal_to_reference_object.md)
  Returns a bool value that indicates whether the two reference objects are equal.
### Room anchor functions
- [ar_room_anchor_contains_point](./ar_room_anchor_contains_point.md)
  Determine if the room contains the given point.
- [ar_room_anchor_get_geometry](./ar_room_anchor_get_geometry.md)
  Get a mesh representation of the room.
- [ar_room_anchor_get_identifier](./ar_room_anchor_get_identifier.md)
  Get the identifier of a room anchor.
- [ar_room_anchor_get_mesh_anchor_identifiers](./ar_room_anchor_get_mesh_anchor_identifiers.md)
  Get the identifiers of all scene reconstruction mesh anchors in a room anchor.
- [ar_room_anchor_get_mesh_geometries_for_classification](./ar_room_anchor_get_mesh_geometries_for_classification.md)
  Get disjoint mesh geometries of a given classification.
- [ar_room_anchor_get_origin_from_anchor_transform](./ar_room_anchor_get_origin_from_anchor_transform.md)
  Get the transform from a room anchor to the origin coordinate system.
- [ar_room_anchor_get_plane_anchor_identifiers](./ar_room_anchor_get_plane_anchor_identifiers.md)
  Get the identifiers of all plane anchors in a room anchor.
- [ar_room_anchor_get_timestamp](./ar_room_anchor_get_timestamp.md)
  Get the timestamp corresponding to when the room anchor was updated.
- [ar_room_anchor_is_current_room](./ar_room_anchor_is_current_room.md)
  Determine if the room anchor represents the current room the person is in.
- [ar_room_anchor_is_equal_to_room_anchor](./ar_room_anchor_is_equal_to_room_anchor.md)
  Returns a bool value that indicates whether the two room anchors are equal.
- [ar_room_anchor_get_mesh_geometries_for_surface_classification](./ar_room_anchor_get_mesh_geometries_for_surface_classification.md)
  Get disjoint mesh geometries of a given surface classification.
- [ar_room_anchors_enumerate_anchors](./ar_room_anchors_enumerate_anchors.md)
  Enumerate a collection of room anchors.
- [ar_room_anchors_enumerate_anchors_f](./ar_room_anchors_enumerate_anchors_f.md)
  Enumerates a collection of room anchors using a function.
- [ar_room_anchors_get_count](./ar_room_anchors_get_count.md)
  Get the count of room anchors in a collection.
- [ar_room_anchor_get_origin_from_anchor_transform_with_correction](./ar_room_anchor_get_origin_from_anchor_transform_with_correction.md)
  Get the transform from a room anchor to the origin coordinate system.
### Room tracking functions
- [ar_room_tracking_configuration_create](./ar_room_tracking_configuration_create.md)
  Create a room tracking configuration.
- [ar_room_tracking_provider_copy_all_room_anchors](./ar_room_tracking_provider_copy_all_room_anchors.md)
  Copy all room anchors.
- [ar_room_tracking_provider_copy_current_room_anchor](./ar_room_tracking_provider_copy_current_room_anchor.md)
  Copy the room anchor that the person is currently inside.
- [ar_room_tracking_provider_create](./ar_room_tracking_provider_create.md)
  Create a room tracking provider.
- [ar_room_tracking_provider_get_required_authorization_type](./ar_room_tracking_provider_get_required_authorization_type.md)
  Get the authorization type required by the room tracking provider.
- [ar_room_tracking_provider_is_supported](./ar_room_tracking_provider_is_supported.md)
  Determine whether this device supports the room tracking provider.
- [ar_room_tracking_provider_set_update_handler](./ar_room_tracking_provider_set_update_handler.md)
  Set the handler for receiving room tracking updates.
- [ar_room_tracking_provider_set_update_handler_f](./ar_room_tracking_provider_set_update_handler_f.md)
  Set the function for receiving room tracking updates.
### Scene reconstruction functions
- [ar_scene_reconstruction_provider_copy_all_mesh_anchors](./ar_scene_reconstruction_provider_copy_all_mesh_anchors.md)
  Copy all mesh anchors.
### Skeleton joint functions
- [ar_skeleton_joint_get_anchor_from_joint_transform](./ar_skeleton_joint_get_anchor_from_joint_transform.md)
  Get the transform from the joint to the anchor’s coordinate system.
- [ar_skeleton_joint_get_index](./ar_skeleton_joint_get_index.md)
  Get a joint’s index.
- [ar_skeleton_joint_get_parent](./ar_skeleton_joint_get_parent.md)
  Get a joint’s parent joint.
- [ar_skeleton_joint_get_parent_from_joint_transform](./ar_skeleton_joint_get_parent_from_joint_transform.md)
  Get the transform from the joint to its parent joint’s coordinate system.
- [ar_skeleton_joint_is_equal_to_skeleton_joint](./ar_skeleton_joint_is_equal_to_skeleton_joint.md)
  Returns a bool value that indicates whether the two skeleton joints are equal.
- [ar_skeleton_joint_is_tracked](./ar_skeleton_joint_is_tracked.md)
  Determine whether a joint is tracked.
- [ar_skeleton_joint_get_anchor_from_joint_transform_with_correction](./ar_skeleton_joint_get_anchor_from_joint_transform_with_correction.md)
  Get the transform from the joint to the anchor’s coordinate system.
- [ar_skeleton_joint_get_parent_from_joint_transform_with_correction](./ar_skeleton_joint_get_parent_from_joint_transform_with_correction.md)
  Get the transform from the joint to its parent joint’s coordinate system.
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
- [ar_world_tracking_provider_copy_all_world_anchors_f](./ar_world_tracking_provider_copy_all_world_anchors_f.md)
  Copies all known world anchors from the world tracking provider asynchronously.

## See Also

### Objective-C compatibility
- [ARKit Data Types](./arkit-data-types.md)
- [Objective-C compatibility](./objective-c-compatibility.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkit-functions)*