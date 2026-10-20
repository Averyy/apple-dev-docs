# commit()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Applies any pending additions to and removals from the residency set.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func commit()
```

```objc
- (void) commit;
```

## Mentions

- [Simplifying GPU resource management with residency sets](../simplifying-gpu-resource-management-with-residency-sets.md)

#### Discussion

Call the method when have no other changes to stage, such as with [`addAllocation(_:)`](./addallocation%28_%29.md), [`removeAllocation(_:)`](./removeallocation%28_%29.md), and their sibling methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresidencyset/commit())*