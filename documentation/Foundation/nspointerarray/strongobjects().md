# strongObjects()

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a new pointer array that maintains strong references to its elements.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func strongObjects() -> NSPointerArray
```

```objc
+ (NSPointerArray *) strongObjectsPointerArray;
```

#### Return Value

A new pointer array that maintains strong references to its elements.

## See Also

### Creating and Initializing a New Pointer Array
- [init(options: NSPointerFunctions.Options)](./init%28options%29.md)
  Initializes the receiver to use the given options.
- [init(pointerFunctions: NSPointerFunctions)](./init%28pointerfunctions%29.md)
  Initializes the receiver to use the given functions.
- [class func weakObjects() -> NSPointerArray](./weakobjects%28%29.md)
  Returns a new pointer array that maintains weak references to its elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerarray/strongobjects())*