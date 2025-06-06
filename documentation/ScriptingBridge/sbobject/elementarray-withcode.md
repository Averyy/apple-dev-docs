# elementArray(withCode:)

**Framework**: Scripting Bridge  
**Kind**: method

Returns an array containing every child of the receiver with the given class-type code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
func elementArray(withCode code: DescType) -> SBElementArray
```

#### Return Value

An [`SBElementArray`](sbelementarray.md) object containing every child of the receiver whose class matches `code`.

#### Discussion

`SBObject` subclasses use this method to implement application-specific property accessor methods. You should not need to call this method directly.

> **Note**: This method doesn’t retrieve the value of the property. To get the value, call [`get()`](sbobject/get().md).

This method doesn’t retrieve the value of the property. To get the value, call [`get()`](sbobject/get().md).

## Parameters

- `code`: A four-character code that identifies a scripting class.

## See Also

- [func property(with: AnyClass, code: AEKeyword) -> SBObject](sbobject/property(with:code:).md)
  Returns an object of the designated scripting class representing the specified property of the receiver
- [func property(withCode: AEKeyword) -> SBObject](sbobject/property(withcode:).md)
  Returns an object representing the specified property of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbobject/elementarray(withcode:))*