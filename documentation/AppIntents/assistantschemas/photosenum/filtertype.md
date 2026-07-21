# filterType

**Framework**: App Intents  
**Kind**: property

The filter effect for a photo or video.

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
var filterType: some AssistantSchemas.Enum { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app enum implementation. The following example shows an app enum that conforms to the `.photos.filterType` schema:

```swift
@AppEnum(schema: .photos.filterType)
enum PhotoFilterEffectType: AppEnum {
    case original

    static var caseDisplayRepresentations: [PhotoFilterEffectType: AppIntents.DisplayRepresentation] = [
        .original: "Original",
    ]
}
```

For more information about the `.photos` app intent domain, see [`Photos`](app-schema-domain-photos.md). For general information about app intent domains, see [`Making actions and content discoverable by Apple Intelligence`](making-actions-and-content-discoverable-by-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/photosenum/filtertype)*