# insert(_:at:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Inserts a descriptor at the specified (one-based) position in the receiving descriptor list, replacing the existing descriptor, if any, at that position.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func insert(_ descriptor: NSAppleEventDescriptor, at index: Int)
```

```objc
- (void) insertDescriptor:(NSAppleEventDescriptor *) descriptor atIndex:(NSInteger) index;
```

## Discussion

Because it actually replaces the descriptor, if any, at the specified position, this method might better be called `replaceDescriptor:atIndex:`. The receiver must be a list descriptor. The indices are one-based. Currently provides no indication if an error occurs.

## Parameters

- `descriptor`: The descriptor to insert in the receiver. Specifying an index of 0 or count + 1 causes appending to the end of the list.
- `index`: The one-based descriptor list position at which to insert the descriptor.

## See Also

### Working With List Descriptors
- [func atIndex(Int) -> NSAppleEventDescriptor?](./atindex%28_%29.md)
  Returns the descriptor at the specified (one-based) position in the receiving descriptor list.
- [func remove(at: Int)](./remove%28at%29.md)
  Removes the descriptor at the specified (one-based) position in the receiving descriptor list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/insert(_:at:))*