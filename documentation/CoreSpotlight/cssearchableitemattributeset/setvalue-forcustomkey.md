# setValue(_:forCustomKey:)

**Framework**: Core Spotlight  
**Kind**: method

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

## Parameters

- `value`: The value of the custom attribute. Values must be common property list types, such as  ,  ,  ,  , or  , or an array of property list types.
- `key`: The custom attribute key.

## See Also

- [func value(forCustomKey: CSCustomAttributeKey) -> (any NSSecureCoding)?](cssearchableitemattributeset/value(forcustomkey:).md)
  Returns the value associated with the specified custom attribute key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/setvalue(_:forcustomkey:))*