# rotationDirection

**Framework**: App Intents  
**Kind**: property

The direction for rotating a photo or video.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var rotationDirection: some AssistantSchemas.Enum { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app enum implementation. The following example shows an app enum that conforms to the `.photos.rotationDirection` schema:

```swift
@AppEnum(schema: .photos.rotationDirection)
enum PhotoRotationDirection: AppEnum {
    case clockwise

    static var caseDisplayRepresentations: [PhotoRotationDirection: AppIntents.DisplayRepresentation] = [
        .clockwise: "Clockwise",
    ]
}
```

For more information about the `.photos` app intent domain, see doc:Making-photo-and-video-actions-available-to-siri-and-apple-intelligence. For general information about app intent domains, see doc:Integrating-actions-with-siri-and-apple-intelligence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/photosenum/rotationdirection)*