# AVMovieShouldSupportAliasDataReferencesKey

**Framework**: AVFoundation  
**Kind**: var  
**Role**: Global Variable

A key that specifies a Boolean value that indicates whether the system parses and resolves alias data references in the movie.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.12+
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

> **Deprecated**: AVMovieShouldSupportAliasDataReferencesKey is not supported on this platform

## Declaration

```swift
let AVMovieShouldSupportAliasDataReferencesKey: String
```

```c
extern NSString * const AVMovieShouldSupportAliasDataReferencesKey;
```

#### Discussion

The default value is [`false`](../Swift/false.md). Most QuickTime movie files contain all of the media data they require, but some contain references to media stored in other files. While AVFoundation and CoreMedia typically use a URL reference for this purpose, older implementations such as QuickTime 7 have commonly used a Macintosh alias instead, as documented in the QuickTime File Format specification. If your app must work with legacy QuickTime movie files containing alias-based references to media data stored in other files, set this value to [`true`](../Swift/true.md).

If you provide a value for [`AVMovieReferenceRestrictionsKey`](./avmoviereferencerestrictionskey.md), the movie observes these restrictions for resolved alias references just as they’re for URL references.

## See Also

### Options
- [let AVMovieReferenceRestrictionsKey: String](./avmoviereferencerestrictionskey.md)
  A key that specifies restrictions for a movie to use when it resolves references to external media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovieshouldsupportaliasdatareferenceskey)*