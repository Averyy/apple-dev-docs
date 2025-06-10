# setModules(_:)

**Framework**: Speech  
**Kind**: method

Adds or removes modules.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final func setModules(_ newModules: [any SpeechModule]) async throws
```

#### Discussion

Modules can be added or removed to the analyzer mid-stream. A newly-added module will immediately begin analysis on new audio input, but it will not have access to already-analyzed audio. However, you may keep a copy of previously-analyzed audio and provide it to a separate analyzer.

Modules cannot be reused from a different analyzer.

## Parameters

- `newModules`: A list of modules to include in the analyzer. These modules replace the previous modules, but you may preserve previous modules by including them in the list.

## See Also

- [var modules: [any SpeechModule]](speechanalyzer/modules.md)
  The modules performing analysis on the audio input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/setmodules(_:))*