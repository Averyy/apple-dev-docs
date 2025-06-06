# init(classifierIdentifier:)

**Framework**: Sound Analysis  
**Kind**: init

Creates a request that uses the framework’s built-in sound classification model.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(classifierIdentifier: SNClassifierIdentifier) throws
```

## Mentions

- [Classifying Sounds in an Audio File](classifying-sounds-in-an-audio-file.md)

## Parameters

- `classifierIdentifier`: A sound classifier version identifier, such as  .

## See Also

- [init(mlModel: MLModel) throws](snclassifysoundrequest/init(mlmodel:).md)
  Creates a request that uses a custom sound classification model.
- [struct SNClassifierIdentifier](snclassifieridentifier.md)
  An identifier that represents the versions of the framework’s sound classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snclassifysoundrequest/init(classifieridentifier:))*