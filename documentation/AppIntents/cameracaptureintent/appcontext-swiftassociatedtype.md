# AppContext

**Framework**: App Intents  
**Kind**: associatedtype  
**Required**: Yes

Container type used for storing and retrieving app specific information that can be accessed whenever (and wherever) this intent gets run

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+

## Declaration

```swift
associatedtype AppContext : Decodable, Encodable, Sendable = Never
```

#### Discussion

Default Value: `Never`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/cameracaptureintent/appcontext-swift.associatedtype)*