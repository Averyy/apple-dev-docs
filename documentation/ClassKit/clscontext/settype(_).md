# setType(_:)

**Framework**: ClassKit  
**Kind**: method  
**Role**: Instance Method

Updates the kind of content that a context represents.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func setType(_ type: CLSContextType)
```

```objc
- (void) setType:(CLSContextType) type;
```

## Discussion

Use this method to change the [`type`](./type.md) property of a context that you’ve already created.

## Parameters

- `type`: A new value for the kind of content that the context represents.

## See Also

### Managing the context type
- [var type: CLSContextType](./type.md)
  The kind of content a context represents.
- [enum CLSContextType](../clscontexttype.md)
  The kinds of assignable content a context can contain.
- [var customTypeName: String?](./customtypename.md)
  An optional name that the system presents to the user if you choose the custom context type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/settype(_:))*