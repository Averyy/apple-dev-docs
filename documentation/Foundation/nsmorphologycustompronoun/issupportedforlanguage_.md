# isSupportedForLanguage:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the given language supports setting custom pronouns.

**Availability**:
- iOS 15.0+ - Deprecated in 17.0
- iPadOS 15.0+ - Deprecated in 17.0
- Mac Catalyst 15.0+ - Deprecated in 17.0
- macOS 12.0+ - Deprecated in 14.0
- tvOS 15.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 8.0+ - Deprecated in 10.0

## Declaration

```objc
+ (BOOL) isSupportedForLanguage:(NSString *) language;
```

## Return Value

`true` if the language supports custom pronouns; otherwise, `false`.

## Parameters

- `language`: The language to query.

## See Also

### Assessing Custom Pronoun Support
- [+ requiredKeysForLanguage:](./requiredkeysforlanguage_.md)
  Returns a collection of the custom pronoun keys required by this language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmorphologycustompronoun/issupportedforlanguage:)*