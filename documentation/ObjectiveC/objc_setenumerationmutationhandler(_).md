# objc_setEnumerationMutationHandler(_:)

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

Sets the current mutation handler.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func objc_setEnumerationMutationHandler(_ handler: ((Any) -> Void)?)
```

```c
extern void objc_setEnumerationMutationHandler(void (*)(id)handler);
```

## Parameters

- `handler`: A function pointer to the new mutation handler.

## See Also

### Using Objective-C Language Features
- [func objc_enumerationMutation(Any)](./objc_enumerationmutation%28_%29.md)
  Inserted by the compiler when a mutation is detected during a foreach iteration.
- [func imp_implementationWithBlock(Any) -> IMP](./imp_implementationwithblock%28_%29.md)
  Creates a pointer to a function that calls the specified block when the method is called.
- [func imp_getBlock(IMP) -> Any?](./imp_getblock%28_%29.md)
  Returns the block associated with an `IMP` that was created using [`imp_implementationWithBlock(_:)`](./imp_implementationwithblock%28_%29.md).
- [func imp_removeBlock(IMP) -> Bool](./imp_removeblock%28_%29.md)
  Disassociates a block from an `IMP` that was created using [`imp_implementationWithBlock(_:)`](./imp_implementationwithblock%28_%29.md), and releases the copy of the block that was created.
- [func objc_loadWeak(AutoreleasingUnsafeMutablePointer<AnyObject?>) -> Any?](./objc_loadweak%28_%29.md)
  Loads the object referenced by a weak pointer and returns it.
- [func objc_storeWeak(AutoreleasingUnsafeMutablePointer<AnyObject?>, Any?) -> Any?](./objc_storeweak%28_,_%29.md)
  Stores a new value in a `__weak` variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_setenumerationmutationhandler(_:))*