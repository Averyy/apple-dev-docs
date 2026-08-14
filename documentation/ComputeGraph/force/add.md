# force::add

**Framework**: Compute Graph  
**Kind**: func

Adds a constant force vector to the current element.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
void force::add(float3 force)
```

#### Discussion

This function applies a specified force to the element by adding it to the force accumulator. Multiple forces can be combined by calling this function (or other force functions) multiple times during simulation.

> **Note**: ![Graph](/images/com.apple.computegraph/force__add.svg)

## Parameters

- `force`: The 3D force vector to add to the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/force/add)*