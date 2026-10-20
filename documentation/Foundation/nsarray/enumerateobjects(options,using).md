# enumerateObjects(options:using:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Executes a given closure or block using each object in the array with the specified options.

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
func enumerateObjects(options opts: NSEnumerationOptions = [], using block: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)
```

```objc
- (void) enumerateObjectsWithOptions:(NSEnumerationOptions) opts usingBlock:(void (^)(ObjectType obj, NSUInteger idx, BOOL *stop)) block;
```

#### Discussion

This method executes synchronously. By default, the enumeration starts with the first object and continues serially through the array to the last object. You can specify [`concurrent`](../nsenumerationoptions/concurrent.md) and/or [`reverse`](../nsenumerationoptions/reverse.md) as enumeration options to modify this behavior.

## Parameters

- `opts`: The options for the enumeration. For possible values, see [`NSEnumerationOptions`](../nsenumerationoptions.md).
- `block`: A closure or block to execute for each object in the array, taking three arguments:

  - The object.
  - The index of the object in the array.
  - A reference to a Boolean value, which the closure can set to [`true`](../../Swift/true.md) in order to stop further enumeration of the array. If a closure stops further enumeration, that closure continues to run until it’s finished. When the [`concurrent`](../nsenumerationoptions/concurrent.md) enumeration option is specified, enumeration stops after all of the currently running closures finish.

## See Also

### Sending Messages to Elements
- [func enumerateObjects((Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateobjects%28_%29.md)
  Executes a given closure or block using each object in the array, starting with the first object and continuing through the array to the last object.
- [func enumerateObjects(at: IndexSet, options: NSEnumerationOptions, using: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateobjects%28at,options,using%29.md)
  Executes a given block using the objects in the array at the specified indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/enumerateobjects(options:using:))*