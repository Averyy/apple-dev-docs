# elementArray(withCode:)

**Framework**: Scripting Bridge  
**Kind**: method  
**Role**: Instance Method

Returns an array containing every child of the receiver with the given class-type code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
func elementArray(withCode code: DescType) -> SBElementArray
```

```objc
- (SBElementArray *) elementArrayWithCode:(DescType) code;
```

## Return Value

An [`SBElementArray`](../sbelementarray.md) object containing every child of the receiver whose class matches `code`.

## Discussion

`SBObject` subclasses use this method to implement application-specific property accessor methods. You should not need to call this method directly.

> **Note**: This method doesn’t retrieve the value of the property. To get the value, call [`get()`](./get%28%29.md).

## Parameters

- `code`: A four-character code that identifies a scripting class.

## See Also

### Getting Properties and Elements
- [func property(with: AnyClass, code: AEKeyword) -> SBObject](./property%28with,code%29.md)
  Returns an object of the designated scripting class representing the specified property of the receiver
- [func property(withCode: AEKeyword) -> SBObject](./property%28withcode%29.md)
  Returns an object representing the specified property of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbobject/elementarray(withcode:))*