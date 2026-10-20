# sourceIdentifier

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A number that identifies the source of the attribution.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+

## Declaration

```swift
var sourceIdentifier: UInt8 { get }
```

```objc
@property (nonatomic, assign, readonly) uint8_t sourceIdentifier;
```

#### Discussion

This property contains an integer, between 0 and 255, that identifies the source of the attribution. For example, for an ad, `sourceIdentifier` might contain a campaign identifier so the advertiser can measure the effectiveness of different advertising campaigns.

This field corresponds to the `source_id` field of a web attribution.

## See Also

### Setting attribution details
- [var destinationURL: URL](./destinationurl.md)
  The destination URL to attribute.
- [var purchaser: String](./purchaser.md)
  The entity that purchased the ad or content.
- [var reportEndpoint: URL?](./reportendpoint.md)
  The URL that receives attribution data.
- [var sourceDescription: String](./sourcedescription.md)
  A string describing the source tapped to launch the external link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieventattribution/sourceidentifier)*