# init(workingDirectory:)

**Framework**: Media Intelligence  
**Kind**: init

Creates a face group analyzer at the specified directory.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(workingDirectory: URL) throws
```

## Mentions

- [Detecting and grouping faces in images](detecting-and-grouping-faces-in-images.md)

#### Discussion

The analyzer loads any existing face data from `workingDirectory` on initialization, so subsequent runs resume from where the previous session ended.

## Parameters

- `workingDirectory`: The directory where the analyzer stores its face data and metadata. The directory must already exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer/init(workingdirectory:))*