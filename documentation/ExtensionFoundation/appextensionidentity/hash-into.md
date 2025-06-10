# hash(into:)

**Framework**: ExtensionFoundation  
**Kind**: method

Hashes the essential components of the extension by feeding them into the given hash function.

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
func hash(into hasher: inout Hasher)
```

## Parameters

- `hasher`: The hash function to use when combining the components of the color parameter.

## See Also

- [static func == (AppExtensionIdentity, AppExtensionIdentity) -> Bool](appextensionidentity/==(_:_:).md)
  Indicates whether two extensions are equal


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity/hash(into:))*