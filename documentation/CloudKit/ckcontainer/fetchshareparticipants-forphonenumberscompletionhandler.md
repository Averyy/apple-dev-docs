# fetchShareParticipants(forPhoneNumbers:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
@preconcurrency
func fetchShareParticipants(forPhoneNumbers phoneNumbers: [String], completionHandler: @escaping (Result<[String : Result<CKShare.Participant, any Error>], any Error>) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/fetchshareparticipants(forphonenumbers:completionhandler:))*