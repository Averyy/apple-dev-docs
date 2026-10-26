# makeObjectsPerformSelector:withObject:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sends the `aSelector` message to each object in the array, starting with the first object and continuing through the array to the last object.

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
- (void) makeObjectsPerformSelector:(SEL) aSelector withObject:(id) argument;
```

#### Discussion

This method raises an `NSInvalidArgumentException` if `aSelector` is `NULL`.

## Parameters

- `aSelector`: A selector that identifies the message to send to the objects in the array. The method must take a single argument of type id, and must not have the side effect of modifying the receiving array.
- `argument`: The object to send as the argument to each invocation of the `aSelector` method.

## See Also

### Sending Messages to Elements
- [- makeObjectsPerformSelector:](./makeobjectsperformselector_.md)
  Sends to each object in the array the message identified by a given selector, starting with the first object and continuing through the array to the last object.
- [func enumerateObjects((Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateobjects%28_%29.md)
  Executes a given closure or block using each object in the array, starting with the first object and continuing through the array to the last object.
- [func enumerateObjects(options: NSEnumerationOptions, using: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateobjects%28options,using%29.md)
  Executes a given closure or block using each object in the array with the specified options.
- [func enumerateObjects(at: IndexSet, options: NSEnumerationOptions, using: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateobjects%28at,options,using%29.md)
  Executes a given block using the objects in the array at the specified indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/makeobjectsperformselector:withobject:)*