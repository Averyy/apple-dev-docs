# AVMovieReferenceRestrictionsKey

**Framework**: AVFoundation  
**Kind**: var

A key that specifies restrictions for a movie to use when it resolves references to external media data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
let AVMovieReferenceRestrictionsKey: String
```

#### Discussion

Specify a value for this key by passing an appropriate [`AVAssetReferenceRestrictions`](avassetreferencerestrictions.md) value, or the logical combination of multiple values.

Some movies contain references to media data stored outside the movie’s container, such as in another file. This key specifies a policy to use when the movie encounters these references. If a movie contains one or more references of a type that’s forbidden by the reference restrictions, the loading of the movie properties fails. Additionally, you can’t use that movie instance for playback or processing.

## See Also

- [let AVMovieShouldSupportAliasDataReferencesKey: String](avmovieshouldsupportaliasdatareferenceskey.md)
  A key that specifies a Boolean value that indicates whether the system parses and resolves alias data references in the movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmoviereferencerestrictionskey)*