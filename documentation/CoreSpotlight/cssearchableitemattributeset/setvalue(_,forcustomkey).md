# setValue(_:forCustomKey:)

**Framework**: Core Spotlight  
**Kind**: method  
**Role**: Instance Method

Sets the value for a custom attribute key.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func setValue(_ value: (any NSSecureCoding)?, forCustomKey key: CSCustomAttributeKey)
```

```objc
- (void) setValue:(id<NSSecureCoding>) value forCustomKey:(CSCustomAttributeKey *) key;
```

## Parameters

- `value`: The value of the custom attribute. Values must be common property list types, such as [`NSString`](../../Foundation/nsstring.md), [`NSNumber`](../../Foundation/nsnumber.md), [`NSNull`](../../Foundation/nsnull.md), [`NSData`](../../Foundation/nsdata.md), or [`NSDate`](../../Foundation/nsdate.md), or an array of property list types.
- `key`: The custom attribute key.

## See Also

### Accessing custom attributes
- [func value(forCustomKey: CSCustomAttributeKey) -> (any NSSecureCoding)?](./value%28forcustomkey%29.md)
  Returns the value associated with the specified custom attribute key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/setvalue(_:forcustomkey:))*