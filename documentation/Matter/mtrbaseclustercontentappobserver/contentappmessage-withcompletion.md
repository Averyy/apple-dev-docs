# contentAppMessage(with:completion:)

**Framework**: Matter  
**Kind**: method

Command ContentAppMessage

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
func contentAppMessage(with params: MTRContentAppObserverClusterContentAppMessageParams) async throws -> MTRContentAppObserverClusterContentAppMessageResponseParams
```

#### Discussion

Upon receipt, the data field MAY be parsed and interpreted. Message encoding is specific to the Content App. A Content App MAY when possible read attributes from the Basic Information Cluster on the Observer and use this to determine the Message encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustercontentappobserver/contentappmessage(with:completion:))*