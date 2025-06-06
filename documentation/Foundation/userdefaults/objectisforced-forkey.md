# objectIsForced(forKey:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value indicating whether the specified key is managed by an administrator.

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
func objectIsForced(forKey key: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the value of the specified key is managed by an administrator, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method assumes that the key is a preference associated with the current user and application. For managed keys, the application should disable any user interface that allows the user to modify the value of `key`.

## Parameters

- `key`: The key whose status you want to check.

## See Also

- [func objectIsForced(forKey: String, inDomain: String) -> Bool](userdefaults/objectisforced(forkey:indomain:).md)
  Returns a Boolean value indicating whether the key in the specified domain is managed by an administrator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/objectisforced(forkey:))*