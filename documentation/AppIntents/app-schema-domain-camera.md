# Camera

**Framework**: App Intents

Make your camera app’s actions available to Apple Intelligence and Siri by adopting schemas for common camera actions.

#### Overview

The `.camera` domain defines app schemas that provide a structured representation for common camera actions and content. Apply schemas in the `.camera` domain to make your app’s camera functionality available to Apple Intelligence and Siri.

The following table maps example phrases that apply to each schema:

| Camera intent schemas | Example phrases |
| --- | --- |
| [`openInCaptureMode`](appschema/cameraintent/openincapturemode.md) | “Open the camera.” or “Take a photo.” |
| [`switchDevice`](appschema/cameraintent/switchdevice.md) | “Flip the camera.” or “Turn the camera.” |
| [`startCapture`](appschema/cameraintent/startcapture.md) | “Start recording.” or “Record a video.” |

> 💡 **Tip**: Xcode generates a template implementation when you type `camera_` and select a schema from the suggestions list.

For more information about making your app’s actions available to Apple Intelligence and Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

## Topics

### Actions
- [var openInCaptureMode: some AppSchemaIntent](appschema/cameraintent/openincapturemode.md)
  An intent schema that opens the camera in the specified mode.
- [var setDevice: some AppSchemaIntent](appschema/cameraintent/setdevice.md)
  An intent schema that changes the camera to the specified position.
- [var startCapture: some AppSchemaIntent](appschema/cameraintent/startcapture.md)
  An intent schema that starts a capture or opens the camera in a specified mode with a timer setting.
- [var stopCapture: some AppSchemaIntent](appschema/cameraintent/stopcapture.md)
  An intent schema that stops a recording in progress.
- [var switchDevice: some AppSchemaIntent](appschema/cameraintent/switchdevice.md)
  An intent schema that toggles between front and back camera.
- [AppSchema.CameraIntent](appschema/cameraintent.md)
  Identifies intent schemas in the camera domain.
### Types for static parameters
- [var captureDevice: some AppSchemaEnum](appschema/cameraenum/capturedevice.md)
  An enum schema for a capture device parameter.
- [var captureDuration: some AppSchemaEnum](appschema/cameraenum/captureduration.md)
  An enum schema for a capture duration parameter.
- [var captureMode: some AppSchemaEnum](appschema/cameraenum/capturemode.md)
  An enum schema for a capture mode parameter.
- [AppSchema.CameraEnum](appschema/cameraenum.md)
  Identifies enum schemas in the camera domain.

## See Also

- [Audio](app-schema-domain-audio.md)
  Make your audio app’s actions available to Apple Intelligence and Siri by adopting schemas for common audio playback actions.
- [Calendar](app-schema-domain-calendar.md)
  Make your calendar app’s actions available to Apple Intelligence and Siri by adopting schemas for common calendar actions.
- [Clock](app-schema-domain-clock.md)
  Make your clock app’s actions available to Apple Intelligence and Siri by adopting schemas for common alarm and timer actions.
- [Files](app-schema-domain-files.md)
  Make your file-management app’s actions available to Apple Intelligence and Siri by adopting schemas for common file actions.
- [Mail](app-schema-domain-mail.md)
  Make your email app’s actions available to Apple Intelligence and Siri by adopting schemas for common email actions.
- [Maps](app-schema-domain-maps.md)
  Make your navigation app’s actions available to Apple Intelligence and Siri by adopting schemas for common navigation actions.
- [Messages](app-schema-domain-messages.md)
  Make your messaging app’s actions available to Apple Intelligence and Siri by adopting schemas for common messaging actions.
- [Notes](app-schema-domain-notes.md)
  Make your note-taking app’s actions available to Apple Intelligence and Siri by adopting schemas for common note actions.
- [Phone](app-schema-domain-phone.md)
  Make your phone app’s actions available to Apple Intelligence and Siri by adopting schemas for calling actions.
- [Photos](app-schema-domain-photos.md)
  Make your photo and video app’s actions available to Apple Intelligence and Siri by adopting schemas for common photo and video actions.
- [Reminders](app-schema-domain-reminders.md)
  Make your reminder app’s actions available to Apple Intelligence and Siri by adopting schemas for common reminder actions.
- [System and in-app search](app-schema-domain-system-and-in-app-search.md)
  Make your app’s actions available to Apple Intelligence and Siri by adopting schemas for in-app search and content access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-schema-domain-camera)*