# orderedSetWithSet:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns an ordered set with the contents of a set.

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
+ (instancetype) orderedSetWithSet:(NSSet<id> *) set;
```

#### Return Value

A new ordered set containing a uniqued collection of the objects contained in the set.

## Parameters

- `set`: A set.

## See Also

### Related Documentation
- [convenience init(set: Set<AnyHashable>, copyItems: Bool)](./init%28set,copyitems%29.md)
  Initializes a new ordered set with the contents of a set, optionally copying the objects in the set.
- [convenience init(set: Set<AnyHashable>)](./init%28set%29.md)
  Initializes a new ordered set with the contents of a set.
### Creating an Ordered Set
- [+ orderedSet](./orderedset.md)
  Creates and returns an empty ordered set
- [+ orderedSetWithArray:](./orderedsetwitharray_.md)
  Creates and returns a set containing a uniqued collection of the objects contained in a given array.
- [+ orderedSetWithArray:range:copyItems:](./orderedsetwitharray_range_copyitems_.md)
  Creates and returns a new ordered set for a specified range of objects in an array.
- [+ orderedSetWithObject:](./orderedsetwithobject_.md)
  Creates and returns a ordered set that contains a single given object.
- [+ orderedSetWithObjects:](./orderedsetwithobjects_.md)
  Creates and returns a ordered set containing the objects in a given argument list.
- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](./init%28objects,count%29-3ny0m.md)
  Creates and returns a set containing a specified number of objects from a given C array of objects.
- [+ orderedSetWithOrderedSet:](./orderedsetwithorderedset_.md)
  Creates and returns an ordered set containing the objects from another ordered set.
- [+ orderedSetWithOrderedSet:range:copyItems:](./orderedsetwithorderedset_range_copyitems_.md)
  Creates and returns a new ordered set for a specified range of objects in an ordered set.
- [+ orderedSetWithSet:copyItems:](./orderedsetwithset_copyitems_.md)
  Creates and returns an ordered set with the contents of a set, optionally copying the items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/orderedsetwithset:)*