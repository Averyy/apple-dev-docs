# AppSchema.AssistantIntent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

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

Functionality provided by `AssistantIntent` and the [`activate`](./assistantintent/activate.md) schema is only available on iPhone in Japan and requires the [`Side Button Access`](../../BundleResources/entitlements/com.apple.developer.side-button-access.allow.md) entitlement. During development, install your provisioning profile on your iPhone test device to test the functionality. For a production device, the country or region of your Apple Account must be set to Japan, and you must physically be located in Japan. For additional information, refer to [Launching your voice-based conversational app from the side button of iPhone](../launching-your-voice-based-conversational-app-from-the-side-button-of-iphone.md).

## Topics

### Schemas
- [var activate: some AppSchemaIntent](./assistantintent/activate.md)
  The app intent conforms to the schema for launching your voice-based conversational app from the side button on iPhone in Japan.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Intent](./intent.md)

## See Also

### Actions
- [var activate: some AppSchemaIntent](./assistantintent/activate.md)
  The app intent conforms to the schema for launching your voice-based conversational app from the side button on iPhone in Japan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/assistantintent)*