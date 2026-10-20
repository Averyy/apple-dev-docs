# ==(_:_:)

**Framework**: ExtensionFoundation  
**Kind**: op  
**Role**: Operator

Returns a Boolean value that indicates whether two identities are equal.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 13.0+
- tvOS 26.0+
- visionOS 1.1+
- watchOS 26.0+

## Declaration

```swift
static func == (lhs: AppExtensionIdentity, rhs: AppExtensionIdentity) -> Bool
```

#### Return Value

`true` if the items are equal, or `false` if they aren’t.

## Parameters

- `lhs`: The first identity to compare.
- `rhs`: The second identity to compare.

## See Also

### Comparing app extensions
- [func hash(into: inout Hasher)](./hash%28into%29.md)
  Hashes the essential components of the extension by feeding them into the given hash function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity/==(_:_:))*