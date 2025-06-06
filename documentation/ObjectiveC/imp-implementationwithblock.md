# imp_implementationWithBlock(_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Creates a pointer to a function that calls the specified block when the method is called.

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
func imp_implementationWithBlock(_ block: Any) -> IMP
```

#### Return Value

The [`IMP`](imp.md) that calls `block`. You must dispose of the returned [`IMP`](imp.md) using the function.

## Parameters

- `block`: The block that implements this method. The signature of   should be  . The selector of the method is not available to  .   is copied with  .

## See Also

- [func objc_enumerationMutation(Any)](objc_enumerationmutation(_:).md)
  Inserted by the compiler when a mutation is detected during a foreach iteration.
- [func objc_setEnumerationMutationHandler(((Any) -> Void)?)](objc_setenumerationmutationhandler(_:).md)
  Sets the current mutation handler.
- [func imp_getBlock(IMP) -> Any?](imp_getblock(_:).md)
  Returns the block associated with an `IMP` that was created using [`imp_implementationWithBlock(_:)`](imp_implementationwithblock(_:).md).
- [func imp_removeBlock(IMP) -> Bool](imp_removeblock(_:).md)
  Disassociates a block from an `IMP` that was created using [`imp_implementationWithBlock(_:)`](imp_implementationwithblock(_:).md), and releases the copy of the block that was created.
- [func objc_loadWeak(AutoreleasingUnsafeMutablePointer<AnyObject?>) -> Any?](objc_loadweak(_:).md)
  Loads the object referenced by a weak pointer and returns it.
- [func objc_storeWeak(AutoreleasingUnsafeMutablePointer<AnyObject?>, Any?) -> Any?](objc_storeweak(_:_:).md)
  Stores a new value in a `__weak` variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/imp_implementationwithblock(_:))*