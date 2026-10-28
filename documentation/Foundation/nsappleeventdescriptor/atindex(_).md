# atIndex(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the descriptor at the specified (one-based) position in the receiving descriptor list.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func atIndex(_ index: Int) -> NSAppleEventDescriptor?
```

```objc
- (NSAppleEventDescriptor *) descriptorAtIndex:(NSInteger) index;
```

## Return Value

The descriptor from the specified position (one-based) in the descriptor list, or `nil` if the specified descriptor cannot be obtained.

## Parameters

- `index`: The one-based descriptor list position of the descriptor to return.

## See Also

### Working With List Descriptors
- [func insert(NSAppleEventDescriptor, at: Int)](./insert%28_,at%29.md)
  Inserts a descriptor at the specified (one-based) position in the receiving descriptor list, replacing the existing descriptor, if any, at that position.
- [func remove(at: Int)](./remove%28at%29.md)
  Removes the descriptor at the specified (one-based) position in the receiving descriptor list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/atindex(_:))*