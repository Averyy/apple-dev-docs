# objc_enumerationMutation(_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Inserted by the compiler when a mutation is detected during a foreach iteration.

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
func objc_enumerationMutation(_ obj: Any)
```

#### Discussion

The compiler inserts this function when it detects that an object is mutated during a foreach iteration. The function is called when a mutation occurs, and the enumeration mutation handler is enacted if it is set up (via the [`objc_setEnumerationMutationHandler(_:)`](objc_setenumerationmutationhandler(_:).md) function). If the handler is not set up, a fatal error occurs.

## Parameters

- `obj`: The object being mutated.

## See Also

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
- [func objc_storeWeak(AutoreleasingUnsafeMutablePointer<AnyObject?>, Any?) -> Any?](objc_storeweak(_:_:).md)
  Stores a new value in a `__weak` variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_enumerationmutation(_:))*