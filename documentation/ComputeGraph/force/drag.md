# force::drag

**Framework**: ComputeGraph  
**Kind**: func

Applies linear drag to slow down the current element over time.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
void force::drag(float linearDragFactor)
```

#### Discussion

This function simulates air resistance or fluid drag by reducing the element’s velocity proportionally to its current speed. The drag is frame-rate independent, ensuring consistent behavior across different frame rates.

The drag force is calculated as: `velocity -= velocity * min(1.0, deltaTime * linearDragFactor)`

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/46808cad6bf650178ab11557ad26d5ce/force__drag.svg)

> **Note**: Reads and writes to element state `float3 velocity`

## Parameters

- `linearDragFactor`: The drag coefficient controlling how quickly the element slows down. Higher values result in faster deceleration. A value of 0 means no drag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/force/drag)*