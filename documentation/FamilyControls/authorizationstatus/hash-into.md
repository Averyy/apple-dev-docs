# hash(into:)

**Framework**: FamilyControls  
**Kind**: method

Hashes the essential components of the authorization status by feeding them into the given hash function.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

## Declaration

```swift
func hash(into hasher: inout Hasher)
```

## Parameters

- `hasher`: The hash function to use when combining the components of the authorization status.

## See Also

- [static func != (Self, Self) -> Bool](authorizationstatus/!=(_:_:).md)
  Returns a Boolean value that indicates whether two authorization statuses aren’t equal.
- [var hashValue: Int](authorizationstatus/hashvalue.md)
  The hashed value of the authorization status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/authorizationstatus/hash(into:))*