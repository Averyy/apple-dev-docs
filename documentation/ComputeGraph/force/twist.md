# force::twist

**Framework**: Compute Graph  
**Kind**: func

Applies a twisting force around a vertical axis through a specified origin point.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
void force::twist(float3 origin, float strength, float attraction)
```

#### Discussion

This function creates a vortex-like effect by applying two force components: a tangential force that causes rotation around the origin, and an optional attractive or repulsive force toward or away from the origin. The twist occurs around a vertical (Y-axis) through the specified origin point.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/3f449b2104da17812b5552060b14ea92/force__twist.svg)

## Parameters

- `origin`: The 3D point in world space around which the twist force is centered.
- `strength`: The magnitude of the tangential (rotational) force. Higher values create stronger rotation.
- `attraction`: The magnitude of the radial force. Positive values attract elements toward the origin, while negative values repel elements away from the origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/force/twist)*