# ==(_:_:)

**Framework**: ExtensionFoundation  
**Kind**: op

Indicates whether two extensions are equal

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 13.0+
- tvOS 26.0+ (Beta)
- visionOS 1.1+
- watchOS 26.0+ (Beta)

## Declaration

```swift
static func == (lhs: AppExtensionIdentity, rhs: AppExtensionIdentity) -> Bool
```

#### Return Value

A Boolean value set to true if the two extension parameters are equal.

## Parameters

- `lhs`: The first extension to compare.
- `rhs`: The second extension to compare.

## See Also

- [func hash(into: inout Hasher)](appextensionidentity/hash(into:).md)
  Hashes the essential components of the extension by feeding them into the given hash function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity/==(_:_:))*