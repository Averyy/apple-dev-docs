# pointerArrayWithPointerFunctions:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

A new pointer array initialized to use the given functions.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (NSPointerArray *) pointerArrayWithPointerFunctions:(NSPointerFunctions *) functions;
```

## Return Value

A new pointer array initialized to use the given pointer functions.

## Parameters

- `functions`: The pointer functions for the new instance.

## See Also

### Creating and Initializing a New Pointer Array
- [init(options: NSPointerFunctions.Options)](./init%28options%29.md)
  Initializes the receiver to use the given options.
- [init(pointerFunctions: NSPointerFunctions)](./init%28pointerfunctions%29.md)
  Initializes the receiver to use the given functions.
- [+ pointerArrayWithOptions:](./pointerarraywithoptions_.md)
  Returns a new pointer array initialized to use the given options.
- [class func strongObjects() -> NSPointerArray](./strongobjects%28%29.md)
  Returns a new pointer array that maintains strong references to its elements.
- [+ pointerArrayWithStrongObjects](./pointerarraywithstrongobjects.md)
  Returns a new pointer array that maintains strong references to its elements.
- [class func weakObjects() -> NSPointerArray](./weakobjects%28%29.md)
  Returns a new pointer array that maintains weak references to its elements.
- [+ pointerArrayWithWeakObjects](./pointerarraywithweakobjects.md)
  Returns a new pointer array that maintains weak references to its elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerarray/pointerarraywithpointerfunctions:)*