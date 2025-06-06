# label

**Framework**: Metal  
**Kind**: property

An optional name that can help you identify a residency set you create with the descriptor.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var label: String? { get set }
```

#### Discussion

Metal applies the value of this property to the [`label`](mtlresidencyset/label.md) property of an [`MTLResidencySet`](mtlresidencyset.md) that you create by passing the descriptor to [`makeResidencySet(descriptor:)`](mtldevice/makeresidencyset(descriptor:).md).

## See Also

- [var initialCapacity: Int](mtlresidencysetdescriptor/initialcapacity.md)
  The number of allocations a new residency set can store without reallocating memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresidencysetdescriptor/label)*