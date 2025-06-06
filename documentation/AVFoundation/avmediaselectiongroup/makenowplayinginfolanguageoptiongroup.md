# makeNowPlayingInfoLanguageOptionGroup()

**Framework**: AVFoundation  
**Kind**: method

Creates a language option group from the media selection group.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func makeNowPlayingInfoLanguageOptionGroup() -> MPNowPlayingInfoLanguageOptionGroup
```

#### Return Value

The new language option group.

#### Discussion

Any option from [`AVMediaSelectionOption`](avmediaselectionoption.md) in the [`AVMediaSelectionGroup`](avmediaselectiongroup.md) not representing an audible or legible selection option is ignored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/makenowplayinginfolanguageoptiongroup())*