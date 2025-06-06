# updateAppContext(_:)

**Framework**: App Intents  
**Kind**: method

Whenever the in-app context for this intent changes any process containing this intent can call this method to provide updated state to the system.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
static func updateAppContext(_ newContext: Self.AppContext?) async throws
```

#### Discussion

Note: The size of data `newContext` uses when encoded with JSONEncoder can not exceed 4kB


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/cameracaptureintent/updateappcontext(_:))*