# exportFormat

**Framework**: App Intents  
**Kind**: property

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst ?+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
var exportFormat: some AssistantSchemas.Enum { get }
```

#### Overview

To integrate your app’s functionality with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app enum implementation.

For general information about app intent domains, see doc:Integrating-actions-with-siri-and-apple-intelligence.

The following example shows an app enum that conforms to the `presentation.exportFormat` schema:

```swift
@AppEnum(schema: .presentation.exportFormat)
enum ExportFormatEnum: String {
    case pdf
    case powerpoint

    static let caseDisplayRepresentations: [Self: DisplayRepresentation] = [
        .pdf: "Pdf",
        .powerpoint: "Powerpoint"
    ]
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/presentationenum/exportformat)*