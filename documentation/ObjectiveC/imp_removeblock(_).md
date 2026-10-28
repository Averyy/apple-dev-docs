# imp_removeBlock(_:)

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

Disassociates a block from an `IMP` that was created using [`imp_implementationWithBlock(_:)`](./imp_implementationwithblock%28_%29.md), and releases the copy of the block that was created.

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
func imp_removeBlock(_ anImp: IMP) -> Bool
```

```c
extern BOOL imp_removeBlock(IMP anImp);
```

## Return Value

[`YES`](./yes.md) if the block was released successfully; otherwise, [`NO`](./no.md) (for example, the function returns [`NO`](./no.md) if the block was not used to create `anImp` previously).

## Parameters

- `anImp`: An [`IMP`](./imp.md) that was created using the [`imp_implementationWithBlock(_:)`](./imp_implementationwithblock%28_%29.md) function.

## See Also

### Using Objective-C Language Features
- [func objc_enumerationMutation(Any)](./objc_enumerationmutation%28_%29.md)
  Inserted by the compiler when a mutation is detected during a foreach iteration.
- [func objc_setEnumerationMutationHandler(((Any) -> Void)?)](./objc_setenumerationmutationhandler%28_%29.md)
  Sets the current mutation handler.
- [func imp_implementationWithBlock(Any) -> IMP](./imp_implementationwithblock%28_%29.md)
  Creates a pointer to a function that calls the specified block when the method is called.
- [func imp_getBlock(IMP) -> Any?](./imp_getblock%28_%29.md)
  Returns the block associated with an `IMP` that was created using [`imp_implementationWithBlock(_:)`](./imp_implementationwithblock%28_%29.md).
- [func objc_loadWeak(AutoreleasingUnsafeMutablePointer<AnyObject?>) -> Any?](./objc_loadweak%28_%29.md)
  Loads the object referenced by a weak pointer and returns it.
- [func objc_storeWeak(AutoreleasingUnsafeMutablePointer<AnyObject?>, Any?) -> Any?](./objc_storeweak%28_,_%29.md)
  Stores a new value in a `__weak` variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/imp_removeblock(_:))*