# initWithObjects:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Initializes a newly allocated set with members taken from the specified list of objects.

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
- (instancetype) initWithObjects:(ObjectType) firstObj;
```

## Return Value

An initialized ordered set containing the objects specified in the parameter list. The returned set might be different than the original receiver.

## Discussion

To add additional objects to the new ordered set, pass comma-separated list of trailing variadic arguments, ending with `nil`,

```
If the same object appears more than once in the list, it is represented only once in the returned ordered set. 
```

## Parameters

- `firstObj`: The first object to add to the new set.

## See Also

### Related Documentation
- [+ orderedSetWithObjects:](./orderedsetwithobjects_.md)
  Creates and returns a ordered set containing the objects in a given argument list.
- [+ orderedSetWithObject:](./orderedsetwithobject_.md)
  Creates and returns a ordered set that contains a single given object.
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
- [convenience init(orderedSet: NSOrderedSet, range: NSRange, copyItems: Bool)](./init%28orderedset,range,copyitems%29.md)
  Initializes a new ordered set with the contents of an ordered set, optionally copying the items.
- [convenience init(set: Set<AnyHashable>)](./init%28set%29.md)
  Initializes a new ordered set with the contents of a set.
- [convenience init(set: Set<AnyHashable>, copyItems: Bool)](./init%28set,copyitems%29.md)
  Initializes a new ordered set with the contents of a set, optionally copying the objects in the set.
- [init()](./init%28%29.md)
  Initializes a newly allocated ordered set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/initwithobjects:)*