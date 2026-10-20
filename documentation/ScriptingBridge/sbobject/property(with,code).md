# property(with:code:)

**Framework**: Scripting Bridge  
**Kind**: method  
**Role**: Instance Method

Returns an object of the designated scripting class representing the specified property of the receiver

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
func property(with cls: AnyClass, code: AEKeyword) -> SBObject
```

```objc
- (SBObject *) propertyWithClass:(Class) cls code:(AEKeyword) code;
```

#### Return Value

An instance of the designated `class` that represents the receiver’s property identified by `code`.

#### Discussion

`SBObject` subclasses use this method to implement application-specific property accessor methods. You should not need to call this method directly.

> **Note**: This method doesn’t retrieve the value of the property. To get the value, call [`get()`](./get%28%29.md).

## Parameters

- `code`: A four-character code that uniquely identifies a property of the receiver.

## See Also

### Getting Properties and Elements
- [func property(withCode: AEKeyword) -> SBObject](./property%28withcode%29.md)
  Returns an object representing the specified property of the receiver.
- [func elementArray(withCode: DescType) -> SBElementArray](./elementarray%28withcode%29.md)
  Returns an array containing every child of the receiver with the given class-type code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbobject/property(with:code:))*