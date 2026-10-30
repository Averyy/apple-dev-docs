# Built-in intelligence

**Framework**: Technology Overviews

Analyze photos, videos, speech, sound, and text using the models built in to the system frameworks.

## Overview

Adding intelligent features to your app is relatively easy because many Apple frameworks already use on-device models to analyze different types of content for you. Adopt these frameworks when you want to focus on building your app’s other features, rather than building your own machine learning models to perform the same tasks.

---

## Analyze photo and video content

Computer vision allows for better understanding of the world around you. When you work with photos and videos, you might want to know more about what’s happening in them to create the feature you want in your app. For example, you don’t have to start from zero to [recognize the content in a document](../Vision/analyzing-a-selfie-and-visualizing-its-content.md). The [Vision](../Vision/Vision.md) and [VisionKit](../VisionKit/VisionKit.md) frameworks perform a wide variety of tasks that do the heavy lifting for you, and provide more than 25 types of image analysis tasks, like:

- Capture text within the camera frame by turning on [Live Text in your app’s image views](../VisionKit/enabling-live-text-interactions-with-images.md).
- Identify objects, text, bar codes, documents, and more in images or the [live camera feed](../VisionKit/scanning-data-with-the-camera.md).
- Track the movement of [objects](../Vision/trackobjectrequest.md) across images or video frames.
- Detect face and body poses for [people](../Vision/detecthumanbodyposerequest.md) and [animals](../Vision/detectanimalbodyposerequest.md).
- Determine the [trajectory of shapes along a path](../Vision/detecttrajectoriesrequest.md).

To detect and prevent people from viewing unwanted image content in your app, [perform sensitive content analysis](../SensitiveContentAnalysis/detecting-nudity-in-media-and-providing-intervention-options.md).

---

## Recognize speech and audio content

Speech recognition transforms spoken words into text to help you with things like dictating notes in a note-taking app, or using voice commands to control a smart thermostat. [Convert human speech](../Speech/bringing-advanced-speech-to-text-capabilities-to-your-app.md) into text with very little code, and entirely on device using the Speech framework. Use this framework with audio from prerecorded files or from a live source like a microphone. [Analyze](../Speech/speechanalyzer.md) the speech you capture to predict the text that matches the audio.

Apps that work with songs or other types of audio can perform acoustic matching using the [ShazamKit](../ShazamKit/ShazamKit.md) framework. Acoustic matching helps you identify audio from pieces you capture from the person’s environment. The framework matches your audio against Shazam’s vast music catalog or a custom catalog of your own prerecorded reference audio.

Enhance the accessibility of your apps by adding sound analysis capabilities to your app. [Classify sounds](../SoundAnalysis/classifying-sounds-in-an-audio-file.md) in real time to identify environmental sounds, like glass breaking or a dog barking. If you’re building a music creation app, use sound analysis to identify the instrument someone is playing. You can even make a custom sound analysis model by training with your own data in the [Create ML app](https://developer.apple.com/machine-learning/create-ml/).

---

## Analyze and translate language content

[Natural language processing](../NaturalLanguage/NaturalLanguage.md) helps your app understand and process human language and extract meaning from text. [Identify different languages](../NaturalLanguage/identifying-the-language-in-text.md) in text to determine whether the content matches an expected language. [Break text down](../NaturalLanguage/tokenizing-natural-language-text.md) into lexical units — like words or sentences — to ensure correct behavior in multiple script languages. [Find similarities](../NaturalLanguage/finding-similarities-between-pieces-of-text.md) between pieces of text to identify matches between semantically similar content.

Offer in-app translations of your content using the [Translation](../Translation/Translation.md) framework. [Translate text](../Translation/translating-text-within-your-app.md) your app collects and display the results in a [popover](https://developer.apple.com/design/human-interface-guidelines/popovers). The framework uses on-device models to support translations between a [variety of languages](../Translation/languageavailability/supportedlanguages.md). If your app [provides translations](../TranslationUIProvider/preparing-your-app-to-be-the-default-translation-app.md), make those translations available to the rest of the system using the [TranslationUIProvider](../TranslationUIProvider/TranslationUIProvider.md) framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/built-in-intelligence)*