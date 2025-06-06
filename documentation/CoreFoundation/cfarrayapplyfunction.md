# CFArrayApplyFunction(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Calls a function once for each element in range in an array.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFArrayApplyFunction(_ theArray: CFArray!, _ range: CFRange, _ applier: ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void)!, _ context: UnsafeMutableRawPointer!)
```

#### Discussion

While this function iterates over a mutable collection, it is unsafe for the `applier` function to change the contents of the collection.

## Parameters

- `theArray`: The array to whose elements to apply the function.
- `range`: The range of values within   to which to apply the   function. The range must not exceed the bounds of  . The range may be empty (length  ).
- `applier`: The callback function to call once for each value in the given range in  . If there are values in the range that the   function does not expect or cannot properly apply to, the behavior is undefined.
- `context`: A pointer-sized program-defined value, which is passed as the second argument to the   function, but is otherwise unused by this function. If the context is not what is expected by the applier function, the behavior is undefined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarrayapplyfunction(_:_:_:_:))*