# Global Vocabulary Reference

**Framework**: SiriKit

Understand the keys and values included in your app’s global vocabulary file.

#### Overview

The `AppIntentVocabulary.plist` file in your iOS app contains examples of how users can engage your app’s intents from Siri and any custom terminology that applies to all users of the app. Place the `AppIntentVocabulary.plist` file in the bundle of your iOS app. You can include localized versions of your vocabulary property list file in the language-specific project (.lproj) directories of your app. When you submit your app to the App Store, your `AppIntentVocabulary.plist` file and any localized versions of that file are sent to Siri for processing. The content of those files remains on the server and that content is specific to that app version.

The Root dictionary of the `AppIntentVocabulary.plist` file contains the following keys:

> ❗ **Important**:  During development, Xcode syncs your vocabulary with Siri, which uses the vocabulary to interpret requests from the version of your app on your development device. Ingestion of your vocabulary data isn’t instantaneous, though, so you may need to wait a minute or two before testing your Siri capabilities.

## Topics

### Property List Keys
- [Parameter Vocabularies](parameter-vocabularies.md)
  The keys you include in your global vocabulary file to describe app-specific terms.
- [Intent Phrases](intent-phrases.md)
  The keys that you include in your global vocabulary file to show how users engage your app from Siri.
### Localization
- [Localizing Your Vocabulary for Chinese Dialects](localizing-your-vocabulary-for-chinese-dialects.md)
  Apply emphasis markers to your pronunciation tips to assist Siri with Chinese dialects.

## See Also

- [Specifying Synonyms for Your App Name](specifying-synonyms-for-your-app-name.md)
  Provide alternative names for your app that are more familiar or easier for users to speak.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/global-vocabulary-reference)*