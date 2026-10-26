# cp_tracking_area_add_automatic_hover_effect

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the hover effect opaque object for the tracking area for this frame.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
cp_hover_effect_tcp_tracking_area_add_automatic_hover_effect(cp_tracking_area_t tracking_area);
```

#### Return Value

The hover effect for the tracking area.

#### Discussion

The hover effect contains information used to render the hover effect using the tracking area textures and gaze once application render pass has completed. Can only create 1 hover effect per-tracking area, to destroy and disable the hover effect see `cp_hover_effect_destroy`

## Parameters

- `tracking_area`: The tracking area for a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_tracking_area_add_automatic_hover_effect)*