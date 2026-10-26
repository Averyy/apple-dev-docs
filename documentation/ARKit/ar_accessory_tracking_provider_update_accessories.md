# ar_accessory_tracking_provider_update_accessories

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Update the accessories being tracked by a provider.

**Availability**:
- visionOS 27.0+

## Declaration

```c
extern void ar_accessory_tracking_provider_update_accessories(ar_accessory_tracking_provider_t accessory_tracking_provider, ar_accessories_t accessories, ar_accessory_tracking_update_accessories_completion_handler_t completion_handler);
```

#### Discussion

Updates are atomic: if any accessory fails to be added, the entire request fails and the provider continues tracking the original set of accessories.

Update requests are processed sequentially. If multiple requests are made while an update is in progress, only the most recent request is retained and will be processed next; intermediate requests are superseded and their completion handlers are called with an error.

The completion handler will be called with an error when one or more accessories cannot be added or the request is superseded by a more recent request.

## Parameters

- `accessory_tracking_provider`: The accessory tracking provider.
- `accessories`: The new set of accessories to track.
- `completion_handler`: Handler triggered after the update completes.

## See Also

### Accessory tracking
- [ar_accessories_enumerator_function_t](./ar_accessories_enumerator_function_t.md)
  Function for enumerating a collection of accessories.
- [ar_accessories_enumerator_t](./ar_accessories_enumerator_t.md)
  Handler for enumerating a collection of accessories.
- [ar_accessories_t](./ar_accessories_t.md)
  A collection of accessories.
- [ar_accessory_anchor_t](./ar_accessory_anchor_t.md)
  An anchor that represents an accessory.
- [ar_accessory_anchors_enumerator_function_t](./ar_accessory_anchors_enumerator_function_t.md)
  Function for enumerating a collection of accessory anchors.
- [ar_accessory_anchors_enumerator_t](./ar_accessory_anchors_enumerator_t.md)
  Handler for enumerating a collection of accessory anchors.
- [ar_accessory_anchors_t](./ar_accessory_anchors_t.md)
  A collection of accessory anchors.
- [ar_accessory_device_load_completion_handler_function_t](./ar_accessory_device_load_completion_handler_function_t.md)
  Function triggered when a request to load an accessory from a `GCDevice` has completed.
- [ar_accessory_device_load_completion_handler_t](./ar_accessory_device_load_completion_handler_t.md)
  Handler triggered when a request to load an accessory from a `GCDevice` has completed.
- [ar_accessory_t](./ar_accessory_t.md)
  An accessory that can be tracked in the physical environment, such as a game controller or stylus.
- [ar_accessory_tracking_configuration_t](./ar_accessory_tracking_configuration_t.md)
  Configuration for accessory tracking.
- [ar_accessory_tracking_provider_t](./ar_accessory_tracking_provider_t.md)
  A data provider for accessory tracking.
- [ar_accessory_tracking_update_handler_function_t](./ar_accessory_tracking_update_handler_function_t.md)
  Function called when there are updates to accessory anchors.
- [ar_accessory_tracking_update_handler_t](./ar_accessory_tracking_update_handler_t.md)
  Handler called when there are updates to accessory anchors.
- [ar_accessory_location_name_aim](./ar_accessory_location_name_aim.md)
  Pre-defined accessory location name for spatial gamepad and stylus aim point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_accessory_tracking_provider_update_accessories)*