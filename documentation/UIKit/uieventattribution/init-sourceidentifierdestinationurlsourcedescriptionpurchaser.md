# init(sourceIdentifier:destinationURL:sourceDescription:purchaser:)

**Framework**: UIKit  
**Kind**: init

Initializes a new event attribution object.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(sourceIdentifier: UInt8, destinationURL: URL, sourceDescription: String, purchaser: String)
```

## Parameters

- `sourceIdentifier`: An 8-bit number that identifies the source of the click for attribution. Value must be between   and  .
- `destinationURL`: The destination URL of the attribution.
- `sourceDescription`: A description of the source of the attribution.
- `purchaser`: A string that describes the entity that purchased the attributed content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieventattribution/init(sourceidentifier:destinationurl:sourcedescription:purchaser:))*