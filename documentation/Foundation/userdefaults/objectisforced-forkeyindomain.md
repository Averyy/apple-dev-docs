# objectIsForced(forKey:inDomain:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value indicating whether the key in the specified domain is managed by an administrator.

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

[`true`](https://developer.apple.com/documentation/swift/true) if the key is managed by an administrator in the specified domain, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method assumes that the key is a preference associated with the current user. For managed keys, the application should disable any user interface that allows the user to modify the value of `key`.

## Parameters

- `key`: The key whose status you want to check.
- `domain`: The domain of the key.

## See Also

- [func objectIsForced(forKey: String) -> Bool](userdefaults/objectisforced(forkey:).md)
  Returns a Boolean value indicating whether the specified key is managed by an administrator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/objectisforced(forkey:indomain:))*