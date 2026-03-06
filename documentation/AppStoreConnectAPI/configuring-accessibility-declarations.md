# Configuring accessibility declarations for your app

**Framework**: App Store Connect API

Manage accessibility metadata for your apps per device family.

#### Overview

You use the App Store Connect API to create and configure accessibility declarations for your app. After you create an accessibility declaration, you can update the list of supported features, and also remove the accessibility declaration. Accessibility declarations enable you to show the accessibility modalities and the specific features that your app supports. Once you create an accessibility declaration, your App Store page shows the accessibility details for your app. You make accessibility declarations for each app and these apply to a device family, such as `IPHONE`, `IPAD`, or `VISION`, to learn more, see [`DeviceFamily`](devicefamily.md).

Use this term list and table to understand what details to include in your app’s accessibility declaration.

##### Read Accessibility Feature Details

Here’s what each accessibility feature provides:

- **`supportsVoiceover`**: Navigate and explore the app using gestures, braille, and speech output.
- **`supportsVoiceControl`**: Navigate and interact with the app using your voice to tap, swipe, type, and more.
- **`supportsLargerText`**: Increase the text size in the app to 200 percent or more.
- **`supportsSufficientContrast`**: Increase or adjust the contrast between text or iconography and background.
- **`supportsDarkInterface`**: Apply a dark color scheme to the screens, menus, and controls to reduce eye strain.
- **`supportsDifferentiateWithoutColorAlone`**: Use shapes or text, in addition to or instead of color, to distinguish key information.
- **`supportsReducedMotion`**: Modify or reduce certain types of animation that may cause motion sickness or discomfort.
- **`supportsCaptions`**: Display the dialog and relevant sounds of video or audio-only content with time-synchronized text.
- **`supportsAudioDescriptions`**: Hear audio descriptions of video content in a clip, show, or movie with time-synchronized narration.

##### Read Accessibility Feature Device Family Compatibility

This table shows the compatibility for each accessibility feature and platform:

| Accessibility Feature | Attribute Name | iOS/iPadOS | tvOS | macOS | visionOS | watchOS |
| --- | --- | --- | --- | --- | --- | --- |
| VoiceOver | `supportsVoiceover` | ✔ | ✔ | ✔ | ✔ | ✔ |
| Voice Control | `supportsVoiceControl` | ✔ |  | ✔ | ✔ |  |
| Larger Text | `supportsLargerText` | ✔ |  |  | ✔ | ✔ |
| Sufficient Contrast | `supportsSufficientContrast` | ✔ | ✔ | ✔ | ✔ | ✔ |
| Dark Interface | `supportsDarkInterface` | ✔ | ✔ | ✔ | ✔ | ✔ |
| Differentiate Without Color Alone | `supportsDifferentiateWithoutColorAlone` | ✔ | ✔ | ✔ | ✔ | ✔ |
| Reduced Motion | `supportsReducedMotion` | ✔ | ✔ | ✔ | ✔ | ✔ |
| Captions | `supportsCaptions` | ✔ | ✔ | ✔ | ✔ | ✔ |
| Audio Descriptions | `supportsAudioDescriptions` | ✔ | ✔ | ✔ | ✔ | ✔ |

##### Create an Accessibility Declarations for Your App

After you determine the accessibility features your app supoorts, create an accessibility declaration, by using [`Create an accessibility declaration`](post-v1-accessibilitydeclarations.md) with a payload.

Here’s an example payload:

```json
{
  "data": {
    "type": "accessibilityDeclarations",
    "attributes": {
      "deviceFamily": "IPHONE",
      "supportsAudioDescriptions": true,
      "supportsCaptions": true,
      "supportsDarkInterface": true,
      "supportsDifferentiateWithoutColorAlone": true,
      "supportsLargerText": true,
      "supportsReducedMotion": true,
      "supportsSufficientContrast": true,
      "supportsVoiceControl": false,
      "supportsVoiceover": false
    },
    "relationships": {
      "app": {
        "data": {
          "type": "apps",
          "id": "{appID}"
        }
      }
    }
  }
}

```

The response includes a unique identifier.

Each device family your app supports can have their own accessibility declaration. To learn more, see [`DeviceFamily`](devicefamily.md).

##### Read the Accessibility Declarations for Your App

You can use [`Read accessibility declaration information`](get-v1-accessibilitydeclarations-_id_.md) with the unique identifier from the `POST` call you made, to look up the details of your current accessibility declaration. You can also get that unqiue identifier by using [`List all accessibility declarations for an app`](get-v1-apps-_id_-accessibilitydeclarations.md).

> **Note**: The response value for [`Read accessibility declaration information`](get-v1-accessibilitydeclarations-_id_.md) includes the `state` attribute, which indicates whether your accessibility declaration appears on your App Store page.

##### Modify the Accessibility Declarations for Your App

If you need to update your accessibility declaration, use [`Modify an accessibility declaration`](patch-v1-accessibilitydeclarations-_id_.md). You can supply any number of the available attributes with a corresponding Boolean value when modifying an accessibility declaration when it is in `DRAFT` state.

##### Publishing the Accessibility Declarations for Your App

When you are ready to show your accessibility declarations on your app’s page in the App Store, use [`Modify an accessibility declaration`](patch-v1-accessibilitydeclarations-_id_.md) with a payload like this:

```json
{
  "data": {
    "type": "accessibilityDeclarations",
    "id": "<id>",
    "attributes": {
      "publish": true
    }
  }
}
```

##### Remove an Accessibility Declaration for Your App

If you need to remove an accessibility declaration for an app, use [`Delete an accessibility declaration`](delete-v1-accessibilitydeclarations-_id_.md). You can only remove accessibility declarations that are in the `DRAFT` state. This deletes the declaration details. To create a new accessibility declaration, use [`Create an accessibility declaration`](post-v1-accessibilitydeclarations.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/configuring-accessibility-declarations)*