# location(precise:)

**Framework**: App Intents  
**Kind**: method

The person needs to allow the app to access their location.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static func location(precise: Bool = false) -> AppIntentError
```

#### Discussion

The error message differs based on whether a person needs to give the app access to their precise or approximate location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintenterror/permissionrequired/location(precise:))*