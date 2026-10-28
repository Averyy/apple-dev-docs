# enumerateObjects(at:options:using:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Executes a given block using the objects in the array at the specified indexes.

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
func enumerateObjects(at s: IndexSet, options opts: NSEnumerationOptions = [], using block: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)
```

```objc
- (void) enumerateObjectsAtIndexes:(NSIndexSet *) s options:(NSEnumerationOptions) opts usingBlock:(void (^)(ObjectType obj, NSUInteger idx, BOOL *stop)) block;
```

## Discussion

By default, the enumeration starts with the first object and continues serially through the array to the last element specified by `indexSet`. You can specify `NSEnumerationConcurrent` and/or `NSEnumerationReverse` as enumeration options to modify this behavior.

This method executes synchronously.

> ❗ **Important**:  If the block parameter or the `indexSet` is `nil` this method will raise an exception.

## Parameters

- `s`: The indexes of the objects over which to enumerate.
- `opts`: A bit mask that specifies the options for the enumeration (whether it should be performed concurrently and whether it should be performed in reverse order).
- `block`: The block to apply to elements in the array.

  The block takes three arguments:

  - **obj**: The element in the array.
  - **idx**: The index of the element in the array.
  - **stop**: A reference to a Boolean value. The block can set the value to [`true`](../../Swift/true.md) to stop further enumeration of the array. If a block stops further enumeration, that block continues to run until it’s finished. When the `NSEnumerationConcurrent` enumeration option is specified, enumeration stops after all of the currently running blocks finish. The `stop` argument is an out-only argument. You should only ever set this Boolean to [`true`](../../Swift/true.md) within the block.

## See Also

### Sending Messages to Elements
- [func enumerateObjects((Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateobjects%28_%29.md)
  Executes a given closure or block using each object in the array, starting with the first object and continuing through the array to the last object.
- [func enumerateObjects(options: NSEnumerationOptions, using: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateobjects%28options,using%29.md)
  Executes a given closure or block using each object in the array with the specified options.
### Related Documentation
- [- makeObjectsPerformSelector:](./makeobjectsperformselector_.md)
  Sends to each object in the array the message identified by a given selector, starting with the first object and continuing through the array to the last object.
- [- makeObjectsPerformSelector:withObject:](./makeobjectsperformselector_withobject_.md)
  Sends the `aSelector` message to each object in the array, starting with the first object and continuing through the array to the last object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/enumerateobjects(at:options:using:))*