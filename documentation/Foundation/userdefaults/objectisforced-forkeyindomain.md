# objectIsForced(forKey:inDomain:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates whether an administrator provided the value for the key in the specified domain.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func objectIsForced(forKey key: String, inDomain domain: String) -> Bool
```

#### Return Value

`true` if an administrator provides a value for the key, otherwise `false`.

#### Discussion

Apps can’t change the value of managed keys, so use this method to determine if you can make changes to a key in a specific domain. For example, you might use this method to check for overrides of settings belonging to a shared app group. If a key is managed, disable any app-specific UI you use to change the value of that key.

## Parameters

- `key`: The name of the key to check.
- `domain`: The domain that contains the key.

## See Also

- [func objectIsForced(forKey: String) -> Bool](userdefaults/objectisforced(forkey:).md)
  Returns a Boolean value that indicates whether an administrator provided the value for the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/objectisforced(forkey:indomain:))*