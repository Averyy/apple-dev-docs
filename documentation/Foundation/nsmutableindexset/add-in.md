# add(in:)

**Framework**: Foundation  
**Kind**: method

Adds the indexes in an index range to the receiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func add(in range: NSRange)
```

#### Discussion

This method raises an [`rangeException`](nsexceptionname/rangeexception.md) when `range` would add an index that exceeds the maximum allowed value for unsigned integers.

## Parameters

- `range`: Index range to add. Must be in the range  .

## See Also

- [func add(Int)](nsmutableindexset/add(_:)-6dtkj.md)
  Adds an index  to the receiver.
- [func add(IndexSet)](nsmutableindexset/add(_:)-6zmti.md)
  Adds the indexes in an index set to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableindexset/add(in:))*