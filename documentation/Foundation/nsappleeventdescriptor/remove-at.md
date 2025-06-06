# remove(at:)

**Framework**: Foundation  
**Kind**: method

Removes the descriptor at the specified (one-based) position in the receiving descriptor list.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func remove(at index: Int)
```

#### Discussion

The receiver must be a list descriptor. The  indices are one-based. Currently provides no indication if an error occurs.

## Parameters

- `index`: The one-based position of the descriptor to remove.

## See Also

- [func atIndex(Int) -> NSAppleEventDescriptor?](nsappleeventdescriptor/atindex(_:).md)
  Returns the descriptor at the specified (one-based) position in the receiving descriptor list.
- [func insert(NSAppleEventDescriptor, at: Int)](nsappleeventdescriptor/insert(_:at:).md)
  Inserts a descriptor at the specified (one-based) position in the receiving descriptor list, replacing the existing descriptor, if any, at that position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/remove(at:))*