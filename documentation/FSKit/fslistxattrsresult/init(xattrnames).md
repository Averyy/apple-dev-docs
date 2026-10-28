# init(xattrNames:)

**Framework**: FSKit  
**Kind**: init  
**Role**: Initializer

Creates a result instance with all required properties populated.

**Availability**:
- macOS 27.0+

## Declaration

```swift
init?(xattrNames: [FSFileName])
```

```objc
- (instancetype) initWithXattrNames:(NSArray<FSFileName *> *) xattrNames;
```

## Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `xattrNames`: An array of [`FSFileName`](../fsfilename.md) instances representing the names of all extended attributes currently set on the item.

## See Also

### Creating a list-extended-attributes result
- [class FSFileName](../fsfilename.md)
  The name of a file, expressed as a data buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fslistxattrsresult/init(xattrnames:))*