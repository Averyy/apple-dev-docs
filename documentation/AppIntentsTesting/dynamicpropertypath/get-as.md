# get(as:)

**Framework**: App Intents Testing  
**Kind**: method

Resolves the value at this path, fetching it from the app if it was deferred.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)
- Mac Catalyst 27.2+ (Beta)
- macOS 27.2+ (Beta)
- tvOS 27.2+ (Beta)
- visionOS 27.2+ (Beta)
- watchOS 27.2+ (Beta)

## Declaration

```swift
func get<T>(as type: T.Type = T.self) async throws -> T where T : IntentValueConvertible
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/dynamicpropertypath/get(as:))*