# sourceDescription

**Framework**: UIKit  
**Kind**: property

A string describing the source tapped to launch the external link.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var sourceDescription: String { get }
```

#### Discussion

This property contains a description of the attribution source. For example, for an ad, `sourceDescription` describes the content of the advertisement that the user tapped.

The system may truncate this field if it’s longer than 100 characters.

## See Also

- [var destinationURL: URL](uieventattribution/destinationurl.md)
  The destination URL to attribute.
- [var purchaser: String](uieventattribution/purchaser.md)
  The entity that purchased the ad or content.
- [var reportEndpoint: URL?](uieventattribution/reportendpoint.md)
  The URL that receives attribution data.
- [var sourceIdentifier: UInt8](uieventattribution/sourceidentifier.md)
  A number that identifies the source of the attribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieventattribution/sourcedescription)*