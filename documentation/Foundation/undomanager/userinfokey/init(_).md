# init(_:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a user info key from the given string.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(_ rawValue: String)
```

## Discussion

Don’t use this initializer. Instead, extend the [`UndoManager.UserInfoKey`](../userinfokey.md) namespace as follows:

```swift
extension UndoManager.UserInfoKey {
    static let icon: UndoManager.UserInfoKey = "icon"
}
```

## Parameters

- `rawValue`: The raw value string.

## See Also

### Creating a user info key from a raw value
- [init(rawValue: String)](./init%28rawvalue%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/userinfokey/init(_:))*