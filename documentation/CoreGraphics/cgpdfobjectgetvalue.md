# CGPDFObjectGetValue(_:_:_:)

**Framework**: Core Graphics  
**Kind**: func

Returns whether an object is of a given type and if it is, retrieves its value.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGPDFObjectGetValue(_ object: CGPDFObjectRef, _ type: CGPDFObjectType, _ value: UnsafeMutableRawPointer?) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/swift/true) if the specified object is a PDF object of the specified type, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The function gets the value of the `object` parameter. If the type of `object` is equal to the type specified, then:

- If the `value` parameter is not a null pointer, then the value of `object` is copied to `value`, and the function returns [`true`](https://developer.apple.com/documentation/swift/true).
- If the `value` parameter is a null pointer, then the function simply returns [`true`](https://developer.apple.com/documentation/swift/true). This allows you to test whether `object` is of the type specified.

If the type of `object` is [`CGPDFObjectType.integer`](cgpdfobjecttype/integer.md) and `type` is equal to [`CGPDFObjectType.real`](cgpdfobjecttype/real.md), then the value of `object` is converted to floating point, the result copied to `value`, and the function returns [`true`](https://developer.apple.com/documentation/swift/true). If none of the preceding conditions is met, returns [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `object`: A PDF object.
- `type`: A PDF object type.
- `value`: If the   parameter is a PDF object of the specified type, then on return contains that object, otherwise the value is unspecified.

## See Also

- [func CGPDFObjectGetType(CGPDFObjectRef) -> CGPDFObjectType](cgpdfobjectgettype(_:).md)
  Returns the PDF type identifier of an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfobjectgetvalue(_:_:_:))*