# init(array:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a newly allocated set with the objects that are contained in a given array.

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
convenience init(array: [Any])
```

```objc
- (instancetype) initWithArray:(NSArray<id> *) array;
```

#### Return Value

An initialized ordered set with the contents of array. The returned ordered set might be different than the original receiver.

## Parameters

- `array`: An array of objects to add to the new set.

  If the same object appears more than once in array, it is represented only once in the returned ordered set.

## See Also

### Initializing an Ordered Set
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
- [- initWithObjects:](./initwithobjects_.md)
  Initializes a newly allocated set with members taken from the specified list of objects.
### Related Documentation
- [+ orderedSetWithArray:](./orderedsetwitharray_.md)
  Creates and returns a set containing a uniqued collection of the objects contained in a given array.
- [+ orderedSetWithArray:range:copyItems:](./orderedsetwitharray_range_copyitems_.md)
  Creates and returns a new ordered set for a specified range of objects in an array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/init(array:))*