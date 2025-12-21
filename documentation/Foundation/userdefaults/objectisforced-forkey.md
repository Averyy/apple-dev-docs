# objectIsForced(forKey:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates whether an administrator provided the value for the specified key.

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

`true` if an administrator provides a value for the key, otherwise `false`.

#### Discussion

Apps can’t change the value of managed keys, so use this method to determine if you can make changes to one of your app-specific keys. If a key is managed, disable any app-specific UI you use to change the value of that key.

## Parameters

- `key`: The name of the key to check.

## See Also

- [func objectIsForced(forKey: String, inDomain: String) -> Bool](userdefaults/objectisforced(forkey:indomain:).md)
  Returns a Boolean value that indicates whether an administrator provided the value for the key in the specified domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/objectisforced(forkey:))*