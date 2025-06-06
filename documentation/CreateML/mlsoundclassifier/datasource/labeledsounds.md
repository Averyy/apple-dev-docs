# labeledSounds()

**Framework**: Create ML  
**Kind**: method

Generates a dictionary of the data source’s labeled audio files.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func labeledSounds() throws -> [String : [URL]]
```

#### Return Value

A dictionary of labeled audio files. Each dictionary key is a label string and its value is an array of audio-file URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeledsounds())*