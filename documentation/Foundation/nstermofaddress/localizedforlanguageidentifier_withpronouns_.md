# localizedForLanguageIdentifier:withPronouns:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

A term of address restricted to a given language

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
+ (instancetype) localizedForLanguageIdentifier:(NSString *) language withPronouns:(NSArray<NSMorphologyPronoun *> *) pronouns;
```

## Parameters

- `language`: ISO language code identifier for the language
- `pronouns`: A list of pronouns in the target language that can be used to refer to the person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstermofaddress/localizedforlanguageidentifier:withpronouns:)*