# setWithObjects:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns a set containing the objects in a given argument list.

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
+ (instancetype) setWithObjects:(ObjectType) firstObj;
```

## Return Value

A new set containing the objects in the argument list.

## Discussion

To add additional objects to the new set, pass a comma-separated list of trailing variadic arguments, ending with `nil`.  If the same object appears more than once in the list of objects, it is added only once to the returned set. Each object receives a [`retain`](../../ObjectiveC/nsobject-c.protocol/retain.md) message as it is added to the set.

As an example, the following code excerpt creates a set containing three different types of elements (assuming `aPath` exits):

```objc
NSSet *mySet;
NSData *someData = [NSData dataWithContentsOfFile:aPath];
NSValue *aValue = [NSNumber numberWithInteger:5];
NSString *aString = @"a string";
 
mySet = [NSSet setWithObjects:someData, aValue, aString, nil];
```

## Parameters

- `firstObj`: The first object to add to the new set.

## See Also

### Creating a Set
- [+ set](./set.md)
  Creates and returns an empty set.
- [+ setWithArray:](./setwitharray_.md)
  Creates and returns a set containing a uniqued collection of the objects contained in a given array.
- [convenience init(object: Any)](./init%28object%29.md)
  Creates and returns a set that contains a single given object.
- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](./init%28objects,count%29-65ni4.md)
  Creates and returns a set containing a specified number of objects from a given C array of objects.
- [+ setWithSet:](./setwithset_.md)
  Creates and returns a set containing the objects from another set.
- [func adding(Any) -> Set<AnyHashable>](./adding%28_%29.md)
  Returns a new set formed by adding a given object to the receiving set.
- [func addingObjects(from: Set<AnyHashable>) -> Set<AnyHashable>](./addingobjects%28from%29-2i31h.md)
  Returns a new set formed by adding the objects in a given set to the receiving set.
- [func addingObjects(from: [Any]) -> Set<AnyHashable>](./addingobjects%28from%29-544m9.md)
  Returns a new set formed by adding the objects in a given array to the receiving set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/setwithobjects:)*