# customTypeName

**Framework**: ClassKit  
**Kind**: property

An optional name that the system presents to the user if you choose the custom context type.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var customTypeName: String? { get set }
```

#### Discussion

The system ignores the value of this property unless you set the context’s [`type`](clscontext/type.md) property to [`CLSContextType.custom`](clscontexttype/custom.md). If you do set the type name, provide a localized value.

If you use a custom context type but don’t set the type name, the system presents a default, localized string instead.

## See Also

- [var type: CLSContextType](clscontext/type.md)
  The kind of content a context represents.
- [func setType(CLSContextType)](clscontext/settype(_:).md)
  Updates the kind of content that a context represents.
- [enum CLSContextType](clscontexttype.md)
  The kinds of assignable content a context can contain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/customtypename)*