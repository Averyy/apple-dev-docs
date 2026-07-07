# AppSchema.AssistantIntent

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for app intents that offer support for the side button on iPhone in Japan.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
protocol AssistantIntent : AppSchema.Kind
```

#### Overview

Functionality provided by `AssistantIntent` and the [`activate`](appschema/assistantintent/activate.md) schema is only available on iPhone in Japan and requires the [`Side Button Access`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.side-button-access.allow) entitlement. During development, install your provisioning profile on your iPhone test device to test the functionality. For a production device, the country or region of your Apple Account must be set to Japan, and you must physically be located in Japan. For additional information, refer to [`Launching your voice-based conversational app from the side button of iPhone`](launching-your-voice-based-conversational-app-from-the-side-button-of-iphone.md).

## Topics

### Schemas
- [var activate: some AppSchemaIntent](appschema/assistantintent/activate.md)
  The app intent conforms to the schema for launching your voice-based conversational app from the side button on iPhone in Japan.

## Relationships

### Inherits From
- [AppSchema.Kind](appschema/kind.md)
### Conforming Types
- [AppSchema.Intent](appschema/intent.md)

## See Also

- [var activate: some AppSchemaIntent](appschema/assistantintent/activate.md)
  The app intent conforms to the schema for launching your voice-based conversational app from the side button on iPhone in Japan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/assistantintent)*