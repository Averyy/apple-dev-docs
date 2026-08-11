# LanguageModelSession.Error.concurrentRequests

**Framework**: Foundation Models  
**Kind**: case

The session received multiple concurrent requests.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
case concurrentRequests
```

#### Discussion

A language model session only supports one request at a time. Wait for the current request to complete before starting another.

## See Also

- [LanguageModelSession.Error.transcriptMutationWhileResponding](languagemodelsession/error/transcriptmutationwhileresponding.md)
  A request mutated the session’s transcript while it was in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/error/concurrentrequests)*