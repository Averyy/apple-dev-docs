# setVocabularyStrings(_:of:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Registers the specified vocabulary strings with the user.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func setVocabularyStrings(_ vocabulary: NSOrderedSet, of type: INVocabularyStringType)
```

```objc
- (void) setVocabularyStrings:(NSOrderedSet<NSString *> *) vocabulary ofType:(INVocabularyStringType) type;
```

## Discussion

Use this method to register user-specific vocabulary terms of the specified type. You may register different sets of strings for each of the supported types, but you may register only one group of strings for each type. Calling this method again for a given type replaces the previously registered strings already assigned to that type.

Do not use this method to register terminology that is common to all users of your app. Use this method only to register terms that are specific to the current user. Common terminology should be included in the vocabulary property list file that you include with your Intents extension.

Calling this method is not a guarantee that Siri will use the terms you supply. If you specify more than just a few strings, Siri may ingest only the first few strings rather than the entire list. So always place the most important strings first in the ordered set. In addition, if any of the strings exceed the maximum size limit, Siri ignores them.

It is a programmer error to register terms that are not supported by any of your extension’s intents.

## Parameters

- `vocabulary`: The vocabulary strings to associate with the specified `type`. Each [`NSString`](../../Foundation/nsstring.md) object should contain terms that are unique to your app and to the specific user. Sort the strings in descending order of importance. In other words, the first string should be the most important, followed by strings of decreasing importance. Each string must be no more than 1024 bytes.
- `type`: The designated purpose for the strings in the `vocabulary` parameter. You must specify one of the designated types. You cannot specify custom types of strings. For a list of possible values, see [`INVocabularyStringType`](../invocabularystringtype.md).

## See Also

### Updating the User-Specific Vocabulary
- [func setVocabulary(NSOrderedSet, of: INVocabularyStringType)](./setvocabulary%28_,of%29.md)
  Registers the specified vocabulary strings with the user.
- [enum INVocabularyStringType](../invocabularystringtype.md)
  Possible usages for a custom vocabulary term.
- [func removeAllVocabularyStrings()](./removeallvocabularystrings%28%29.md)
  Removes all user-specific vocabulary strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/invocabulary/setvocabularystrings(_:of:))*