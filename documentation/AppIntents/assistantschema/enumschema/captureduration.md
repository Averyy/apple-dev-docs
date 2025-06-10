# captureDuration

**Framework**: App Intents  
**Kind**: property

The capture duration for a photo or video.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var captureDuration: some AssistantSchemas.Enum { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app enum implementation.The following example shows an app enum that conforms to the `.camera.captureDuration` schema:

```swift
@AssistantEnum(schema: .camera.captureDuration)
enum CaptureDuration: AppEnum {
    case short
    case long

    static var caseDisplayRepresentations: [CaptureDuration: AppIntents.DisplayRepresentation] = [
        .short: "Short",
        .long: "Long",
    ]
}
```

For more information about the `.camera` app intent domain, see [`Making camera actions available to Siri and Apple Intelligence`](making-camera-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschema/enumschema/captureduration)*