# imp_getBlock(_:)

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

Returns the block associated with an `IMP` that was created using [`imp_implementationWithBlock(_:)`](./imp_implementationwithblock%28_%29.md).

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func imp_getBlock(_ anImp: IMP) -> Any?
```

```c
extern idimp_getBlock(IMP anImp);
```

#### Return Value

The block called by `anImp`.

## Parameters

- `anImp`: The [`IMP`](./imp.md) that calls this block.

## See Also

### Using Objective-C Language Features
- [func objc_enumerationMutation(Any)](./objc_enumerationmutation%28_%29.md)
  Inserted by the compiler when a mutation is detected during a foreach iteration.
- [func objc_setEnumerationMutationHandler(((Any) -> Void)?)](./objc_setenumerationmutationhandler%28_%29.md)
  Sets the current mutation handler.
- [func imp_implementationWithBlock(Any) -> IMP](./imp_implementationwithblock%28_%29.md)
  Creates a pointer to a function that calls the specified block when the method is called.
- [func imp_removeBlock(IMP) -> Bool](./imp_removeblock%28_%29.md)
  Disassociates a block from an `IMP` that was created using [`imp_implementationWithBlock(_:)`](./imp_implementationwithblock%28_%29.md), and releases the copy of the block that was created.
- [func objc_loadWeak(AutoreleasingUnsafeMutablePointer<AnyObject?>) -> Any?](./objc_loadweak%28_%29.md)
  Loads the object referenced by a weak pointer and returns it.
- [func objc_storeWeak(AutoreleasingUnsafeMutablePointer<AnyObject?>, Any?) -> Any?](./objc_storeweak%28_,_%29.md)
  Stores a new value in a `__weak` variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/imp_getblock(_:))*