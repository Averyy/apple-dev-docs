# NSOrderedSet

**Framework**: Foundation  
**Kind**: class

A static, ordered collection of unique objects.

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
class NSOrderedSet
```

#### Overview

[`NSOrderedSet`](nsorderedset.md) declares the programmatic interface for static sets of distinct objects. You establish a static set’s entries when it’s created, and thereafter the entries can’t be modified. [`NSMutableOrderedSet`](nsmutableorderedset.md), on the other hand, declares a programmatic interface for dynamic sets of distinct objects. A dynamic—or mutable—set allows the addition and deletion of entries at any time, automatically allocating memory as needed.

You can use ordered sets as an alternative to arrays when the order of elements is important and performance in testing whether an object is contained in the set is a consideration—testing for membership of an array is slower than testing for membership of a set.

## Topics

### Creating an Ordered Set
- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](nsorderedset/init(objects:count:)-3ny0m.md)
  Creates and returns a set containing a specified number of objects from a given C array of objects.
### Initializing an Ordered Set
- [convenience init(array: [Any])](nsorderedset/init(array:).md)
  Initializes a newly allocated set with the objects that are contained in a given array.
- [convenience init(array: [Any], copyItems: Bool)](nsorderedset/init(array:copyitems:).md)
  Initializes a newly allocated set with the objects that are contained in a given array, optionally copying the items.
- [convenience init(array: [Any], range: NSRange, copyItems: Bool)](nsorderedset/init(array:range:copyitems:).md)
  Initializes a newly allocated set with the objects that are contained in the specified range of an array, optionally copying the items.
- [convenience init(object: Any)](nsorderedset/init(object:).md)
  Initializes a new ordered set with the object.
- [init(objects: UnsafePointer<AnyObject>?, count: Int)](nsorderedset/init(objects:count:)-2ai32.md)
  Initializes a newly allocated set with a specified number of objects from a given C array of objects.
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
### Counting Entries
- [var count: Int](nsorderedset/count.md)
  The number of members in the set.
### Accessing Set Members
- [func contains(Any) -> Bool](nsorderedset/contains(_:).md)
  Returns a Boolean value that indicates whether a given object is present in the ordered set.
- [func enumerateObjects(at: IndexSet, options: NSEnumerationOptions, using: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](nsorderedset/enumerateobjects(at:options:using:).md)
  Executes a given block using the objects in the ordered set at the specified indexes.
- [func enumerateObjects((Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](nsorderedset/enumerateobjects(_:).md)
  Executes a given block using each object in the ordered set.
- [func enumerateObjects(options: NSEnumerationOptions, using: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](nsorderedset/enumerateobjects(options:using:).md)
  Executes a given block using each object in the set, using the specified enumeration options.
- [var firstObject: Any?](nsorderedset/firstobject.md)
  The first object in the ordered set.
- [var lastObject: Any?](nsorderedset/lastobject.md)
  The last object in the ordered set.
- [func object(at: Int) -> Any](nsorderedset/object(at:).md)
  Returns the object at the specified index of the set.
- [func objects(at: IndexSet) -> [Any]](nsorderedset/objects(at:).md)
  Returns the objects in the ordered set at the specified indexes.
- [func index(of: Any) -> Int](nsorderedset/index(of:).md)
  Returns the index of the specified object.
- [func index(of: Any, inSortedRange: NSRange, options: NSBinarySearchingOptions, usingComparator: (Any, Any) -> ComparisonResult) -> Int](nsorderedset/index(of:insortedrange:options:usingcomparator:).md)
  Returns the index, within a specified range, of an object compared with elements in the ordered set using a given NSComparator block.
- [func index(ofObjectAt: IndexSet, options: NSEnumerationOptions, passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](nsorderedset/index(ofobjectat:options:passingtest:).md)
  Returns the index, from a given set of indexes, of the object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [func index(ofObjectPassingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](nsorderedset/index(ofobjectpassingtest:).md)
  Returns the index of the object in the ordered set that passes a test in a given block.
- [func index(NSEnumerationOptions, ofObjectPassingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](nsorderedset/index(_:ofobjectpassingtest:).md)
  Returns the index of an object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [func indexes(ofObjectsAt: IndexSet, options: NSEnumerationOptions, passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](nsorderedset/indexes(ofobjectsat:options:passingtest:).md)
  Returns the index, from a given set of indexes, of the object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [func indexes(ofObjectsPassingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](nsorderedset/indexes(ofobjectspassingtest:).md)
  Returns the index of the object in the ordered set that passes a test in a given block.
- [func indexes(options: NSEnumerationOptions, ofObjectsPassingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](nsorderedset/indexes(options:ofobjectspassingtest:).md)
  Returns the index of an object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [func objectEnumerator() -> NSEnumerator](nsorderedset/objectenumerator.md)
  Returns an enumerator object that lets you access each object in the ordered set.
- [func reverseObjectEnumerator() -> NSEnumerator](nsorderedset/reverseobjectenumerator.md)
  Returns an enumerator object that lets you access each object in the ordered set.
- [var reversed: NSOrderedSet](nsorderedset/reversed.md)
  An ordered set in the reverse order.
### Key-Value Coding Support
- [func setValue(Any?, forKey: String)](nsorderedset/setvalue(_:forkey:).md)
  Invokes `setValue:forKey:` on each of the receiver’s members using the specified value and key
- [func value(forKey: String) -> Any](nsorderedset/value(forkey:).md)
  Returns an ordered set containing the results of invoking `valueForKey:` using key on each of the ordered set’s objects.
### Key-Value Observing Support
- [func addObserver(NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](nsorderedset/addobserver(_:forkeypath:options:context:).md)
  Raises an exception.
- [func removeObserver(NSObject, forKeyPath: String)](nsorderedset/removeobserver(_:forkeypath:).md)
  Raises an exception.
- [func removeObserver(NSObject, forKeyPath: String, context: UnsafeMutableRawPointer?)](nsorderedset/removeobserver(_:forkeypath:context:).md)
  Raises an exception.
### Comparing Sets
- [func isEqual(to: NSOrderedSet) -> Bool](nsorderedset/isequal(to:).md)
  Compares the receiving ordered set to another ordered set.
- [func intersects(NSOrderedSet) -> Bool](nsorderedset/intersects(_:).md)
  Returns a Boolean value that indicates whether at least one object in the receiving ordered set is also present in another given ordered set.
- [func intersectsSet(Set<AnyHashable>) -> Bool](nsorderedset/intersectsset(_:).md)
  Returns a Boolean value that indicates whether at least one object in the receiving ordered set is also present in another given set.
- [func isSubset(of: NSOrderedSet) -> Bool](nsorderedset/issubset(of:)-7brc.md)
  Returns a Boolean value that indicates whether every object in the receiving ordered set is also present in another given ordered set.
- [func isSubset(of: Set<AnyHashable>) -> Bool](nsorderedset/issubset(of:)-8zx9x.md)
  Returns a Boolean value that indicates whether every object in the receiving ordered set is also present in another given set.
### Creating a Sorted Array
- [func sortedArray(using: [NSSortDescriptor]) -> [Any]](nsorderedset/sortedarray(using:).md)
  Returns an array of the ordered set’s elements sorted as specified by a given array of sort descriptors.
- [func sortedArray(comparator: (Any, Any) -> ComparisonResult) -> [Any]](nsorderedset/sortedarray(comparator:).md)
  Returns an array that lists the receiving ordered set’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block
- [func sortedArray(options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult) -> [Any]](nsorderedset/sortedarray(options:usingcomparator:).md)
  Returns an array that lists the receiving ordered set’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.
### Filtering Ordered Sets
- [func filtered(using: NSPredicate) -> NSOrderedSet](nsorderedset/filtered(using:).md)
  Evaluates a given predicate against each object in the receiving ordered set and returns a new ordered set containing the objects for which the predicate returns true.
### Describing a Set
- [var description: String](nsorderedset/description.md)
  A string that represents the contents of the ordered set, formatted as a property list.
- [func description(withLocale: Any?) -> String](nsorderedset/description(withlocale:).md)
  Returns a string that represents the contents of the ordered set, formatted as a property list.
- [func description(withLocale: Any?, indent: Int) -> String](nsorderedset/description(withlocale:indent:).md)
  Returns a string that represents the contents of the ordered set, formatted as a property list.
### Converting Other Collections
- [var array: [Any]](nsorderedset/array.md)
  A representation of the ordered set as an array.
- [var set: Set<AnyHashable>](nsorderedset/set.md)
  A representation of the set containing the contents of the ordered set.
### Comparing with Another Set
- [class NSOrderedCollectionDifference](nsorderedcollectiondifference.md)
  An object representing the difference between two ordered collections.
- [struct NSOrderedCollectionDifferenceCalculationOptions](nsorderedcollectiondifferencecalculationoptions.md)
  Constants that specify the options to use when creating an ordered collection difference.
### Initializers
- [init?(coder: NSCoder)](nsorderedset/init(coder:).md)
- [convenience init(objects: Any...)](nsorderedset/init(objects:).md)
### Default Implementations
- [Sequence Implementations](nsorderedset/sequence-implementations.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSMutableOrderedSet](nsmutableorderedset.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSFastEnumeration](nsfastenumeration.md)
- [NSMutableCopying](nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [class NSCountedSet](nscountedset.md)
  A mutable, unordered collection of distinct objects that may appear more than once in the collection.
- [class NSMutableOrderedSet](nsmutableorderedset.md)
  A dynamic, ordered collection of unique objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset)*