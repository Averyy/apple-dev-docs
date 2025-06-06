# sel_getUid(_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Registers a method name with the Objective-C runtime system.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func sel_getUid(_ str: UnsafePointer<CChar>) -> Selector
```

#### Return Value

A pointer of type [`SEL`](sel.md) specifying the selector for the named method.

#### Discussion

The implementation of this method is identical to the implementation of [`sel_registerName(_:)`](sel_registername(_:).md).

##### Version Notes

Prior to OS X version 10.0, this method tried to find the selector mapped to the given name and returned `NULL` if the selector was not found. This was changed for safety, because it was observed that many of the callers of this function did not check the return value for `NULL`.

## Parameters

- `str`: A pointer to a C string. Pass the name of the method you wish to register.

## See Also

- [func sel_getName(Selector) -> UnsafePointer<CChar>](sel_getname(_:).md)
  Returns the name of the method specified by a given selector.
- [func sel_registerName(UnsafePointer<CChar>) -> Selector](sel_registername(_:).md)
  Registers a method with the Objective-C runtime system, maps the method name to a selector, and returns the selector value.
- [func sel_isEqual(Selector, Selector) -> Bool](sel_isequal(_:_:).md)
  Returns a Boolean value that indicates whether two selectors are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/sel_getuid(_:))*