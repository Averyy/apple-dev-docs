# property(withCode:)

**Framework**: Scripting Bridge  
**Kind**: method  
**Role**: Instance Method

Returns an object representing the specified property of the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
func property(withCode code: AEKeyword) -> SBObject
```

```objc
- (SBObject *) propertyWithCode:(AEKeyword) code;
```

#### Return Value

An object representing the receiver’s property as identified by `code`.

#### Discussion

`SBObject` subclasses use this method to implement application-specific property accessor methods. You should not need to call this method directly.

## Parameters

- `code`: A four-character code that uniquely identifies a property of the receiver.

## See Also

### Getting Properties and Elements
- [func property(with: AnyClass, code: AEKeyword) -> SBObject](./property%28with,code%29.md)
  Returns an object of the designated scripting class representing the specified property of the receiver
- [func elementArray(withCode: DescType) -> SBElementArray](./elementarray%28withcode%29.md)
  Returns an array containing every child of the receiver with the given class-type code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbobject/property(withcode:))*