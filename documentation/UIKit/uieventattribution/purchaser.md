# purchaser

**Framework**: UIKit  
**Kind**: property

The entity that purchased the ad or content.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var purchaser: String { get }
```

#### Discussion

This property contains the name of the party that purchased the ad or other content. For example, for an in-app ad, this would contain the name of the company or individual that purchased the advertisement. The system may truncate this field if it’s longer than 100 characters.

## See Also

- [var destinationURL: URL](uieventattribution/destinationurl.md)
  The destination URL to attribute.
- [var reportEndpoint: URL?](uieventattribution/reportendpoint.md)
  The URL that receives attribution data.
- [var sourceDescription: String](uieventattribution/sourcedescription.md)
  A string describing the source tapped to launch the external link.
- [var sourceIdentifier: UInt8](uieventattribution/sourceidentifier.md)
  A number that identifies the source of the attribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieventattribution/purchaser)*