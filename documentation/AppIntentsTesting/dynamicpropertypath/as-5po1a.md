# as(_:)

**Framework**: App Intents Testing  
**Kind**: method

Casts a property to the provided type.

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
func `as`<T>(_ type: T.Type) throws -> T where T : IntentValueConvertible
```

#### Discussion

If the value’s type doesn’t match, this method throws an error.

```swift
let result = try await intent.run()
try result.value.as(String.self) == "My Name"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/dynamicpropertypath/as(_:)-5po1a)*