# subscript(dynamicMember:)

**Framework**: App Intents Testing  
**Kind**: subscript

Accesses a typed property at the current path by name.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
subscript<T>(dynamicMember identifier: String) -> T where T : IntentValueConvertible { get throws }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/dynamicpropertypath/subscript(dynamicmember:)-lizi)*