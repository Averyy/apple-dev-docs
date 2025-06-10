# ARKit in visionOS C API

**Framework**: ARKit

Integrate ARKit with low-level libraries and functionality.

#### Overview

ARKit in visionOS includes a full C API for compatibility with C and Objective-C apps and frameworks.

## Topics

### Sessions
- [ar_session_t](ar_session_t.md)
  The main entry point for receiving data from ARKit.
- [ar_session_create](ar_session_create.md)
  Creates a new session.
- [ar_session_query_authorization_results](ar_session_query_authorization_results.md)
  Checks whether the current session is authorized for particular authorization types without requesting authorization.
- [ar_session_query_authorization_results_f](ar_session_query_authorization_results_f.md)
  Checks whether the current session is authorized for particular authorization types without requesting authorization.
- [ar_session_request_authorization](ar_session_request_authorization.md)
  Requests authorization from the user to use the specified kinds of ARKit data.
- [ar_session_request_authorization_f](ar_session_request_authorization_f.md)
  Requests authorization from the user to use the specified kinds of ARKit data.
- [ar_session_run](ar_session_run.md)
  Runs a session with the data providers you supply.
- [ar_session_set_authorization_update_handler](ar_session_set_authorization_update_handler.md)
  Sets the handler for receiving updates in authorization status for a specific authorization type.
- [ar_session_set_authorization_update_handler_f](ar_session_set_authorization_update_handler_f.md)
  Sets the handler for receiving updates in authorization status for a specific authorization type.
- [ar_session_set_data_provider_state_change_handler](ar_session_set_data_provider_state_change_handler.md)
  Sets the handler for responding to a change in the state of one or more data providers.
- [ar_session_set_data_provider_state_change_handler_f](ar_session_set_data_provider_state_change_handler_f.md)
  Sets the handler for responding to a change in the state of one or more data providers.
- [ar_session_data_provider_state_change_handler_t](ar_session_data_provider_state_change_handler_t.md)
  A handler for receiving updates to data provider states.
- [ar_session_stop](ar_session_stop.md)
  Stops a session.
### Memory Management
- [ar_release](ar_release-c.func.md)
  Releases a reference count on an ARKit object.
- [ar_retain](ar_retain-c.func.md)
  Adds a reference count to an ARKit object.
### Authorization
- [ar_authorization_status_t](ar_authorization_status_t.md)
  The authorization states for a type of ARKit data.
- [ARKitSession.AuthorizationStatus](arkitsession/authorizationstatus.md)
  The authorization states for a type of ARKit data.
- [ar_authorization_type_t](ar_authorization_type_t.md)
  The authorization types you can request from ARKit.
- [ar_authorization_result_get_authorization_type](ar_authorization_result_get_authorization_type.md)
  Gets the authorization type associated with an authorization result.
- [ar_authorization_result_get_status](ar_authorization_result_get_status.md)
  Gets the authorization status associated with an authorization result.
- [ar_authorization_results_enumerate_results](ar_authorization_results_enumerate_results.md)
  Enumerates a collection of authorization results.
- [ar_authorization_results_enumerate_results_f](ar_authorization_results_enumerate_results_f.md)
  Enumerates a collection of authorization results.
- [ar_authorization_results_get_count](ar_authorization_results_get_count.md)
  Gets the number of authorization results in a collection.
- [ar_authorization_status_allowed](ar_authorization_status_t/ar_authorization_status_allowed.md)
  Your app has permission to use the associated kind of ARKit data.
- [ar_authorization_status_denied](ar_authorization_status_t/ar_authorization_status_denied.md)
  Your app doesn’t have permission to use the associated kind of ARKit data.
- [ar_authorization_status_not_determined](ar_authorization_status_t/ar_authorization_status_not_determined.md)
  Permission for your app to use the associated kind of ARKit data is undetermined.
- [ar_authorization_result_t](ar_authorization_result_t.md)
  An authorization result.
- [ar_authorization_results_enumerator_t](ar_authorization_results_enumerator_t.md)
  A handler for enumerating a collection of authorization results.
- [ar_authorization_results_handler_t](ar_authorization_results_handler_t.md)
  A handler to call upon completion of an authorization request.
- [ar_authorization_results_t](ar_authorization_results_t.md)
  A collection of authorization results.
- [ar_authorization_update_handler_t](ar_authorization_update_handler_t.md)
  A handler for receiving updates in authorization status for a specific authorization type.
- [ar_authorization_results_handler_function_t](ar_authorization_results_handler_function_t.md)
- [ar_authorization_update_handler_function_t](ar_authorization_update_handler_function_t.md)
- [ar_authorization_results_enumerator_function_t](ar_authorization_results_enumerator_function_t.md)
### Anchors
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
- [ar_trackable_anchor_t](ar_trackable_anchor_t.md)
  An anchor that can gain and lose its tracking state over the course of a session.
- [ar_world_anchor_t](ar_world_anchor_t.md)
  A fixed location in a person’s surroundings.
- [ar_world_anchors_t](ar_world_anchors_t.md)
  A collection of world anchors.
- [ar_world_anchors_enumerator_t](ar_world_anchors_enumerator_t.md)
  A handler for enumerating a collection of world anchors.
- [ar_plane_anchor_t](ar_plane_anchor_t.md)
  An anchor that represents horizontal and vertical planes.
- [ar_plane_anchors_t](ar_plane_anchors_t.md)
  A collection of plane anchors.
- [ar_plane_anchors_enumerator_t](ar_plane_anchors_enumerator_t.md)
  A handler for enumerating a collection of plane anchors.
- [ar_plane_detection_provider_t](ar_plane_detection_provider_t.md)
  A source of live data about planes in a person’s surroundings.
- [ar_hand_skeleton_joint_name_t](ar_hand_skeleton_joint_name_t.md)
  An enumeration that describes hand joint names.
- [ar_hand_anchor_query_status_t](ar_hand_anchor_query_status_t.md)
  An enumeration that describes the status of a hand anchor query.
- [world_tracking_h](world_tracking_h.md)
- [anchor_h](anchor_h.md)
### Data providers
- [ar_data_provider_state_t](ar_data_provider_state_t.md)
  The possible states of a data provider.
- [ar_data_provider_get_required_authorization_type](ar_data_provider_get_required_authorization_type.md)
  The kinds of authorization you need to use a particular data provider type.
- [ar_data_provider_get_state](ar_data_provider_get_state.md)
  Gets the current status of data coming from this provider.
- [ar_data_providers_enumerator_t](ar_data_providers_enumerator_t.md)
  A handler for enumerating a collection of data providers.
- [ar_data_providers_t](ar_data_providers_t.md)
  A collection of data providers.
- [ar_data_providers_add_data_provider](ar_data_providers_add_data_provider.md)
  Adds a data provider to a collection.
- [ar_data_providers_add_data_providers](ar_data_providers_add_data_providers.md)
  Adds multiple data providers to a collection.
- [ar_data_providers_create](ar_data_providers_create.md)
  Creates an empty collection of data providers.
- [ar_data_providers_create_with_data_providers](ar_data_providers_create_with_data_providers.md)
  Creates a collection of data providers that contains the data providers you supply.
- [ar_data_providers_enumerate_data_providers_f](ar_data_providers_enumerate_data_providers_f.md)
  Enumerates a collection of data providers.
- [ar_data_providers_get_count](ar_data_providers_get_count.md)
  Gets the number of data providers in a collection.
- [ar_data_providers_enumerate_data_providers](ar_data_providers_enumerate_data_providers.md)
  Enumerates a collection of data providers.
- [ar_data_providers_remove_data_provider](ar_data_providers_remove_data_provider.md)
  Removes a data provider from a collection.
- [ar_data_providers_remove_data_providers](ar_data_providers_remove_data_providers.md)
  Removes multiple data providers from a collection.
- [ar_data_providers_enumerator_function_t](ar_data_providers_enumerator_function_t.md)
- [ar_session_data_provider_state_change_handler_function_t](ar_session_data_provider_state_change_handler_function_t.md)
- [ar_data_provider_t](ar_data_provider_t.md)
  A source of live data from ARKit.
### Geometry
- [ar_geometry_primitive_type_t](ar_geometry_primitive_type_t.md)
  The kinds of geometry primitives that a geometry element can contain.
- [ar_geometry_element_get_buffer](ar_geometry_element_get_buffer.md)
  Gets a Metal buffer that contains index data that defines the geometry of an object.
- [ar_geometry_element_get_bytes_per_index](ar_geometry_element_get_bytes_per_index.md)
  Gets the number of bytes that represent an index value.
- [ar_geometry_element_get_count](ar_geometry_element_get_count.md)
  Gets the number of primitives in the Metal buffer for a geometry element.
- [ar_geometry_element_get_index_count_per_primitive](ar_geometry_element_get_index_count_per_primitive.md)
  Gets the number of indices for each primitive.
- [ar_geometry_element_get_primitive_type](ar_geometry_element_get_primitive_type.md)
  Gets the kind of primitive, lines or triangles, that a geometry element contains.
- [ar_geometry_source_get_buffer](ar_geometry_source_get_buffer.md)
  Gets a Metal buffer that contains per-vector data for a geometry source.
- [ar_geometry_source_get_components_per_vector](ar_geometry_source_get_components_per_vector.md)
  Gets the number of scalar components in each vector in a geometry source.
- [ar_geometry_source_get_count](ar_geometry_source_get_count.md)
  Gets the number of vectors in a geometry source.
- [ar_geometry_source_get_format](ar_geometry_source_get_format.md)
  Gets the vertex format for data in a geometry source’s buffer.
- [ar_geometry_source_get_offset](ar_geometry_source_get_offset.md)
  Gets the offset, in bytes, from the beginning of a geometry source’s buffer.
- [ar_geometry_source_get_stride](ar_geometry_source_get_stride.md)
  Gets the number of bytes between one vector and another in a geometry source’s buffer.
- [ar_geometry_primitive_type_line](ar_geometry_primitive_type_t/ar_geometry_primitive_type_line.md)
  Two vertices that connect to form a line.
- [ar_geometry_primitive_type_triangle](ar_geometry_primitive_type_t/ar_geometry_primitive_type_triangle.md)
  Three vertices that connect to form a triangle.
- [ar_geometry_element_t](ar_geometry_element_t.md)
  A container for vertex indices of lines or triangles.
- [ar_geometry_source_t](ar_geometry_source_t.md)
  A container for geometrical vector data.
- [ar_mesh_geometry_t](ar_mesh_geometry_t.md)
  The shapes that make up a mesh anchor.
- [ar_mesh_anchors_enumerator_function_t](ar_mesh_anchors_enumerator_function_t.md)
### Plane detection
- [ar_plane_alignment_t](ar_plane_alignment_t.md)
  The kinds of alignment — horizontal or vertical — that a plane anchor can have.
- [ar_plane_classification_t](ar_plane_classification_t.md)
  The kinds of object classification a plane anchor can have.
- [ar_plane_classification_ceiling](ar_plane_classification_t/ar_plane_classification_ceiling.md)
  A ceiling.
- [ar_plane_classification_door](ar_plane_classification_t/ar_plane_classification_door.md)
  A door.
- [ar_plane_classification_floor](ar_plane_classification_t/ar_plane_classification_floor.md)
  A floor.
- [ar_plane_classification_seat](ar_plane_classification_t/ar_plane_classification_seat.md)
  A seat.
- [ar_plane_classification_status_not_available](ar_plane_classification_t/ar_plane_classification_status_not_available.md)
  A plane classification is currently unavailable.
- [ar_plane_classification_status_undetermined](ar_plane_classification_t/ar_plane_classification_status_undetermined.md)
  A plane classification is undetermined.
- [ar_plane_classification_status_unknown](ar_plane_classification_t/ar_plane_classification_status_unknown.md)
  A plane classification isn’t one of the known classes.
- [ar_plane_classification_table](ar_plane_classification_t/ar_plane_classification_table.md)
  A table.
- [ar_plane_classification_wall](ar_plane_classification_t/ar_plane_classification_wall.md)
  A wall.
- [ar_plane_classification_window](ar_plane_classification_t/ar_plane_classification_window.md)
  A window.
- [ar_plane_anchor_get_alignment](ar_plane_anchor_get_alignment.md)
  Gets the alignment — horizontal or vertical — of a plane anchor relative to gravity.
- [ar_plane_anchor_get_geometry](ar_plane_anchor_get_geometry.md)
  Gets the shape of a plane anchor.
- [ar_plane_anchor_get_plane_classification](ar_plane_anchor_get_plane_classification.md)
  Gets the kind of real-world object that ARKit determines the plane anchor might be.
- [ar_plane_anchors_enumerate_anchors](ar_plane_anchors_enumerate_anchors.md)
  Enumerates a collection of plane anchors using the collection of plane anchors and the enumeratin handler you provide.
- [ar_plane_anchors_enumerate_anchors_f](ar_plane_anchors_enumerate_anchors_f.md)
  Enumerates a collection of plane anchors.
- [ar_plane_anchors_get_count](ar_plane_anchors_get_count.md)
  Gets the number of plane anchors in a collection.
- [ar_plane_detection_configuration_t](ar_plane_detection_configuration_t.md)
- [ar_plane_detection_provider_create](ar_plane_detection_provider_create.md)
  Creates a plane detection provider for the types of planes you want to detect.
- [ar_plane_detection_provider_is_supported](ar_plane_detection_provider_is_supported.md)
  Returns a Boolean value that indicates whether the current runtime environment supports plane detection providers.
- [ar_plane_geometry_get_plane_extent](ar_plane_geometry_get_plane_extent.md)
  Gets the size of a plane.
- [ar_plane_geometry_get_mesh_vertices](ar_plane_geometry_get_mesh_vertices.md)
  Gets the vertices in the mesh that describes a plane.
- [ar_plane_geometry_get_mesh_faces](ar_plane_geometry_get_mesh_faces.md)
  Gets the faces in the mesh that describes a plane.
- [ar_plane_detection_provider_get_required_authorization_type](ar_plane_detection_provider_get_required_authorization_type.md)
  Gets the types of authorizations necessary for detecting planes.
- [ar_plane_detection_configuration_create](ar_plane_detection_configuration_create.md)
  Creates a plane detection configuration.
- [ar_plane_detection_configuration_set_alignment](ar_plane_detection_configuration_set_alignment.md)
  Sets the plane alignments that you want the provider to detect.
- [ar_plane_detection_provider_set_update_handler](ar_plane_detection_provider_set_update_handler.md)
  Sets the handler for receiving plane detection updates.
- [ar_plane_detection_provider_set_update_handler_f](ar_plane_detection_provider_set_update_handler_f.md)
  Sets the handler for receiving plane detection updates using the plane detection provider and plane detection update queue you provide.
- [ar_plane_extent_t](ar_plane_extent_t.md)
  The size of a plane.
- [ar_plane_extent_get_height](ar_plane_extent_get_height.md)
  Gets the height of a plane.
- [ar_plane_extent_get_plane_anchor_from_plane_extent_transform](ar_plane_extent_get_plane_anchor_from_plane_extent_transform.md)
  Gets the transform of a plane anchor from its extent transform.
- [ar_plane_extent_get_width](ar_plane_extent_get_width.md)
  Gets the width of a plane.
- [ar_plane_geometry_t](ar_plane_geometry_t.md)
  The geometry of a plane anchor.
- [ar_plane_detection_update_handler_t](ar_plane_detection_update_handler_t.md)
  A handler for receiving updates to plane anchors.
- [ar_plane_anchors_enumerator_function_t](ar_plane_anchors_enumerator_function_t.md)
- [ar_plane_detection_update_handler_function_t](ar_plane_detection_update_handler_function_t.md)
- [ARPlaneClassificationStatus](arplaneclassificationstatus.md)
  Possible states of ARKit’s process for classifying plane anchors.
- [plane_detection_h](plane_detection_h.md)
### World tracking
- [ar_world_anchor_create_with_origin_from_anchor_transform](ar_world_anchor_create_with_origin_from_anchor_transform.md)
  Creates a world anchor from a position and orientation in world space.
- [ar_world_tracking_add_anchor_completion_handler_t](ar_world_tracking_add_anchor_completion_handler_t.md)
  A handler to call upon completion of a request to add a world anchor.
- [ar_world_tracking_remove_anchor_completion_handler_t](ar_world_tracking_remove_anchor_completion_handler_t.md)
  A handler to call upon completion of a request to remove a world anchor.
- [ar_world_tracking_anchor_update_handler_t](ar_world_tracking_anchor_update_handler_t.md)
  A handler for receiving updates to world anchors.
- [ar_world_tracking_configuration_create](ar_world_tracking_configuration_create.md)
  Creates a world tracking configuration.
- [ar_world_anchors_enumerate_anchors](ar_world_anchors_enumerate_anchors.md)
  Enumerates a collection of world anchors.
- [ar_world_anchors_enumerate_anchors_f](ar_world_anchors_enumerate_anchors_f.md)
  Enumerates a collection of world anchors.
- [ar_world_anchors_get_count](ar_world_anchors_get_count.md)
  Gets the number of world anchors in the collection.
- [ar_world_tracking_provider_create](ar_world_tracking_provider_create.md)
  Creates a world tracking provider.
- [ar_world_tracking_provider_is_supported](ar_world_tracking_provider_is_supported.md)
  Returns a Boolean value that indicates whether the current runtime environment supports world tracking providers.
- [ar_world_tracking_provider_query_device_anchor_at_timestamp](ar_world_tracking_provider_query_device_anchor_at_timestamp.md)
  Queries the predicted pose of the current device at a given time.
- [ar_world_tracking_provider_add_anchor](ar_world_tracking_provider_add_anchor.md)
  Adds a world anchor you supply to the set of currently tracked anchors.
- [ar_world_tracking_provider_add_anchor_f](ar_world_tracking_provider_add_anchor_f.md)
  Adds a world anchor you supply to the set of currently tracked anchors.
- [ar_world_tracking_provider_get_required_authorization_type](ar_world_tracking_provider_get_required_authorization_type.md)
  Gets the types of authorizations required to track world anchors.
- [ar_world_tracking_provider_set_anchor_update_handler](ar_world_tracking_provider_set_anchor_update_handler.md)
  Sets the handler for receiving world tracking updates.
- [ar_world_tracking_provider_set_anchor_update_handler_f](ar_world_tracking_provider_set_anchor_update_handler_f.md)
  Sets the handler for receiving world tracking updates.
- [ar_world_tracking_provider_remove_anchor_with_identifier](ar_world_tracking_provider_remove_anchor_with_identifier.md)
  Removes a world anchor from a world tracking provider based on its ID.
- [ar_world_tracking_provider_remove_anchor](ar_world_tracking_provider_remove_anchor.md)
  Removes a world anchor from a world tracking provider.
- [ar_world_tracking_provider_remove_anchor_f](ar_world_tracking_provider_remove_anchor_f.md)
  Removes a world anchor from a world tracking provider.
- [ar_world_tracking_configuration_t](ar_world_tracking_configuration_t.md)
- [ar_device_anchor_t](ar_device_anchor_t.md)
- [ar_device_anchor_create](ar_device_anchor_create.md)
- [ar_device_anchor_query_status_t](ar_device_anchor_query_status_t.md)
- [ar_world_anchors_enumerator_function_t](ar_world_anchors_enumerator_function_t.md)
- [ar_world_tracking_add_anchor_completion_handler_function_t](ar_world_tracking_add_anchor_completion_handler_function_t.md)
- [ar_world_tracking_anchor_update_handler_function_t](ar_world_tracking_anchor_update_handler_function_t.md)
- [ar_world_tracking_remove_anchor_completion_handler_function_t](ar_world_tracking_remove_anchor_completion_handler_function_t.md)
- [ar_world_tracking_provider_t](ar_world_tracking_provider_t.md)
  A source of live data about the device pose and anchors in a person’s surroundings.
- [ar_camera_position_t](ar_camera_position_t.md)
  An enumeration that describes possible camera positions.
- [ar_camera_type_t](ar_camera_type_t.md)
  An enumeration that describes camera types.
- [ar_device_anchor_tracking_state_t](ar_device_anchor_tracking_state_t.md)
  Values that describe the tracking states of a device anchor.
- [ar_world_tracking_error_code_t](ar_world_tracking_error_code_t.md)
  The error codes for errors that world tracking providers throw.
- [ar_session_error_code_t](ar_session_error_code_t.md)
  The error codes for ARKit sessions.
### Scene reconstruction
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
- [ar_mesh_geometry_get_classification](ar_mesh_geometry_get_classification.md)
  Gets the classification of each face in the mesh.
- [ar_mesh_geometry_get_faces](ar_mesh_geometry_get_faces.md)
  Gets the faces of the mesh.
- [ar_mesh_geometry_get_normals](ar_mesh_geometry_get_normals.md)
  Gets the normals of the mesh.
- [ar_mesh_geometry_get_vertices](ar_mesh_geometry_get_vertices.md)
  Gets the vertices of the mesh.
- [ar_scene_reconstruction_provider_t](ar_scene_reconstruction_provider_t.md)
  A source of live data about the shape of a person’s surroundings.
- [ar_scene_reconstruction_update_handler_t](ar_scene_reconstruction_update_handler_t.md)
  A handler for receiving updates to mesh anchors.
- [ar_scene_reconstruction_update_handler_function_t](ar_scene_reconstruction_update_handler_function_t.md)
- [scene_reconstruction_h](scene_reconstruction_h.md)
### Hand tracking
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
- [ar_hand_tracking_provider_get_latest_anchors](ar_hand_tracking_provider_get_latest_anchors.md)
  Fetches the most recent hand anchors for each hand.
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
- [ar_hand_skeleton_joint_name_index_finger_metacarpal](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_index_finger_metacarpal.md)
- [ar_hand_skeleton_joint_name_index_finger_tip](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_index_finger_tip.md)
- [ar_hand_skeleton_joint_name_little_finger_intermediate_base](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_little_finger_intermediate_base.md)
- [ar_hand_skeleton_joint_name_little_finger_intermediate_tip](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_little_finger_intermediate_tip.md)
- [ar_hand_skeleton_joint_name_little_finger_knuckle](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_little_finger_knuckle.md)
- [ar_hand_skeleton_joint_name_little_finger_metacarpal](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_little_finger_metacarpal.md)
- [ar_hand_skeleton_joint_name_little_finger_tip](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_little_finger_tip.md)
- [ar_hand_skeleton_joint_name_middle_finger_intermediate_base](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_middle_finger_intermediate_base.md)
- [ar_hand_skeleton_joint_name_middle_finger_intermediate_tip](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_middle_finger_intermediate_tip.md)
- [ar_hand_skeleton_joint_name_middle_finger_knuckle](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_middle_finger_knuckle.md)
- [ar_hand_skeleton_joint_name_middle_finger_metacarpal](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_middle_finger_metacarpal.md)
- [ar_hand_skeleton_joint_name_middle_finger_tip](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_middle_finger_tip.md)
- [ar_hand_skeleton_joint_name_ring_finger_intermediate_base](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_ring_finger_intermediate_base.md)
- [ar_hand_skeleton_joint_name_ring_finger_intermediate_tip](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_ring_finger_intermediate_tip.md)
- [ar_hand_skeleton_joint_name_ring_finger_knuckle](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_ring_finger_knuckle.md)
- [ar_hand_skeleton_joint_name_ring_finger_metacarpal](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_ring_finger_metacarpal.md)
- [ar_hand_skeleton_joint_name_ring_finger_tip](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_ring_finger_tip.md)
- [ar_hand_skeleton_joint_name_thumb_intermediate_base](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_thumb_intermediate_base.md)
- [ar_hand_skeleton_joint_name_thumb_intermediate_tip](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_thumb_intermediate_tip.md)
- [ar_hand_skeleton_joint_name_thumb_knuckle](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_thumb_knuckle.md)
- [ar_hand_skeleton_joint_name_thumb_tip](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_thumb_tip.md)
- [ar_hand_skeleton_joint_name_wrist](ar_hand_skeleton_joint_name_t/ar_hand_skeleton_joint_name_wrist.md)
- [ar_hand_chirality_left](ar_hand_chirality_t/ar_hand_chirality_left.md)
  A left hand.
- [ar_hand_chirality_right](ar_hand_chirality_t/ar_hand_chirality_right.md)
  A right hand.
- [ar_hand_tracking_provider_t](ar_hand_tracking_provider_t.md)
  A source of live data about the position of a person’s hands and hand joints.
- [ar_hand_tracking_update_handler_t](ar_hand_tracking_update_handler_t.md)
  A handler for receiving updates to hand anchors.
- [ar_hand_tracking_update_handler_function_t](ar_hand_tracking_update_handler_function_t.md)
### Image tracking
- [ar_image_anchor_get_estimated_scale_factor](ar_image_anchor_get_estimated_scale_factor.md)
  Gets the estimated scale factor between the tracked image’s physical size and the reference image’s size.
- [ar_image_anchor_get_reference_image](ar_image_anchor_get_reference_image.md)
  Gets the reference image that this image anchor tracks.
- [ar_image_anchors_enumerate_anchors](ar_image_anchors_enumerate_anchors.md)
  Enumerates a collection of image anchors.
- [ar_image_anchors_enumerate_anchors_f](ar_image_anchors_enumerate_anchors_f.md)
  Enumerates a collection of image anchors.
- [ar_image_anchors_get_count](ar_image_anchors_get_count.md)
  Gets the number of image anchors in the collection.
- [ar_image_tracking_provider_create](ar_image_tracking_provider_create.md)
  Creates an image tracking provider that tracks the reference images you supply.
- [ar_image_tracking_provider_is_supported](ar_image_tracking_provider_is_supported.md)
  Returns a Boolean value that indicates whether the current runtime environment supports image tracking providers.
- [ar_image_tracking_provider_get_required_authorization_type](ar_image_tracking_provider_get_required_authorization_type.md)
  Gets the types of authorizations required to track images.
- [ar_image_tracking_provider_set_update_handler](ar_image_tracking_provider_set_update_handler.md)
  Sets the handler for receiving image tracking updates.
- [ar_image_tracking_provider_set_update_handler_f](ar_image_tracking_provider_set_update_handler_f.md)
  Sets the handler for receiving image tracking updates.
- [ar_image_tracking_configuration_add_reference_images](ar_image_tracking_configuration_add_reference_images.md)
  Adds reference images to the set to be tracked.
- [ar_image_tracking_configuration_create](ar_image_tracking_configuration_create.md)
  Creates an image tracking configuration.
- [ar_image_tracking_configuration_t](ar_image_tracking_configuration_t.md)
- [ar_reference_images_t](ar_reference_images_t.md)
  A collection of reference images.
- [ar_reference_images_enumerator_t](ar_reference_images_enumerator_t.md)
  A handler for enumerating a collection of reference images.
- [ar_reference_images_add_image](ar_reference_images_add_image.md)
  Adds a reference image to a collection.
- [ar_reference_images_add_images](ar_reference_images_add_images.md)
  Adds multiple reference images to a collection.
- [ar_reference_images_create](ar_reference_images_create.md)
  Creates an empty collection of reference images.
- [ar_reference_images_enumerate_images](ar_reference_images_enumerate_images.md)
  Enumerates a collection of reference images.
- [ar_reference_images_enumerate_images_f](ar_reference_images_enumerate_images_f.md)
  Enumerates a collection of reference images.
- [ar_reference_images_get_count](ar_reference_images_get_count.md)
  Gets the number of reference images in a collection.
- [ar_reference_images_load_reference_images_in_group](ar_reference_images_load_reference_images_in_group.md)
  Creates multiple reference images based on their group name in an asset catalog.
- [ar_reference_image_create_from_cgimage](ar_reference_image_create_from_cgimage.md)
  Creates a reference image from a Core Graphics image.
- [ar_reference_image_create_from_pixel_buffer](ar_reference_image_create_from_pixel_buffer.md)
  Creates a reference image from a pixel buffer.
- [ar_reference_image_get_name](ar_reference_image_get_name.md)
  Gets the name of a reference image.
- [ar_reference_image_set_name](ar_reference_image_set_name.md)
  Sets the name of a reference image.
- [ar_reference_image_get_physical_height](ar_reference_image_get_physical_height.md)
  Gets the height, in meters, of a reference image in the real world.
- [ar_reference_image_get_physical_width](ar_reference_image_get_physical_width.md)
  Gets the height, in meters, of a reference image in the real world.
- [ar_image_tracking_provider_t](ar_image_tracking_provider_t.md)
  A source of live data about a 2D image’s position in a person’s surroundings.
- [ar_image_tracking_update_handler_t](ar_image_tracking_update_handler_t.md)
  A handler for receiving updates to image anchors.
- [ar_reference_image_t](ar_reference_image_t.md)
  A 2D image the system uses as a reference to find the same image in a person’s surroundings.
- [ar_image_anchors_enumerator_function_t](ar_image_anchors_enumerator_function_t.md)
- [ar_image_tracking_update_handler_function_t](ar_image_tracking_update_handler_function_t.md)
- [ar_reference_images_enumerator_function_t](ar_reference_images_enumerator_function_t.md)
### Objective-C compatibility
- [ARKit Functions](arkit-functions.md)
- [ARKit Data Types](arkit-data-types.md)
- [Objective-C compatibility](objective-c-compatibility.md)
### Errors
- [ar_error_t](ar_error_t.md)
  An error reported by ARKit.
- [ar_error_code_t](ar_error_code_t.md)
  Codes that identify errors in ARKit.
- [ar_error_domain](ar_error_domain.md)
  A string that indicates the error domain in Core Foundation.
- [ar_error_get_error_code](ar_error_get_error_code.md)
  Gets the error code associated with an error.
- [ar_error_copy_cf_error](ar_error_copy_cf_error.md)
  Copies a reference to a Core Foundation error object that represents the specified ARKit error.
### Protocols
- [AR_EXTERN_C_BEGIN](ar_extern_c_begin.md)
- [AR_EXTERN_C_END](ar_extern_c_end.md)
- [ar_object_h](ar_object_h.md)
- [authorization_h](authorization_h.md)
- [barcode_detection_h](barcode_detection_h.md)
- [data_h](data_h.md)
- [data_provider_h](data_provider_h.md)
- [environment_light_estimation_h](environment_light_estimation_h.md)
- [error_h](error_h.md)
- [hand_skeleton_h](hand_skeleton_h.md)
- [hand_tracking_h](hand_tracking_h.md)
- [image_tracking_h](image_tracking_h.md)
- [session_h](session_h.md)
- [skeleton_joint_h](skeleton_joint_h.md)

## See Also

- [Setting up access to ARKit data](../visionOS/setting-up-access-to-arkit-data.md)
  Check whether your app can use ARKit and respect people’s privacy.
- [ARKit in visionOS C API](arkit-in-visionos-c-api.md)
  Integrate ARKit with low-level libraries and functionality.
- [ARKit in iOS](arkit-in-ios.md)
  Integrate iOS device camera and motion features to produce augmented reality experiences in your app or game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkit-in-visionos-c-api)*