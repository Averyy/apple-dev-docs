# ar_accessory_tracking_provider_predict_anchor_at_timestamp

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Predict an accessory anchor to a target timestamp.

**Availability**:
- visionOS 26.0+

## Declaration

```c
extern bool ar_accessory_tracking_provider_predict_anchor_at_timestamp(ar_accessory_tracking_provider_t accessory_tracking_provider, ar_accessory_anchor_t anchor, CFTimeInterval timestamp, ar_accessory_anchor_t predicted_anchor);
```

#### Return Value

Whether accessory anchor prediction was successful.

#### Discussion

Example usage:

```
auto timing_info = cp_drawable_get_frame_timing(drawable);
auto time = cp_time_to_cf_time_interval(cp_frame_timing_get_trackable_anchor_time(timing_info));
const BOOL success = ar_accessory_tracking_provider_predict_anchor_at_timestamp(_provider, anchor_id, timestamp, accessory_anchor);
```

> **Note**: A large time offset from latest anchor timestamp could degrade accuracy. For accuracy sensitive use cases like drawing, use a small offset or the latest anchor. Use a prediction timestamp smaller than the latest anchor timestamp for interpolation.

## Parameters

- `accessory_tracking_provider`: An accessory tracking provider.
- `anchor`: An anchor to predict. Use `ar_accessory_tracking_provider_get_latest_anchors` to get latest anchors. Use tracked anchors to predict.
- `timestamp`: The timestamp to get the accessory anchor at. The timestamp should be provided as mach absolute time in seconds.
- `predicted_anchor`: The output predicted accessory anchor.

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

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_accessory_tracking_provider_predict_anchor_at_timestamp)*