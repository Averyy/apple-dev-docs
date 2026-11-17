# ar_object_tracking_configuration_get_maximum_trackable_instances

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Get the number to be configured for the maximum number of reference object instances to track.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern int ar_object_tracking_configuration_get_maximum_trackable_instances(ar_object_tracking_configuration_t object_tracking_configuration);
```

## Return Value

The configured number.

## Parameters

- `object_tracking_configuration`: The object tracking configuration.

## See Also

### Object tracking configuration functions
- [ar_object_tracking_configuration_add_reference_objects](./ar_object_tracking_configuration_add_reference_objects.md)
  Add reference objects to the set of objects to be tracked. Object tracking will run without any reference objects, but will detect nothing.
- [ar_object_tracking_configuration_create](./ar_object_tracking_configuration_create.md)
  Create an object tracking configuration.
- [ar_object_tracking_configuration_get_detection_rate](./ar_object_tracking_configuration_get_detection_rate.md)
  Get the frequency to be configured for running object detection.
- [ar_object_tracking_configuration_get_maximum_instances_per_reference_object](./ar_object_tracking_configuration_get_maximum_instances_per_reference_object.md)
  Get the number to be configured for the maximum number of instances of each reference object type to track.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_object_tracking_configuration_get_maximum_trackable_instances)*