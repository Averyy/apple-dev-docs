# group::elementMaximumInGroup

**Framework**: Compute Graph  
**Kind**: func

Returns the maximum number of elements that can exist in the group.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
int group::elementMaximumInGroup()
```

#### Return Value

The maximum number of elements allocated for this group

#### Discussion

Use this function to determine the fixed capacity of particles per group, which is useful for normalizing element indices or managing group resources.

> **Note**: ![Graph](/images/com.apple.computegraph/group__elementMaximumInGroup.svg)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/group/elementmaximumingroup)*