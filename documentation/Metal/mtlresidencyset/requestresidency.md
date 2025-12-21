# requestResidency()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Tells Metal to do as much preparatory work as it can, with the system’s current conditions, to make the set’s resource allocations resident.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func requestResidency()
```

## Mentions

- [Simplifying GPU resource management with residency sets](simplifying-gpu-resource-management-with-residency-sets.md)

#### Discussion

Call the method anytime after calling a residency set’s [`commit()`](mtlresidencyset/commit().md) method, ideally well before calling the [`commit()`](mtlcommandbuffer/commit().md) method of any [`MTLCommandBuffer`](mtlcommandbuffer.md) that uses it.

The method may postpone some of the necessary steps to make resources resident in scenarios where other apps concurrently need resources in residency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresidencyset/requestresidency())*