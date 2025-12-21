# AssistantSchemas.AssistantIntent

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for app intents that offer support for the side button on iPhone in Japan.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst ?+

## Declaration

```swift
protocol AssistantIntent : AssistantSchemas.Model
```

#### Overview

Functionality provided by `AssistantIntent` and the [`activate`](assistantschemas/assistantintent/activate.md) schema is only available on iPhone in Japan and requires the [`Side Button Access`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.side-button-access.allow) entitlement. During development, install your provisioning profile on your iPhone test device to test the functionality. For a production device, the country or region of your Apple Account must be set to Japan, and you must physically be located in Japan. For additional information, refer to [`Launching your voice-based conversational app from the side button of iPhone`](launching-your-voice-based-conversational-app-from-the-side-button-of-iphone.md).

## Topics

### Schemas
- [var activate: some AssistantSchemas.Intent](assistantschemas/assistantintent/activate.md)
  The app intent conforms to the schema for launching your voice-based conversational app from the side button on iPhone in Japan.

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.IntentSchema](assistantschema/intentschema.md)

## See Also

- [Launching your voice-based conversational app from the side button of iPhone](launching-your-voice-based-conversational-app-from-the-side-button-of-iphone.md)
  Let people in Japan configure the side button of iPhone to launch your voice-based conversational app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/assistantintent)*