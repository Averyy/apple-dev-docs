# appContext

**Framework**: App Intents  
**Kind**: property

An app context that an app can use to pass necessary information to the sandboxed capture extension. The system will retrieve this app context when necessary and inject it for use during

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
static var appContext: Self.AppContext? { get async throws }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/cameracaptureintent/appcontext-swift.type.property)*