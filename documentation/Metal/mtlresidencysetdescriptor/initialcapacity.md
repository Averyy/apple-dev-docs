# initialCapacity

**Framework**: Metal  
**Kind**: property

The number of allocations a new residency set can store without reallocating memory.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var initialCapacity: Int { get set }
```

#### Discussion

Reduce the memory reallocations the set needs to make by setting the property to a value large enough to hold the allocations you expect. You can leave the property at its default value of `0`, which tells Metal to give the residency set the standard starting capacity.

> **Note**:  The residency set can hold more allocations than its initial capacity.

 The residency set can hold more allocations than its initial capacity.

## See Also

- [var label: String?](mtlresidencysetdescriptor/label.md)
  An optional name that can help you identify a residency set you create with the descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresidencysetdescriptor/initialcapacity)*