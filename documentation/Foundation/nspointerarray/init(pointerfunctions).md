# init(pointerFunctions:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes the receiver to use the given functions.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(pointerFunctions functions: NSPointerFunctions)
```

```objc
- (instancetype) initWithPointerFunctions:(NSPointerFunctions *) functions;
```

#### Return Value

The receiver, initialized to use the given functions.

## Parameters

- `functions`: The pointer functions for the new instance.

## See Also

### Creating and Initializing a New Pointer Array
- [init(options: NSPointerFunctions.Options)](./init%28options%29.md)
  Initializes the receiver to use the given options.
- [class func strongObjects() -> NSPointerArray](./strongobjects%28%29.md)
  Returns a new pointer array that maintains strong references to its elements.
- [class func weakObjects() -> NSPointerArray](./weakobjects%28%29.md)
  Returns a new pointer array that maintains weak references to its elements.
- [+ pointerArrayWithStrongObjects](./pointerarraywithstrongobjects.md)
  Returns a new pointer array that maintains strong references to its elements.
- [+ pointerArrayWithWeakObjects](./pointerarraywithweakobjects.md)
  Returns a new pointer array that maintains weak references to its elements.
### Related Documentation
- [+ pointerArrayWithOptions:](./pointerarraywithoptions_.md)
  Returns a new pointer array initialized to use the given options.
- [+ pointerArrayWithPointerFunctions:](./pointerarraywithpointerfunctions_.md)
  A new pointer array initialized to use the given functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerarray/init(pointerfunctions:))*