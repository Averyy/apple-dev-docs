# value(forCustomKey:)

**Framework**: Core Spotlight  
**Kind**: method  
**Role**: Instance Method

Returns the value associated with the specified custom attribute key.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func value(forCustomKey key: CSCustomAttributeKey) -> (any NSSecureCoding)?
```

```objc
- (id<NSSecureCoding>) valueForCustomKey:(CSCustomAttributeKey *) key;
```

## Return Value

The value associated with the custom attribute key.

## Parameters

- `key`: The custom attribute key.

## See Also

### Accessing custom attributes
- [func setValue((any NSSecureCoding)?, forCustomKey: CSCustomAttributeKey)](./setvalue%28_,forcustomkey%29.md)
  Sets the value for a custom attribute key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/value(forcustomkey:))*