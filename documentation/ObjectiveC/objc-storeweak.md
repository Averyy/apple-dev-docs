# objc_storeWeak(_:_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Stores a new value in a `__weak` variable.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func objc_storeWeak(_ location: AutoreleasingUnsafeMutablePointer<AnyObject?>, _ obj: Any?) -> Any?
```

#### Return Value

The value stored in `location` (that is, `obj`).

#### Discussion

This function is typically used anywhere a `__weak` variable is the target of an assignment.

## Parameters

- `location`: The address of the weak pointer.
- `obj`: The new object you want the weak pointer to now point to.

## See Also

- [func objc_enumerationMutation(Any)](objc_enumerationmutation(_:).md)
  Inserted by the compiler when a mutation is detected during a foreach iteration.
- [func objc_setEnumerationMutationHandler(((Any) -> Void)?)](objc_setenumerationmutationhandler(_:).md)
  Sets the current mutation handler.
- [func imp_implementationWithBlock(Any) -> IMP](imp_implementationwithblock(_:).md)
  Creates a pointer to a function that calls the specified block when the method is called.
- [func imp_getBlock(IMP) -> Any?](imp_getblock(_:).md)
  Returns the block associated with an `IMP` that was created using [`imp_implementationWithBlock(_:)`](imp_implementationwithblock(_:).md).
- [func imp_removeBlock(IMP) -> Bool](imp_removeblock(_:).md)
  Disassociates a block from an `IMP` that was created using [`imp_implementationWithBlock(_:)`](imp_implementationwithblock(_:).md), and releases the copy of the block that was created.
- [func objc_loadWeak(AutoreleasingUnsafeMutablePointer<AnyObject?>) -> Any?](objc_loadweak(_:).md)
  Loads the object referenced by a weak pointer and returns it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_storeweak(_:_:))*