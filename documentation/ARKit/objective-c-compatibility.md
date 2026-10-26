# Objective-C compatibility

**Framework**: ARKit  
**Role**: API Collection

## Topics

### Objective-C compatibility types
- [protocol OS_ar_anchor](./os_ar_anchor.md)
  The identity, location, and orientation of an object in world space.
- [protocol OS_ar_trackable_anchor](./os_ar_trackable_anchor.md)
  An anchor that can gain and lose its tracking state over the course of a session.
- [protocol OS_ar_authorization_result](./os_ar_authorization_result.md)
  An authorization result.
- [protocol OS_ar_authorization_results](./os_ar_authorization_results.md)
  A collection of authorization results.
- [protocol OS_ar_data_provider](./os_ar_data_provider.md)
  A source of live data from ARKit.
- [protocol OS_ar_device_anchor](./os_ar_device_anchor.md)
  The position and orientation of Apple Vision Pro.
- [protocol OS_ar_error](./os_ar_error.md)
  An error reported by ARKit.
- [protocol OS_ar_data_providers](./os_ar_data_providers.md)
  A source of live data from ARKit.
- [protocol OS_ar_geometry_element](./os_ar_geometry_element.md)
  A container for vertex indices of lines or triangles.
- [protocol OS_ar_geometry_source](./os_ar_geometry_source.md)
  A container for geometrical vector data.
- [protocol OS_ar_hand_anchor](./os_ar_hand_anchor.md)
  A hand’s position in a person’s surroundings.
- [protocol OS_ar_hand_skeleton](./os_ar_hand_skeleton.md)
- [protocol OS_ar_hand_tracking_provider](./os_ar_hand_tracking_provider.md)
  A source of live data about the position of a person’s hands and hand joints.
- [protocol OS_ar_hand_tracking_configuration](./os_ar_hand_tracking_configuration.md)
- [protocol OS_ar_image_tracking_configuration](./os_ar_image_tracking_configuration.md)
- [protocol OS_ar_plane_detection_configuration](./os_ar_plane_detection_configuration.md)
- [protocol OS_ar_plane_extent](./os_ar_plane_extent.md)
  The size of a plane.
- [protocol OS_ar_reference_images](./os_ar_reference_images.md)
  A collection of reference images.
- [protocol OS_ar_scene_reconstruction_configuration](./os_ar_scene_reconstruction_configuration.md)
- [protocol OS_ar_session](./os_ar_session.md)
  The main entry point for receiving data from ARKit.
- [protocol OS_ar_world_tracking_configuration](./os_ar_world_tracking_configuration.md)
- [protocol OS_ar_image_anchor](./os_ar_image_anchor.md)
  A 2D image’s position in a person’s surroundings.
- [protocol OS_ar_image_anchors](./os_ar_image_anchors.md)
  A collection of image anchors.
- [protocol OS_ar_image_tracking_provider](./os_ar_image_tracking_provider.md)
  A source of live data about a 2D image’s position in a person’s surroundings.
- [protocol OS_ar_mesh_anchor](./os_ar_mesh_anchor.md)
  A source of live data about a 2D image’s position in a person’s surroundings.
- [protocol OS_ar_mesh_anchors](./os_ar_mesh_anchors.md)
  A collection of mech anchors.
- [protocol OS_ar_mesh_geometry](./os_ar_mesh_geometry.md)
  The shapes that make up a mesh anchor.
- [protocol OS_ar_plane_anchor](./os_ar_plane_anchor.md)
  An anchor that represents horizontal and vertical planes.
- [protocol OS_ar_plane_anchors](./os_ar_plane_anchors.md)
  A collection of plane anchors.
- [protocol OS_ar_plane_detection_provider](./os_ar_plane_detection_provider.md)
  A source of live data about planes in a person’s surroundings.
- [protocol OS_ar_plane_geometry](./os_ar_plane_geometry.md)
  The geometry of a plane anchor.
- [protocol OS_ar_reference_image](./os_ar_reference_image.md)
  A 2D image the system uses as a reference to find the same image in a person’s surroundings.
- [protocol OS_ar_scene_reconstruction_provider](./os_ar_scene_reconstruction_provider.md)
  A source of live data about the shape of a person’s surroundings.
- [protocol OS_ar_skeleton_joint](./os_ar_skeleton_joint.md)
- [protocol OS_ar_world_anchor](./os_ar_world_anchor.md)
  A fixed location in a person’s surroundings.
- [protocol OS_ar_world_anchors](./os_ar_world_anchors.md)
  A collection of world anchors.
- [protocol OS_ar_world_tracking_provider](./os_ar_world_tracking_provider.md)
  A source of live data about the device pose and anchors in a person’s surroundings.
- [protocol OS_ar_barcode_anchor](./os_ar_barcode_anchor.md)
- [protocol OS_ar_barcode_anchors](./os_ar_barcode_anchors.md)
- [protocol OS_ar_barcode_detection_callbacks](./os_ar_barcode_detection_callbacks.md)
- [protocol OS_ar_barcode_detection_configuration](./os_ar_barcode_detection_configuration.md)
- [protocol OS_ar_barcode_detection_provider](./os_ar_barcode_detection_provider.md)
- [protocol OS_ar_camera_frame](./os_ar_camera_frame.md)
- [protocol OS_ar_camera_frame_parameters](./os_ar_camera_frame_parameters.md)
- [protocol OS_ar_camera_frame_provider](./os_ar_camera_frame_provider.md)
- [protocol OS_ar_camera_frame_sample](./os_ar_camera_frame_sample.md)
- [protocol OS_ar_camera_video_format](./os_ar_camera_video_format.md)
- [protocol OS_ar_camera_video_formats](./os_ar_camera_video_formats.md)
- [protocol OS_ar_data](./os_ar_data.md)
- [protocol OS_ar_environment_light_estimation_configuration](./os_ar_environment_light_estimation_configuration.md)
- [protocol OS_ar_environment_light_estimation_provider](./os_ar_environment_light_estimation_provider.md)
- [protocol OS_ar_environment_probe_anchor](./os_ar_environment_probe_anchor.md)
- [protocol OS_ar_environment_probe_anchors](./os_ar_environment_probe_anchors.md)
- [protocol OS_ar_identifiers](./os_ar_identifiers.md)
- [protocol OS_ar_mesh_geometries](./os_ar_mesh_geometries.md)
- [protocol OS_ar_object_anchor](./os_ar_object_anchor.md)
- [protocol OS_ar_object_anchors](./os_ar_object_anchors.md)
- [protocol OS_ar_object_axis_aligned_bounding_box](./os_ar_object_axis_aligned_bounding_box.md)
- [protocol OS_ar_object_tracking_configuration](./os_ar_object_tracking_configuration.md)
- [protocol OS_ar_object_tracking_provider](./os_ar_object_tracking_provider.md)
- [protocol OS_ar_reference_object](./os_ar_reference_object.md)
- [protocol OS_ar_reference_objects](./os_ar_reference_objects.md)
- [protocol OS_ar_room_anchor](./os_ar_room_anchor.md)
- [protocol OS_ar_room_anchors](./os_ar_room_anchors.md)
- [protocol OS_ar_room_tracking_configuration](./os_ar_room_tracking_configuration.md)
- [protocol OS_ar_room_tracking_provider](./os_ar_room_tracking_provider.md)
- [protocol OS_ar_accessories](./os_ar_accessories.md)
  A collection of accessories.
- [protocol OS_ar_accessory](./os_ar_accessory.md)
  An accessory that can be tracked in the physical environment, such as a game controller or stylus.
- [protocol OS_ar_accessory_anchor](./os_ar_accessory_anchor.md)
  An anchor that represents an accessory.
- [protocol OS_ar_accessory_anchors](./os_ar_accessory_anchors.md)
  A collection of accessory anchors.
- [protocol OS_ar_accessory_tracking_configuration](./os_ar_accessory_tracking_configuration.md)
  Configuration for accessory tracking.
- [protocol OS_ar_accessory_tracking_provider](./os_ar_accessory_tracking_provider.md)
  A data provider for accessory tracking.
- [protocol OS_ar_camera_frame_samples](./os_ar_camera_frame_samples.md)
  A collection of camera frame samples.
- [protocol OS_ar_camera_region_anchor](./os_ar_camera_region_anchor.md)
  An anchor representing a camera region with enhanced image processing.
- [protocol OS_ar_camera_region_anchors](./os_ar_camera_region_anchors.md)
  A collection of camera region anchors.
- [protocol OS_ar_camera_region_configuration](./os_ar_camera_region_configuration.md)
  Configuration for camera region processing.
- [protocol OS_ar_camera_region_provider](./os_ar_camera_region_provider.md)
  A data provider for camera region processing.
- [protocol OS_ar_coordinate_space_data](./os_ar_coordinate_space_data.md)
  Data for sharing coordinate space information between participants.
- [protocol OS_ar_device](./os_ar_device.md)
  Represents a physical device that a session can be run on.
- [protocol OS_ar_shared_coordinate_space_configuration](./os_ar_shared_coordinate_space_configuration.md)
  Configuration for the shared coordinate space provider.
- [protocol OS_ar_shared_coordinate_space_provider](./os_ar_shared_coordinate_space_provider.md)
  A data provider for shared coordinate spaces across participants.
- [protocol OS_ar_stereo_properties_configuration](./os_ar_stereo_properties_configuration.md)
  Configuration for the stereo properties provider.
- [protocol OS_ar_stereo_properties_provider](./os_ar_stereo_properties_provider.md)
  A data provider that provides stereo viewpoint properties.
- [protocol OS_ar_strings](./os_ar_strings.md)
  A collection of strings.
- [protocol OS_ar_viewpoint_properties](./os_ar_viewpoint_properties.md)
  Properties describing the stereo viewpoints of the device.
- [protocol OS_ar_field_of_view](./os_ar_field_of_view.md)
  Field of view specification.
- [protocol OS_ar_field_of_view_anchor](./os_ar_field_of_view_anchor.md)
  An anchor representing a set of field of view boundary polygon points in immersive space.
- [protocol OS_ar_polygon_points](./os_ar_polygon_points.md)
  A collection of 2D polygon points.
- [protocol OS_ar_reference_object_configuration](./os_ar_reference_object_configuration.md)
  Defines a configuration for an individual reference object.
- [protocol OS_ar_visual_fidelity_configuration](./os_ar_visual_fidelity_configuration.md)
  Configuration object for visual fidelity monitoring.
- [protocol OS_ar_visual_fidelity_data](./os_ar_visual_fidelity_data.md)
  Visual fidelity data object containing device fit and field of view validation results.
- [protocol OS_ar_visual_fidelity_provider](./os_ar_visual_fidelity_provider.md)
  Data provider for visual fidelity monitoring.
- [var AR_OBJECT_USE_OBJC: Int32](./ar_object_use_objc.md)
- [AR_ASSUME_NONNULL_BEGIN](./ar_assume_nonnull_begin.md)
- [AR_ASSUME_NONNULL_END](./ar_assume_nonnull_end.md)
- [AR_EXTERN](./ar_extern.md)
- [AR_MT_UNSAFE](./ar_mt_unsafe.md)
- [AR_OBJECT_DECL](./ar_object_decl.md)
- [AR_OBJECT_DECL_SUBCLASS](./ar_object_decl_subclass.md)
- [AR_OBJECT_RETURNS_RETAINED](./ar_object_returns_retained.md)
- [AR_REFINED_FOR_SWIFT](./ar_refined_for_swift.md)
- [AR_SWIFT_SENDABLE](./ar_swift_sendable.md)
- [ar_release](./ar_release-c.macro.md)
- [ar_retain](./ar_retain-c.macro.md)

## See Also

### Objective-C compatibility
- [ARKit Functions](./arkit-functions.md)
- [ARKit Data Types](./arkit-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/objective-c-compatibility)*