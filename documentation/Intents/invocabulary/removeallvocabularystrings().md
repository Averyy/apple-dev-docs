# removeAllVocabularyStrings()

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Removes all user-specific vocabulary strings.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func removeAllVocabularyStrings()
```

```objc
- (void) removeAllVocabularyStrings;
```

#### Discussion

This method removes all strings (regardless of type) that you previously registered for this user using the [`setVocabularyStrings(_:of:)`](./setvocabularystrings%28_,of%29.md) method.

## See Also

### Updating the User-Specific Vocabulary
- [func setVocabulary(NSOrderedSet, of: INVocabularyStringType)](./setvocabulary%28_,of%29.md)
  Registers the specified vocabulary strings with the user.
- [enum INVocabularyStringType](../invocabularystringtype.md)
  Possible usages for a custom vocabulary term.
- [func setVocabularyStrings(NSOrderedSet, of: INVocabularyStringType)](./setvocabularystrings%28_,of%29.md)
  Registers the specified vocabulary strings with the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/invocabulary/removeallvocabularystrings())*