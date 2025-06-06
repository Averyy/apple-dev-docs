# objc_loadWeak(_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Loads the object referenced by a weak pointer and returns it.

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
func objc_loadWeak(_ location: AutoreleasingUnsafeMutablePointer<AnyObject?>) -> Any?
```

#### Return Value

The object pointed to by `location`, or `nil` if `location` is `nil`.

#### Discussion

This function loads the object referenced by a weak pointer and returns it after retaining and autoreleasing the object. As a result, the object stays alive long enough for the caller to use it. This function is typically used anywhere a `__weak` variable is used in an expression.

## Parameters

- `location`: The address of the weak pointer.

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
- [func objc_storeWeak(AutoreleasingUnsafeMutablePointer<AnyObject?>, Any?) -> Any?](objc_storeweak(_:_:).md)
  Stores a new value in a `__weak` variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_loadweak(_:))*