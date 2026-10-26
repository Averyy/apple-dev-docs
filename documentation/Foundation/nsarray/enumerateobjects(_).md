# enumerateObjects(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Executes a given closure or block using each object in the array, starting with the first object and continuing through the array to the last object.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func enumerateObjects(_ block: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)
```

```objc
- (void) enumerateObjectsUsingBlock:(void (^)(ObjectType obj, NSUInteger idx, BOOL *stop)) block;
```

#### Discussion

This method executes synchronously. Values allocated within the block are deallocated after the block is executed.

## Parameters

- `block`: A closure or block to execute for each object in the array, taking three arguments:

  - The object.
  - The index of the object in the array.
  - A reference to a Boolean value, which the closure can set to [`true`](../../Swift/true.md) in order to stop further enumeration of the array. If a closure stops further enumeration, that closure continues to run until it’s finished.

## See Also

### Sending Messages to Elements
- [func enumerateObjects(options: NSEnumerationOptions, using: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateobjects%28options,using%29.md)
  Executes a given closure or block using each object in the array with the specified options.
- [func enumerateObjects(at: IndexSet, options: NSEnumerationOptions, using: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateobjects%28at,options,using%29.md)
  Executes a given block using the objects in the array at the specified indexes.
### Related Documentation
- [- makeObjectsPerformSelector:](./makeobjectsperformselector_.md)
  Sends to each object in the array the message identified by a given selector, starting with the first object and continuing through the array to the last object.
- [- makeObjectsPerformSelector:withObject:](./makeobjectsperformselector_withobject_.md)
  Sends the `aSelector` message to each object in the array, starting with the first object and continuing through the array to the last object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/enumerateobjects(_:))*