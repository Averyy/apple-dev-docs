# init(objects:count:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a newly allocated set with a specified number of objects from a given C array of objects.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(objects: UnsafePointer<AnyObject>?, count cnt: Int)
```

```objc
- (instancetype) initWithObjects:(ObjectType const[]) objects count:(NSUInteger) cnt;
```

#### Return Value

An initialized ordered set containing cnt objects from the list of objects specified by objects. The returned set might be different than the original receiver.

#### Discussion

This method is a designated initializer of `NSOrderedSet`.

## Parameters

- `objects`: A C array of objects to add to the new set.

  If the same object appears more than once in objects, it is added only once to the returned ordered set.
- `cnt`: The number of objects from objects to add to the new ordered set.

## See Also

### Related Documentation
- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](./init%28objects,count%29-3ny0m.md)
  Creates and returns a set containing a specified number of objects from a given C array of objects.
### Initializing an Ordered Set
- [convenience init(array: [Any])](./init%28array%29.md)
  Initializes a newly allocated set with the objects that are contained in a given array.
- [convenience init(array: [Any], copyItems: Bool)](./init%28array,copyitems%29.md)
  Initializes a newly allocated set with the objects that are contained in a given array, optionally copying the items.
- [convenience init(array: [Any], range: NSRange, copyItems: Bool)](./init%28array,range,copyitems%29.md)
  Initializes a newly allocated set with the objects that are contained in the specified range of an array, optionally copying the items.
- [convenience init(object: Any)](./init%28object%29.md)
  Initializes a new ordered set with the object.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/init(objects:count:)-2ai32)*