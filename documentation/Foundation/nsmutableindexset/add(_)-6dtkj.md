# add(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds an index  to the receiver.

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
func add(_ value: Int)
```

```objc
- (void) addIndex:(NSUInteger) value;
```

## Parameters

- `value`: Index to add. Must be in the range `0 .. NSNotFound - 1`.

## See Also

### Related Documentation
- [Collections Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Collections.html#//apple_ref/doc/uid/10000034i)
### Adding Indexes
- [func add(IndexSet)](./add%28_%29-6zmti.md)
  Adds the indexes in an index set to the receiver.
- [func add(in: NSRange)](./add%28in%29.md)
  Adds the indexes in an index range to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableindexset/add(_:)-6dtkj)*