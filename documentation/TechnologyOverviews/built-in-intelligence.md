# Built-in intelligence

**Framework**: Technology Overviews

Analyze photos, videos, speech, sound, and text using the models built in to the system frameworks.

#### Overview

Adding intelligent features to your app is relatively easy because many Apple frameworks already use on-device models to analyze different types of content for you. Adopt these frameworks when you want to focus on building your app’s other features, rather than building your own machine learning models to perform the same tasks.

---

#### Analyze Photo and Video Content

Computer vision allows for better understanding of the world around you. When you work with photos and videos, you might want to know more about what’s happening in them to create the feature you want in your app. For example, you don’t have to start from zero to [`Analyzing a selfie and visualizing its content`](https://developer.apple.com/documentation/Vision/analyzing-a-selfie-and-visualizing-its-content). The [`Vision`](https://developer.apple.com/documentation/Vision) and [`VisionKit`](https://developer.apple.com/documentation/VisionKit) frameworks perform a wide variety of tasks that do the heavy lifting for you, and provide more than 25 types of image analysis tasks, like:

- Capture text within the camera frame by turning on [`Enabling Live Text interactions with images`](https://developer.apple.com/documentation/VisionKit/enabling-live-text-interactions-with-images).
- Identify objects, text, bar codes, documents, and more in images or the [`Scanning data with the camera`](https://developer.apple.com/documentation/VisionKit/scanning-data-with-the-camera).
- Track the movement of [`TrackObjectRequest`](https://developer.apple.com/documentation/Vision/TrackObjectRequest) across images or video frames.
- Detect face and body poses for [`DetectHumanBodyPoseRequest`](https://developer.apple.com/documentation/Vision/DetectHumanBodyPoseRequest) and [`DetectAnimalBodyPoseRequest`](https://developer.apple.com/documentation/Vision/DetectAnimalBodyPoseRequest).
- Determine the [`DetectTrajectoriesRequest`](https://developer.apple.com/documentation/Vision/DetectTrajectoriesRequest).

To detect and prevent people from viewing unwanted image content in your app, [`Detecting sensitive content in media and providing intervention options`](https://developer.apple.com/documentation/SensitiveContentAnalysis/detecting-nudity-in-media-and-providing-intervention-options).

---

#### Recognize Speech and Audio Content

Speech recognition transforms spoken words into text to help you with things like dictating notes in a note-taking app, or using voice commands to control a smart thermostat. [`Bringing advanced speech-to-text capabilities to your app`](https://developer.apple.com/documentation/Speech/bringing-advanced-speech-to-text-capabilities-to-your-app) into text with very little code, and entirely on device using the [`Speech`](https://developer.apple.comdocumentation/Speech) framework. Use this framework with audio from prerecorded files or from a live source like a microphone. [`SpeechAnalyzer`](https://developer.apple.com/documentation/Speech/SpeechAnalyzer) the speech you capture to predict the text that matches the audio.

Apps that work with songs or other types of audio can perform acoustic matching using the [`ShazamKit`](https://developer.apple.com/documentation/ShazamKit) framework. Acoustic matching helps you identify audio from pieces you capture from the person’s environment. The framework matches your audio against Shazam’s vast music catalog or a custom catalog of your own prerecorded reference audio.

Enhance the accessibility of your apps by adding sound analysis capabilities to your app. [`Classifying Sounds in an Audio File`](https://developer.apple.com/documentation/SoundAnalysis/classifying-sounds-in-an-audio-file) in real time to identify environmental sounds, like glass breaking or a dog barking. If you’re building a music creation app, use sound analysis to identify the instrument someone is playing. You can even make a custom sound analysis model by training with your own data in the [`Create ML app`](https://developer.apple.comhttps://developer.apple.com/machine-learning/create-ml/).

---

#### Analyze and Translate Language Content

[`Natural Language`](https://developer.apple.com/documentation/NaturalLanguage) helps your app understand and process human language and extract meaning from text. [`Identifying the language in text`](https://developer.apple.com/documentation/NaturalLanguage/identifying-the-language-in-text) in text to determine whether the content matches an expected language. [`Tokenizing natural language text`](https://developer.apple.com/documentation/NaturalLanguage/tokenizing-natural-language-text) into lexical units — like words or sentences — to ensure correct behavior in multiple script languages. [`Finding similarities between pieces of text`](https://developer.apple.com/documentation/NaturalLanguage/finding-similarities-between-pieces-of-text) between pieces of text to identify matches between semantically similar content.

Offer in-app translations of your content using the [`Translation`](https://developer.apple.com/documentation/Translation) framework. [`Translating text within your app`](https://developer.apple.com/documentation/Translation/translating-text-within-your-app) your app collects and display the results in a [`Popovers`](https://developer.apple.com/design/Human-Interface-Guidelines/popovers). The framework uses on-device models to support translations between a [`supportedLanguages`](https://developer.apple.com/documentation/Translation/LanguageAvailability/supportedLanguages). If your app [`Preparing your app to be the default translation app`](https://developer.apple.com/documentation/TranslationUIProvider/Preparing-your-app-to-be-the-default-translation-app), make those translations available to the rest of the system using the [`TranslationUIProvider`](https://developer.apple.com/documentation/TranslationUIProvider) framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/built-in-intelligence)*