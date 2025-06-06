# removeObject(forKey:)

**Framework**: Foundation  
**Kind**: method

Removes the value of the specified default key.

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
func removeObject(forKey defaultName: String)
```

#### Discussion

Removing a default has no effect on the value returned by the [`object(forKey:)`](userdefaults/object(forkey:).md) method if the same key exists in a domain that precedes the standard application domain in the search list.

## Parameters

- `defaultName`: The key whose value you want to remove.

## See Also

- [func set(Any?, forKey: String)](userdefaults/set(_:forkey:)-8ab6d.md)
  Sets the value of the specified default key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/removeobject(forkey:))*