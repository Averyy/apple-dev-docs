# init(options:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes the receiver to use the given options.

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
init(options: NSPointerFunctions.Options = [])
```

```objc
- (instancetype) initWithOptions:(NSPointerFunctionsOptions) options;
```

#### Return Value

The receiver, initialized to use the given options.

## Parameters

- `options`: The pointer functions options for the new instance.

## See Also

### Related Documentation
- [Collections Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Collections.html#//apple_ref/doc/uid/10000034i)
- [+ pointerArrayWithOptions:](./pointerarraywithoptions_.md)
  Returns a new pointer array initialized to use the given options.
- [+ pointerArrayWithPointerFunctions:](./pointerarraywithpointerfunctions_.md)
  A new pointer array initialized to use the given functions.
### Creating and Initializing a New Pointer Array
- [init(pointerFunctions: NSPointerFunctions)](./init%28pointerfunctions%29.md)
  Initializes the receiver to use the given functions.
- [class func strongObjects() -> NSPointerArray](./strongobjects%28%29.md)
  Returns a new pointer array that maintains strong references to its elements.
- [class func weakObjects() -> NSPointerArray](./weakobjects%28%29.md)
  Returns a new pointer array that maintains weak references to its elements.
- [+ pointerArrayWithStrongObjects](./pointerarraywithstrongobjects.md)
  Returns a new pointer array that maintains strong references to its elements.
- [+ pointerArrayWithWeakObjects](./pointerarraywithweakobjects.md)
  Returns a new pointer array that maintains weak references to its elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerarray/init(options:))*