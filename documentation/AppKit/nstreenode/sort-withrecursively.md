# sort(with:recursively:)

**Framework**: AppKit  
**Kind**: method

Sorts the receiver’s subtree using the values of the represented objects with the specified sort descriptors.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func sort(with sortDescriptors: [NSSortDescriptor], recursively: Bool)
```

#### Discussion

All the represented objects in the child nodes must be key-value coding compliant for the keys specified in the sort descriptors.

## Parameters

- `sortDescriptors`: Array of sort descriptors specifying how to sort the represented objects.
- `recursively`: A Boolean that specifies whether the child nodes should be sorted recursively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreenode/sort(with:recursively:))*