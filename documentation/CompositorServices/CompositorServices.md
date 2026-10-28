# Compositor Services

**Framework**: Compositor Services  
**Kind**: module  
**Role**: Framework

Take control of the drawing environment and render your own content using Metal.

**Availability**:
- visionOS 1.0+

## Overview

Compositor Services lets you draw directly to the device’s displays using Metal and your own rendering engine. Use this framework to create a fully immersive scene in your app that doesn’t require integration with the person’s surroundings.

When you present an immersive space with [`CompositorLayer`](./compositorlayer.md) content from your app, you receive a [`LayerRenderer`](./layerrenderer.md) with the information you need to set up your Metal drawing environment. Use the layer to start your rendering loop and deliver successive frames of content. The layer provides the timing information you need to deliver frames at the refresh rate of the display. It also provides the Metal textures and other information that you need to draw content on the device displays.

For more information about how to draw your app’s content using Metal, see [Metal](../Metal/Metal.md).

## Topics

### App integration
- [Drawing fully immersive content using Metal](./drawing-fully-immersive-content-using-metal.md)
  Create a fully immersive experience in visionOS using a custom Metal-based rendering engine.
- [Interacting with virtual content blended with passthrough](./interacting-with-virtual-content-blended-with-passthrough.md)
  Present a mixed immersion style space to draw content in a person’s surroundings, and choose how upper limbs appear with respect to rendered content.
- [Rendering hover effects in Metal immersive apps](./rendering_hover_effects_in_metal_immersive_apps.md)
  Change the appearance of a rendered onscreen element when a player gazes at it.
- [struct CompositorLayer](./compositorlayer.md)
  A type that you use with an immersive space to display fully immersive content using Metal.
- [protocol CompositorLayerConfiguration](./compositorlayerconfiguration.md)
  An interface for specifying the texture configurations and rendering behaviors to use with your Metal rendering engine.
- [struct DefaultCompositorLayerConfiguration](./defaultcompositorlayerconfiguration.md)
  A type that configures the layer with the default texture configurations and rendering behaviors for the current device.
### Render-loop setup
- [class LayerRenderer](./layerrenderer.md)
  A type that provides the Metal types and timing information you need to draw your content.
- [LayerRenderer.Frame](./layerrenderer/frame.md)
  A type that provides access to the timing information and data types you need to render a single frame of content.
- [Layer renderer](./layer-renderer.md)
  A type that provides the Metal types and timing information you need to draw your content.
- [Frames](./frames.md)
  A type that represents a single frame of content, manages the pace of animations, and provides access to the drawable environment.
- [Utilities](./utilities.md)
  Common types and utilities to manage your app’s rendering process.
### Drawing environment
- [LayerRenderer.Drawable](./layerrenderer/drawable.md)
  A type that provides the textures and information you need to draw a frame of content.
- [LayerRenderer.Drawable.View](./layerrenderer/drawable/view.md)
  A type that provides information on how to render content into the frame’s textures.
- [Drawable](./drawable.md)
  A type that provides information on how to render content into the frame’s textures.
- [View](./view.md)
  A type that manages the viewport and texture details for each portion of your frame’s content.
### Errors
- [enum LayerRendererConfigurationError](./layerrendererconfigurationerror.md)
  Errors that can occur when configuring layers.
- [cp_layer_renderer_configuration_error_domain](./cp_layer_renderer_configuration_error_domain.md)
  The domain for errors that occur during layer configuration.
- [cp_layer_renderer_configuration_error_code](./cp_layer_renderer_configuration_error_code.md)
  Errors that can occur during layer configuration.
### Articles
- [Controlling Metal rendering immersion level](./controlling-metal-rendering-immersion-level.md)
  Enable flexible immersive rendering by supporting progressive immersion when rendering your Metal content.
- [CompositorServices Functions](./compositorservices-functions.md)
### Structures
- [struct TextureTopology](./texturetopology.md)
  A type that specifies the organization of one of the drawable’s textures.
- [cp_time](./cp_time.md)
  A Mach absolute time clock value.
### Variables
- [var CP_ARKIT_AVAILABLE: Bool](./cp_arkit_available.md)
- [cp_tracking_area_identifier_invalid](./cp_tracking_area_identifier_invalid.md)
  Identifier reserved as invalid.
- [cp_tracking_area_render_value_invalid](./cp_tracking_area_render_value_invalid.md)
  Value to be used in the tracking area texture, to indicate that there is no tracking area at a given pixel.
### Type Aliases
- [typealias cp_drawable_array_t](./cp_drawable_array_t.md)
  An opaque type that contains the drawable types and other information you need to set up your render pipeline.
- [typealias cp_hover_effect_t](./cp_hover_effect_t.md)
  An opaque type that describes a hover effect of the tracking area.
- [cp_tracking_area_identifier](./layerrenderer/drawable/trackingarea/identifier-swift.struct.md)
  An identifier for the tracking area.
- [cp_tracking_area_render_value](./layerrenderer/drawable/trackingarea/rendervalue-swift.struct.md)
  A value used when rendering a tracking area.
- [cp_render_quality_t](./layerrenderer/renderquality-swift.struct.md)
  Render quality controls the quality which drawing happens at.
- [cp_drawable_render_context_t](./cp_drawable_render_context_t.md)
  An object that can render any effects associated with a drawable This is required for applications that want to render using the Progressive Immersion Style
- [cp_tracking_area_t](./cp_tracking_area_t.md)
  An opaque type that describes a region of a view that interacts with the gaze/cursor.
### Functions
- [cp_tracking_area_get_identifier](./layerrenderer/drawable/trackingarea/identifier-swift.property.md)
  Returns the identifier for the tracking area.
- [cp_tracking_area_get_render_value](./layerrenderer/drawable/trackingarea/rendervalue-swift.property.md)
  Returns the render value for the tracking area.
- [cp_drawable_add_tracking_area](./layerrenderer/drawable/addtrackingarea%28identifier%29.md)
  Returns a tracking area which is create on the drawable’s list of tracking areas.
- [cp_drawable_mtl4_encode_present](./layerrenderer/drawable/encodepresent%28%29.md)
  Encodes a notification event to the specified command buffer to present the drawable’s content onscreen.
- [cp_drawable_is_content_capture_protected](./layerrenderer/drawable/iscontentcaptureprotected.md)
  Returns whether content capture is protected and it is safe to draw content that should be protected from capture.
- [cp_frame_get_drawable_target_view_count](./layerrenderer/frame/drawabletargetviewcount%28target%29.md)
  Returns the number of view in the drawable target.
- [cp_layer_renderer_get_mtl4_command_queue](./layerrenderer/commandqueue.md)
  Returns the command queue that the layer uses for drawing operations.
- [cp_drawable_array_get_count](./cp_drawable_array_get_count.md)
  Returns the number of drawables in the array.
- [cp_drawable_array_get_drawable](./cp_drawable_array_get_drawable.md)
  Returns the drawable at the specified index in the array.
- [cp_drawable_get_tracking_areas_texture](./cp_drawable_get_tracking_areas_texture.md)
  Returns the tracking areas texture at the specified index in the drawable.
- [cp_drawable_get_tracking_areas_texture_count](./cp_drawable_get_tracking_areas_texture_count.md)
  Returns the number of tracking areas textures available in the drawable.
- [cp_frame_binocular_frustum_matrix_for_drawable_target](./cp_frame_binocular_frustum_matrix_for_drawable_target.md)
  Returns the transform which can be used for binocular frustum culling. A matrix to convert between the device coordinate space to normalized device coordinate space. This should be acquired after query frame via [`cp_layer_renderer_query_next_frame`](./cp_layer_renderer_query_next_frame.md) and before calling into [`cp_frame_end_submission`](./layerrenderer/frame/endsubmission%28%29.md). Renderer should not utilize this transform for actual rendering output.
- [cp_frame_monocular_frustum_matrix_for_drawable_target](./cp_frame_monocular_frustum_matrix_for_drawable_target.md)
  Returns the transform which can be used for monocular frustum culling. A matrix to convert between the device coordinate space to normalized device coordinate space. This should be acquired after query frame via [`cp_layer_renderer_query_next_frame`](./cp_layer_renderer_query_next_frame.md) and before calling into [`cp_frame_end_submission`](./layerrenderer/frame/endsubmission%28%29.md). Renderer should not utilize this transform for actual rendering output.
- [cp_frame_query_drawables](./cp_frame_query_drawables.md)
  Returns the drawable array type you use to retrieve the drawables for drawing environment for the frame.
- [cp_layer_renderer_capabilities_drawable_render_context_supported_stencil_format](./cp_layer_renderer_capabilities_drawable_render_context_supported_stencil_format.md)
  Returns the stencil format at the specified index in the layer capabilities.
- [cp_layer_renderer_capabilities_drawable_render_context_supported_stencil_formats_count](./cp_layer_renderer_capabilities_drawable_render_context_supported_stencil_formats_count.md)
  Returns the number of stencil formats the specified layer supports.
- [cp_layer_renderer_capabilities_get_default_render_quality](./cp_layer_renderer_capabilities_get_default_render_quality.md)
  Returns default render quality for drawing on this platform.
- [cp_layer_renderer_capabilities_supported_color_format_with_options](./cp_layer_renderer_capabilities_supported_color_format_with_options.md)
  Returns the color format at the specified index in the layer capabilities.
- [cp_layer_renderer_capabilities_supported_color_formats_count_with_options](./cp_layer_renderer_capabilities_supported_color_formats_count_with_options.md)
  Returns the number of color formats the specified layer supports.
- [cp_layer_renderer_capabilities_supported_tracking_areas_format](./cp_layer_renderer_capabilities_supported_tracking_areas_format.md)
  Returns the tracking areas format at the specified index in the layer capabilities.
- [cp_layer_renderer_capabilities_supported_tracking_areas_formats_count](./cp_layer_renderer_capabilities_supported_tracking_areas_formats_count.md)
  Returns the number of tracking areas formats the specified layer supports.
- [cp_layer_renderer_configuration_get_drawable_render_context_raster_sample_count](./cp_layer_renderer_configuration_get_drawable_render_context_raster_sample_count.md)
  Returns the raster sample count to use in drawable’s render context.
- [cp_layer_renderer_configuration_get_drawable_render_context_stencil_format](./cp_layer_renderer_configuration_get_drawable_render_context_stencil_format.md)
  Returns the pixel format to use for the stencil texture in drawable’s render context.
- [cp_layer_renderer_configuration_get_max_render_quality](./cp_layer_renderer_configuration_get_max_render_quality.md)
  Get max render quality the layer can use when drawing to the drawables.
- [cp_layer_renderer_configuration_get_supports_mtl4](./cp_layer_renderer_configuration_get_supports_mtl4.md)
  Get whether the layer can use Metal4 when drawing to the drawables.
- [cp_layer_renderer_configuration_get_tracking_areas_format](./cp_layer_renderer_configuration_get_tracking_areas_format.md)
  Returns the pixel format to apply to the layer’s tracking areas textures.
- [cp_layer_renderer_configuration_get_tracking_areas_usage](./cp_layer_renderer_configuration_get_tracking_areas_usage.md)
  Returns the texture usage value to apply to the layer’s tracking areas textures.
- [cp_layer_renderer_configuration_set_drawable_render_context_raster_sample_count](./cp_layer_renderer_configuration_set_drawable_render_context_raster_sample_count.md)
  Sets the raster sample count for the drawable’s render context to the specified value.
- [cp_layer_renderer_configuration_set_drawable_render_context_stencil_format](./cp_layer_renderer_configuration_set_drawable_render_context_stencil_format.md)
  Sets the pixel format for the drawable’s render context stencil textures to the specified value.
- [cp_layer_renderer_configuration_set_max_render_quality](./cp_layer_renderer_configuration_set_max_render_quality.md)
  Set max render quality the layer can use when drawing to the drawables.
- [cp_layer_renderer_configuration_set_supports_mtl4](./cp_layer_renderer_configuration_set_supports_mtl4.md)
  Set whether the layer can use Metal4 when drawing to the drawables.
- [cp_layer_renderer_configuration_set_tracking_areas_format](./cp_layer_renderer_configuration_set_tracking_areas_format.md)
  Sets the pixel format for the layer’s tracking areas textures to the specified value.
- [cp_layer_renderer_configuration_set_tracking_areas_usage](./cp_layer_renderer_configuration_set_tracking_areas_usage.md)
  Sets the texture usage for the layer’s tracking areas textures to the specified value.
- [cp_layer_renderer_properties_get_tracking_areas_max_value](./cp_layer_renderer_properties_get_tracking_areas_max_value.md)
  Returns the max render value for tracking areas’ render values.
- [cp_layer_renderer_set_render_quality](./cp_layer_renderer_set_render_quality.md)
  Set the render quality to be used by the drawables.
- [cp_tracking_area_add_automatic_hover_effect](./cp_tracking_area_add_automatic_hover_effect.md)
  Returns the hover effect opaque object for the tracking area for this frame.
### Macros
- [CP_ARKITCORE_AVAILABLE](./cp_arkitcore_available.md)
- [CP_EXPORT](./cp_export.md)
- [CP_EXTERN](./cp_extern.md)
- [CP_EXTERN_C_BEGIN](./cp_extern_c_begin.md)
- [CP_EXTERN_C_END](./cp_extern_c_end.md)
- [CP_FINAL_CLASS](./cp_final_class.md)
- [CP_MTL4_AVAILABLE](./cp_mtl4_available.md)
- [CP_NONNULL_EXTERN_C_BEGIN](./cp_nonnull_extern_c_begin.md)
- [CP_NONNULL_EXTERN_C_END](./cp_nonnull_extern_c_end.md)
- [CP_NULLABLE_STRUCT_REF](./cp_nullable_struct_ref.md)
- [CP_OBJECT_DECL](./cp_object_decl.md)
- [CP_OBJECT_DECL_](./cp_object_decl_.md)
- [CP_OBJECT_DECL_1](./cp_object_decl_1.md)
- [CP_OBJECT_DECL_2](./cp_object_decl_2.md)
- [CP_OBJECT_DECL_3](./cp_object_decl_3.md)
- [CP_OBJECT_DECL_BASE](./cp_object_decl_base.md)
- [CP_OBJECT_NAME](./cp_object_name.md)
- [CP_STRUCT_REF](./cp_struct_ref.md)
- [CP_STRUCT_REF_](./cp_struct_ref_.md)
- [CP_STRUCT_REF_1](./cp_struct_ref_1.md)
- [CP_STRUCT_REF_2](./cp_struct_ref_2.md)
- [CP_STRUCT_REF_3](./cp_struct_ref_3.md)
- [CP_STRUCT_REF_BASE](./cp_struct_ref_base.md)
- [CP_WARN_UNUSED_RESULT](./cp_warn_unused_result.md)
### Enumerations
- [cp_supported_color_formats_options](./cp_supported_color_formats_options.md)
  The options to provide when calling `cp_layer_renderer_capabilities_supported_color_formats` and [`cp_layer_renderer_capabilities_supported_color_formats_count`](./cp_layer_renderer_capabilities_supported_color_formats_count.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/CompositorServices)*