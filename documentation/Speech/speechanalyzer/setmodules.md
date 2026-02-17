# setModules(_:)

**Framework**: Speech  
**Kind**: method

Adds or removes modules.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func setModules(_ newModules: [any SpeechModule]) async throws
```

#### Discussion

Modules can be added or removed to the analyzer mid-stream. A newly-added module will immediately begin analysis on new audio input, but it will not have access to already-analyzed audio. However, you may keep a copy of previously-analyzed audio and provide it to a separate analyzer.

Modules cannot be reused from a different analyzer.

> **Note**: There is a limit to the number of active, backing engine instances and models SpeechAnalyzer is allowed to allocate to clients at the same time. An error will be thrown if that limit is reached in order to prevent poor system performance. Several transcriber instances can share the same backing engine instances and models, so long as the transcribers are configured similarly in certain respects. For iOS and visionOS, this roughly translates to two ongoing recognition instances (or two incompatible modules running simultaneously). There is currently no limit on macOS.

## Parameters

- `newModules`: A list of modules to include in the analyzer. These modules replace the previous modules, but you may preserve previous modules by including them in the list.

## See Also

- [var modules: [any SpeechModule]](speechanalyzer/modules.md)
  The modules performing analysis on the audio input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/setmodules(_:))*