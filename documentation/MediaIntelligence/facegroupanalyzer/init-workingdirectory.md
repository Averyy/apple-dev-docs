# init(workingDirectory:)

**Framework**: Media Intelligence  
**Kind**: init

Creates a face group analyzer at the specified directory.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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