# atIndex(_:)

**Framework**: Foundation  
**Kind**: method

Returns the descriptor at the specified (one-based) position in the receiving descriptor list.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func atIndex(_ index: Int) -> NSAppleEventDescriptor?
```

#### Return Value

The descriptor from the specified position (one-based) in the descriptor list, or `nil` if the specified descriptor cannot be obtained.

## Parameters

- `index`: The one-based descriptor list position of the descriptor to return.

## See Also

- [func insert(NSAppleEventDescriptor, at: Int)](nsappleeventdescriptor/insert(_:at:).md)
  Inserts a descriptor at the specified (one-based) position in the receiving descriptor list, replacing the existing descriptor, if any, at that position.
- [func remove(at: Int)](nsappleeventdescriptor/remove(at:).md)
  Removes the descriptor at the specified (one-based) position in the receiving descriptor list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/atindex(_:))*