# location(precise:)

**Framework**: App Intents  
**Kind**: method

User needs to grant location permission to the app.

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
static func location(precise: Bool = false) -> AppIntentError
```

#### Discussion

The error message will differ based on whether they need to grant Precise or Approximate Location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintenterror/permissionrequired/location(precise:))*