# hash(into:)

**Framework**: ExtensionFoundation  
**Kind**: method  
**Role**: Instance Method

Hashes the essential components of the extension by feeding them into the given hash function.

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
func hash(into hasher: inout Hasher)
```

## Parameters

- `hasher`: The hash function to use when combining the components of the extension.

## See Also

### Comparing app extensions
- [static func == (AppExtensionIdentity, AppExtensionIdentity) -> Bool](./eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two identities are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity/hash(into:))*