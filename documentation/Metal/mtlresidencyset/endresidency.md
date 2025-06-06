# endResidency()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Informs Metal that the residency set’s allocations no longer need to be resident, and that it can reuse the memory for other allocations.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func endResidency()
```

## Mentions

- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresidencyset/endresidency())*