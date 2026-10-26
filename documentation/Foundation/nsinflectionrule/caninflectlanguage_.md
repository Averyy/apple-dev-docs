# canInflectLanguage:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the rule can inflect a given language.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```objc
+ (BOOL) canInflectLanguage:(NSString *) language;
```

## Parameters

- `language`: The language to apply inflection to, specified as a BCP 47 language code.

## See Also

### Determining Availability
- [canInflectPreferredLocalization](./caninflectpreferredlocalization.md)
  A Boolean value that indicates whether the rule can inflect the user’s current preferred localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsinflectionrule/caninflectlanguage:)*