# export(to:)

**Framework**: Speech  
**Kind**: method

Export the accumulated data to a file.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.1+

## Declaration

```swift
func export(to path: URL) async throws
```

#### Discussion

The file produced by this method can be provided to `SFSpeechLanguageModel.prepareCustomLanguageModel` to produce language model and vocabulary files that are then ready to be used in conjunction with the `SFSpeechRecognizer`.

> **Note**: Errors related to creating directories and files, and deleting files

## Parameters

- `path`: A URL where the exported data will be saved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/export(to:))*