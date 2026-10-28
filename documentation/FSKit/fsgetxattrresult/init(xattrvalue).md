# init(xattrValue:)

**Framework**: FSKit  
**Kind**: init  
**Role**: Initializer

Creates a result for an extended-attribute-getting operation.

**Availability**:
- macOS 27.0+

## Declaration

```swift
init?(xattrValue value: Data)
```

```objc
- (instancetype) initWithXattrValue:(NSData *) value;
```

## Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `value`: The extended attribute value for the requested attribute name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsgetxattrresult/init(xattrvalue:))*