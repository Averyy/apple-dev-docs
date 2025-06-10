# Classifying Sounds in an Audio File

**Framework**: Sound Analysis

Identify individual sounds in a file, such as a recording, with an audio file analyzer.

#### Overview

Recognize sounds, such as laughter and applause, when they occur in a recording by processing audio files with an [`SNAudioFileAnalyzer`](snaudiofileanalyzer.md). For example, a sound recording app can use an audio file analyzer to assign searchable metadata tags to each sound file in its library. The same app could also use the analyzer to add timestamps to each recording so that the user can jump to a moment with a specific sound.

##### Create a Sound Classification Request

Create an [`SNClassifySoundRequest`](snclassifysoundrequest.md) by passing a version identifier to the [`init(classifierIdentifier:)`](snclassifysoundrequest/init(classifieridentifier:).md) initializer.

```swift
let version1 = SNClassifierIdentifier.version1
let request = try SNClassifySoundRequest(classifierIdentifier: version1)
```

Alternatively, you can create a sound request that uses a custom Core ML model. For example, you can train your own sound classifier with Create ML’s [`MLSoundClassifier`](https://developer.apple.com/documentation/CreateML/MLSoundClassifier).

Create an [`SNClassifySoundRequest`](snclassifysoundrequest.md) with a custom sound classifier model:

1. Add a sound classifier’s [`Core ML`](https://developer.apple.com/documentation/CoreML) model file to your project (see [`Integrating a Core ML Model into Your App`](https://developer.apple.com/documentation/CoreML/integrating-a-core-ml-model-into-your-app)).
2. Create an instance of the model’s wrapper class. Xcode automatically generates a class with the same name (minus the `mlmodel` extension).
3. Pass the instance’s `model` property to the [`init(mlModel:)`](snclassifysoundrequest/init(mlmodel:).md) initializer.

```swift
// Use a default model configuration.
let defaultConfig = MLModelConfiguration()

// Create an instance of the sound classifier's wrapper class.
let soundClassifier = try SoundClassifier(configuration: defaultConfig)

// Create a classify sound request that uses the custom sound classifier.
let classifySoundRequest = try SNClassifySoundRequest(mlModel: soundClassifier.model)
```

##### Implement a Results Observer

Implement a type that receives results from an audio analyzer by adopting the [`SNResultsObserving`](snresultsobserving.md) protocol. The protocol defines the methods an analyzer calls as it generates results or errors, or when it completes a task.

```swift
let resultsObserver = ResultsObserver()

/// An observer that receives results from a classify sound request.
class ResultsObserver: NSObject, SNResultsObserving {
    /// Notifies the observer when a request generates a prediction.
    func request(_ request: SNRequest, didProduce result: SNResult) {
        // Downcast the result to a classification result.
        guard let result = result as? SNClassificationResult else  { return }

        // Get the prediction with the highest confidence.
        guard let classification = result.classifications.first else { return }

        // Get the starting time.
        let timeInSeconds = result.timeRange.start.seconds

        // Convert the time to a human-readable string.
        let formattedTime = String(format: "%.2f", timeInSeconds)
        print("Analysis result for audio at time: \(formattedTime)")

        // Convert the confidence to a percentage string.
        let percent = classification.confidence * 100.0
        let percentString = String(format: "%.2f%%", percent)

        // Print the classification's name (label) with its confidence.
        print("\(classification.identifier): \(percentString) confidence.\n")
    }


    /// Notifies the observer when a request generates an error.
    func request(_ request: SNRequest, didFailWithError error: Error) {
        print("The analysis failed: \(error.localizedDescription)")
    }

    /// Notifies the observer when a request is complete.
    func requestDidComplete(_ request: SNRequest) {
        print("The request completed successfully!")
    }
}
```

The observer in this example prints the prediction’s result — a timestamp, a classification name, and the classifier’s confidence — to the console. Implement your observer to take action that’s appropriate for your app according to the result.

> ❗ **Important**:  You must maintain a strong reference to your observer. Sound analyzers don’t keep strong references to your observer.

##### Create an Audio File Analyzer

Analyze an audio file by creating an [`SNAudioFileAnalyzer`](snaudiofileanalyzer.md) and passing a URL to an audio file to the [`init(url:)`](snaudiofileanalyzer/init(url:).md) initializer.

```swift
/// Creates an analyzer for an audio file.
/// - Parameter audioFileURL: The URL to an audio file.
func createAnalyzer(audioFileURL: URL) -> SNAudioFileAnalyzer? {
    return try? SNAudioFileAnalyzer(url: audioFileURL)
}
```

> 💡 **Tip**:  Audio file analyzers work with any compressed or uncompressed audio file format that [`Core Audio`](https://developer.apple.com/documentation/CoreAudio) supports.

Add your sound classification request and results observer to the analyzer by calling the [`add(_:withObserver:)`](snaudiofileanalyzer/add(_:withobserver:).md) method.

```swift
// Create a new observer to receive notifications for analysis results.
resultsObserver = ResultsObserver()

// Add a request to analyze.
try audioFileAnalyzer.add(classifySoundRequest, withObserver: resultsObserver)
```

Start analyzing the audio file by calling the [`analyze()`](snaudiofileanalyzer/analyze().md) or [`analyze(completionHandler:)`](snaudiofileanalyzer/analyze(completionhandler:).md) methods.

```swift
// Analyze the audio data.
audioFileAnalyzer.analyze()
```

##### Receive the Results

The audio analyzer sends each result to your [`SNResultsObserving`](snresultsobserving.md) instance as it processes the audio data.

```None
Analysis result for audio at time: 1.45
Acoustic Guitar: 92.39% confidence.

...

Analysis result for audio at time: 8.74
Acoustic Guitar: 94.45% confidence.

...

Analysis result for audio at time: 14.15
Tambourine: 85.39% confidence.

...

Analysis result for audio at time: 20.92
Snare Drum: 96.87% confidence.
```

## See Also

- [class SNAudioFileAnalyzer](snaudiofileanalyzer.md)
  An analyzer that runs sound classification requests on an audio file.
- [Classifying Sounds in an Audio Stream](classifying-sounds-in-an-audio-stream.md)
  Identify individual sounds in an audio data stream, such as from a microphone, with an audio stream analyzer.
- [class SNAudioStreamAnalyzer](snaudiostreamanalyzer.md)
  An object you create to analyze a stream of audio data and provide the results to your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/classifying-sounds-in-an-audio-file)*