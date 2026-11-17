# ar_hand_tracking_provider_query_anchors_at_timestamp

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

The provided `timestamp`when rendering should be obtained from `cp_frame_timing_get_trackable_anchor_time`.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern ar_hand_anchor_query_status_t ar_hand_tracking_provider_query_anchors_at_timestamp(ar_hand_tracking_provider_t hand_tracking_provider, CFTimeInterval timestamp, ar_hand_anchor_t hand_anchor_left, ar_hand_anchor_t hand_anchor_right);
```

## Return Value

Whether the query was successful or not.

## Discussion

```objc
cp_time_t anchor_prediction_time = cp_frame_timing_get_trackable_anchor_time(timing);
CFTimeInterval anchor_prediction_time_seconds = cp_time_to_cf_time_interval(anchor_prediction_time);

ar_hand_tracking_provider_query_anchors_at_timestamp(provider, hand_anchor_left, hand_anchor_right);

if (ar_trackable_anchor_is_tracked(hand_anchor_left)) {
   ...
}

if (ar_trackable_anchor_is_tracked(hand_anchor_right)) {
   ...
}
```

## Parameters

- `hand_tracking_provider`: The hand tracking provider.
- `timestamp`: Target timestamp, mach absolute time in seconds.
- `hand_anchor_left`: The anchor instance for the left hand to be updated.
- `hand_anchor_right`: The anchor instance for the right hand to be updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_hand_tracking_provider_query_anchors_at_timestamp)*