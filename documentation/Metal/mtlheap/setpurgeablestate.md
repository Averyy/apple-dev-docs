# setPurgeableState(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Sets the purgeable state of the heap.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func setPurgeableState(_ state: MTLPurgeableState) -> MTLPurgeableState
```

#### Return Value

The previous purgeable state of the heap.

#### Discussion

The heap purgeability state refers to its whole backing memory and affects all resources in the heap. Heaps can be marked purgeable but its resources cannot; the heap’s resources always reflect the heap’s purgeability state.

Refer to the [`MTLPurgeableState`](mtlpurgeablestate.md) and [`setPurgeableState(_:)`](mtlresource/setpurgeablestate(_:).md) reference for further information.

## Parameters

- `state`: The desired purgeable state of the heap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/setpurgeablestate(_:))*