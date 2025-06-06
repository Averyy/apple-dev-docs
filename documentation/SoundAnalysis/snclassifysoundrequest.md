# SNClassifySoundRequest

**Framework**: Sound Analysis  
**Kind**: class

A request that classifies sound using a Core ML model.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class SNClassifySoundRequest
```

## Mentions

- [Classifying Sounds in an Audio File](classifying-sounds-in-an-audio-file.md)
- [Classifying Sounds in an Audio Stream](classifying-sounds-in-an-audio-stream.md)

#### Overview

An `SNClassifySoundRequest` represents a specific sound classification model. Analyze audio data with a sound classification model by:

1. Creating an `SNClassifySoundRequest`, either with the Sound Analysis model, or by providing your custom Core ML model.
2. Adding the sound request to an [`SNAudioFileAnalyzer`](snaudiofileanalyzer.md) or [`SNAudioStreamAnalyzer`](snaudiostreamanalyzer.md) to process an audio file or stream, respectively.

```swift
func makeRequest(_ customModel: MLModel? = nil) throws -> SNClassifySoundRequest {
    // If applicable, create a request with a custom sound classification model.
    if let model = customModel {
        let customRequest = try SNClassifySoundRequest(mlModel: model)
        return customRequest
    }

    // Create a request with the Sound Analysis model.
    let version1 = SNClassifierIdentifier.version1
    let request = try SNClassifySoundRequest(classifierIdentifier: version1)

    return request
}

let classifySoundRequest = try makeRequest()

// Prints every label in the request's sound classification model.
print(classifySoundRequest.knownClassifications)
```

For more information about creating and using classify sound requests, see:

- [`Classifying Sounds in an Audio File`](classifying-sounds-in-an-audio-file.md)
- [`Classifying Sounds in an Audio Stream`](classifying-sounds-in-an-audio-stream.md)

## Topics

### Creating a Request
- [init(mlModel: MLModel) throws](snclassifysoundrequest/init(mlmodel:).md)
  Creates a request that uses a custom sound classification model.
- [init(classifierIdentifier: SNClassifierIdentifier) throws](snclassifysoundrequest/init(classifieridentifier:).md)
  Creates a request that uses the framework’s built-in sound classification model.
- [struct SNClassifierIdentifier](snclassifieridentifier.md)
  An identifier that represents the versions of the framework’s sound classifier.
### Configuring a Request
- [var overlapFactor: Double](snclassifysoundrequest/overlapfactor.md)
  The amount of overlap between successive analysis windows when the model operates on a fixed-size audio block.
- [var windowDuration: CMTime](snclassifysoundrequest/windowduration.md)
  The duration of the audio buffer the request sends to the underlying sound classifier for each prediction.
### Inspecting a Request
- [var knownClassifications: [String]](snclassifysoundrequest/knownclassifications.md)
  A string array that contains every prediction label in the request’s underlying sound classifier model.
- [enum SNTimeDurationConstraint](sntimedurationconstraint-swift.enum.md)
  Defines the time duration windows the request’s underlying sound classifier accepts with a range, or an array, of durations.
### Instance Properties
- [var windowDurationConstraint: SNTimeDurationConstraint](snclassifysoundrequest/windowdurationconstraint-5no60.md)
  A range or list of sound duration times the request’s underlying sound classifier supports.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [SNRequest](snrequest.md)

## See Also

- [Classifying Live Audio Input with a Built-in Sound Classifier](classifying-live-audio-input-with-a-built-in-sound-classifier.md)
  Detect and identify hundreds of sounds by using a trained classifier.
- [class SNClassificationResult](snclassificationresult.md)
  A result that contains the highest-ranking classifications in a time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snclassifysoundrequest)*