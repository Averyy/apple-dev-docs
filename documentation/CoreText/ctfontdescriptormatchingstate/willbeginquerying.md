# CTFontDescriptorMatchingState.willBeginQuerying

**Framework**: Core Text  
**Kind**: case

A state that indicates communication with the server is about to begin.

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
case willBeginQuerying
```

#### Discussion

This state is skipped if unnecessary.

## See Also

- [CTFontDescriptorMatchingState.didBegin](ctfontdescriptormatchingstate/didbegin.md)
  A state that indicates matching is about to begin.
- [CTFontDescriptorMatchingState.didFinish](ctfontdescriptormatchingstate/didfinish.md)
  A state that indicates matching is done.
- [CTFontDescriptorMatchingState.stalled](ctfontdescriptormatchingstate/stalled.md)
  A state that indicates that matching is stalled, such as while waiting for a server response.
- [CTFontDescriptorMatchingState.willBeginDownloading](ctfontdescriptormatchingstate/willbegindownloading.md)
  A state that indicates downloading is about to begin.
- [CTFontDescriptorMatchingState.downloading](ctfontdescriptormatchingstate/downloading.md)
  A state that indicates downloading is in progress.
- [CTFontDescriptorMatchingState.didFinishDownloading](ctfontdescriptormatchingstate/didfinishdownloading.md)
  A state that indicates downloading is done.
- [CTFontDescriptorMatchingState.didMatch](ctfontdescriptormatchingstate/didmatch.md)
  A state that indicates the font descriptor match is successful.
- [CTFontDescriptorMatchingState.didFailWithError](ctfontdescriptormatchingstate/didfailwitherror.md)
  A state that indicates an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/willbeginquerying)*