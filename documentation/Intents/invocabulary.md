# INVocabulary

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An object for registering user-specific vocabulary that Siri requests might include.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INVocabulary
```

```objc
@interface INVocabulary : NSObject
```

## Mentions

- [Improving interactions between Siri and your messaging app](../SiriKit/improving-interactions-between-siri-and-your-messaging-app.md)
- [Improving Siri Media Interactions and App Selection](../SiriKit/improving-siri-media-interactions-and-app-selection.md)

#### Overview

The [`INVocabulary`](./invocabulary.md) object lets you augment your app’s global vocabulary with terms that are both unique to your app and to the current user of your app. Registering custom terms provides Siri with hints it needs to apply those terms appropriately to the corresponding intent objects. You may register custom terms only for specific types of content, including users of your app, custom workout names, or custom tags applied to a photo.

Some tips for specifying custom vocabulary include:

- Be selective about the terms that you register for users. Include words and phrases only when their use in your app by the current user might differ from everyday usage.
- Order terms from most important to least important. If you register a large number of entries, Siri may ingest only the ones at the beginning of your list.
- Don’t register contact names that you retrieved from the user’s Contacts database. Register contacts only if your app manages contact information separately from the system databases.
- Don’t use this class to register terms that are common to all users of your app. Include vocabulary that’s common to all users of your app in your app’s global vocabulary file. For information about specifying your app’s global vocabulary file, see [SiriKit Programming Guide](https://developer.apple.com/library/archive/documentation/Intents/Conceptual/SiriIntegrationGuide/index.html#//apple_ref/doc/uid/TP40016875).
- Your Intents extension must support at least one intent that uses the registered terms. It’s a programmer error to register terms that aren’t supported by any of your extension’s intents.

Use the shared vocabulary object only in your iOS app. Don’t try to register vocabulary from your Intents extension or Intents UI extension.

## Topics

### Getting the Shared Vocabulary Object
- [class func shared() -> Self](./invocabulary/shared%28%29.md)
  Returns the shared vocabulary object.
### Updating the User-Specific Vocabulary
- [func setVocabulary(NSOrderedSet, of: INVocabularyStringType)](./invocabulary/setvocabulary%28_,of%29.md)
  Registers the specified vocabulary strings with the user.
- [enum INVocabularyStringType](./invocabularystringtype.md)
  Possible usages for a custom vocabulary term.
- [func setVocabularyStrings(NSOrderedSet, of: INVocabularyStringType)](./invocabulary/setvocabularystrings%28_,of%29.md)
  Registers the specified vocabulary strings with the user.
- [func removeAllVocabularyStrings()](./invocabulary/removeallvocabularystrings%28%29.md)
  Removes all user-specific vocabulary strings.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Vocabulary
- [Registering Custom Vocabulary with SiriKit](../SiriKit/registering-custom-vocabulary-with-sirikit.md)
  Register your app’s custom terminology, and provide sample phrases for how to use your app with Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/invocabulary)*