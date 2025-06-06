# ar_image_tracking_provider_set_update_handler_f

**Framework**: ARKit  
**Kind**: func

Sets the handler for receiving image tracking updates.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
extern void ar_image_tracking_provider_set_update_handler_f(ar_image_tracking_provider_t image_tracking_provider, dispatch_queue_t image_tracking_updates_queue, void * context, ar_image_tracking_update_handler_function_t image_tracking_update_handler_function);
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_image_tracking_provider_set_update_handler_f)*