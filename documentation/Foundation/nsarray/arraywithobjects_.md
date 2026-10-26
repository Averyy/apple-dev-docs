# arrayWithObjects:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns an array containing the objects in the argument list.

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
+ (instancetype) arrayWithObjects:(ObjectType) firstObj;
```

#### Return Value

An array containing the objects in the argument list.

#### Discussion

Pass comma-separated list of trailing variadic arguments as additional objects, ending with `nil`.

The following code example creates an array containing three different types of element:

```objc
NSDate *aDate = [NSDate distantFuture];
NSValue *aValue = @(5);
NSString *aString = @"hello";
 
NSArray *array = [NSArray arrayWithObjects:aDate, aValue, aString, nil];
```

Alternatively, you can use array literal syntax in Objective-C or Swift to create an array containing given objects:

```objc
NSArray *array = @[@"alpha", @"bravo", @"charlie"];
```

## Parameters

- `firstObj`: The first object for the array.

## See Also

### Creating an Array
- [+ array](./array.md)
  Creates and returns an empty array.
- [+ arrayWithArray:](./arraywitharray_.md)
  Creates and returns an array containing the objects in another given array.
- [+ arrayWithContentsOfFile:](./arraywithcontentsoffile_.md)
  Creates and returns an array containing the contents of the file specified by a given path.
- [convenience init(object: Any)](./init%28object%29.md)
  Creates and returns an array containing a given object.
- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](./init%28objects,count%29-7dct1.md)
  Creates and returns an array that includes a given number of objects from a given C array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/arraywithobjects:)*