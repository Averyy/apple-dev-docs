# setWithCapacity:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns a mutable set with a given initial capacity.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) setWithCapacity:(NSUInteger) numItems;
```

## Return Value

A mutable set with initial capacity to hold `numItems` members.

## Discussion

Mutable sets allocate additional memory as needed, so `numItems` simply establishes the object’s initial capacity.

## Parameters

- `numItems`: The initial capacity of the new set.

## See Also

### Related Documentation
- [+ set](../nsset/set.md)
  Creates and returns an empty set.
- [Collections Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Collections.html#//apple_ref/doc/uid/10000034i)
- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](../nsset/init%28objects,count%29-65ni4.md)
  Creates and returns a set containing a specified number of objects from a given C array of objects.
### Creating a mutable set
- [init(capacity: Int)](./init%28capacity%29.md)
  Returns an initialized mutable set with a given initial capacity.
- [init()](./init%28%29.md)
  Initializes a newly allocated set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableset/setwithcapacity:)*