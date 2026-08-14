# orient_to_velocity

**Framework**: Compute Graph  
**Kind**: func

Orient the particle by setting its `axisY` to the velocity’s current direction.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
void orient_to_velocity()
```

#### Discussion

Adding this node will cause a `float3 axisY` attribute to be added, if one doesn’t already exist.

> **Note**: ![Graph](/images/com.apple.computegraph/orient_to_velocity.svg)

> **Note**: Reads from element state `float3 velocity`, if it exists

> **Note**: Writes to element state `float3 axisY`


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/orient_to_velocity)*