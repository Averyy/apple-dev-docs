# init(orderedSet:range:copyItems:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a new ordered set with the contents of an ordered set, optionally copying the items.

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
convenience init(orderedSet set: NSOrderedSet, range: NSRange, copyItems flag: Bool)
```

```objc
- (instancetype) initWithOrderedSet:(NSOrderedSet<id> *) set range:(NSRange) range copyItems:(BOOL) flag;
```

#### Return Value

An initialized ordered set containing the objects in the ordered set.

## Parameters

- `set`: An ordered set.
- `range`: The range of objects in `orderedSet` to add to the ordered set.
- `flag`: If [`true`](../../Swift/true.md) the objects are copied to the ordered set; otherwise [`false`](../../Swift/false.md).

## See Also

### Initializing an Ordered Set
- [convenience init(array: [Any])](./init%28array%29.md)
  Initializes a newly allocated set with the objects that are contained in a given array.
- [convenience init(array: [Any], copyItems: Bool)](./init%28array,copyitems%29.md)
  Initializes a newly allocated set with the objects that are contained in a given array, optionally copying the items.
- [convenience init(array: [Any], range: NSRange, copyItems: Bool)](./init%28array,range,copyitems%29.md)
  Initializes a newly allocated set with the objects that are contained in the specified range of an array, optionally copying the items.
- [convenience init(object: Any)](./init%28object%29.md)
  Initializes a new ordered set with the object.
- [init(objects: UnsafePointer<AnyObject>?, count: Int)](./init%28objects,count%29-2ai32.md)
  Initializes a newly allocated set with a specified number of objects from a given C array of objects.
- [convenience init(orderedSet: NSOrderedSet)](./init%28orderedset%29.md)
  Initializes a new ordered set with the contents of a set.
- [convenience init(orderedSet: NSOrderedSet, copyItems: Bool)](./init%28orderedset,copyitems%29.md)
  Initializes a new ordered set with the contents of a set, optionally copying the items.
- [convenience init(set: Set<AnyHashable>)](./init%28set%29.md)
  Initializes a new ordered set with the contents of a set.
- [convenience init(set: Set<AnyHashable>, copyItems: Bool)](./init%28set,copyitems%29.md)
  Initializes a new ordered set with the contents of a set, optionally copying the objects in the set.
- [init()](./init%28%29.md)
  Initializes a newly allocated ordered set.
- [- initWithObjects:](./initwithobjects_.md)
  Initializes a newly allocated set with members taken from the specified list of objects.
### Related Documentation
- [+ orderedSetWithOrderedSet:](./orderedsetwithorderedset_.md)
  Creates and returns an ordered set containing the objects from another ordered set.
- [+ orderedSetWithOrderedSet:range:copyItems:](./orderedsetwithorderedset_range_copyitems_.md)
  Creates and returns a new ordered set for a specified range of objects in an ordered set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/init(orderedset:range:copyitems:))*