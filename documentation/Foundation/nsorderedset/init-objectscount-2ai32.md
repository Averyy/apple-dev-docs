# init(objects:count:)

**Framework**: Foundation  
**Kind**: init

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

#### Return Value

An initialized ordered set containing cnt objects from the list of objects specified by objects. The returned set might be different than the original receiver.

#### Discussion

This method is a designated initializer of `NSOrderedSet`.

## Parameters

- `objects`: If the same object appears more than once in objects, it is added only once to the returned ordered set.
- `cnt`: The number of objects from objects to add to the new ordered set.

## See Also

- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](nsorderedset/init(objects:count:)-3ny0m.md)
  Creates and returns a set containing a specified number of objects from a given C array of objects.
- [convenience init(array: [Any])](nsorderedset/init(array:).md)
  Initializes a newly allocated set with the objects that are contained in a given array.
- [convenience init(array: [Any], copyItems: Bool)](nsorderedset/init(array:copyitems:).md)
  Initializes a newly allocated set with the objects that are contained in a given array, optionally copying the items.
- [convenience init(array: [Any], range: NSRange, copyItems: Bool)](nsorderedset/init(array:range:copyitems:).md)
  Initializes a newly allocated set with the objects that are contained in the specified range of an array, optionally copying the items.
- [convenience init(object: Any)](nsorderedset/init(object:).md)
  Initializes a new ordered set with the object.
- [convenience init(orderedSet: NSOrderedSet)](nsorderedset/init(orderedset:).md)
  Initializes a new ordered set with the contents of a set.
- [convenience init(orderedSet: NSOrderedSet, copyItems: Bool)](nsorderedset/init(orderedset:copyitems:).md)
  Initializes a new ordered set with the contents of a set, optionally copying the items.
- [convenience init(orderedSet: NSOrderedSet, range: NSRange, copyItems: Bool)](nsorderedset/init(orderedset:range:copyitems:).md)
  Initializes a new ordered set with the contents of an ordered set, optionally copying the items.
- [convenience init(set: Set<AnyHashable>)](nsorderedset/init(set:).md)
  Initializes a new ordered set with the contents of a set.
- [convenience init(set: Set<AnyHashable>, copyItems: Bool)](nsorderedset/init(set:copyitems:).md)
  Initializes a new ordered set with the contents of a set, optionally copying the objects in the set.
- [init()](nsorderedset/init.md)
  Initializes a newly allocated ordered set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/init(objects:count:)-2ai32)*