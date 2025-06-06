# init(trainingData:parameters:)

**Framework**: Create ML  
**Kind**: init

Creates a sound classifier with a training dataset represented by a data source.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
init(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.ModelParameters = ModelParameters()) throws
```

#### Discussion

Use this initializer to train a sound classifier with an [`MLSoundClassifier.DataSource`](mlsoundclassifier/datasource.md). For example, you can organize your audio files into labeled directories. See [`MLSoundClassifier.DataSource.labeledDirectories(at:)`](mlsoundclassifier/datasource/labeleddirectories(at:).md).

```swift
// Get the Documents directory URL.
guard let documentsURL = FileManager.default.urls(for: .documentDirectory,
                                                  in: .userDomainMask).first else {
    fatalError("Can't find Documents directory.")
}

// Build a URL to the ~/Documents/Sounds directory, which contains the training data.
let soundsURL = documentsURL.appendingPathComponent("Sounds")

// The Sounds directory contains subdirectories, one for each class of sound.
// Each subdirectory's name is the label for audio files it contains.
//
// Sounds
// -- Laughter
// -- Recording1.wav
// -- Recording4.wav
// -- ...
// -- Applause
// -- Recording2.wav
// -- Recording5.wav
// -- ...

// Create a data source from the Sounds directory.
let trainingData = MLSoundClassifier.DataSource.labeledDirectories(at: soundsURL)

// Train a sound classifier with the data source.
let soundClassifier = try MLSoundClassifier(trainingData: trainingData)
```

## Parameters

- `trainingData`: An   instance that contains a collection of labeled audio   files.
- `parameters`: An   instance you use to configure the model   for the training session.

## See Also

- [init(trainingData: [String : [URL]], parameters: MLSoundClassifier.ModelParameters) throws](mlsoundclassifier/init(trainingdata:parameters:)-83tih.md)
  Creates a sound classifier with a training dataset represented by a dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/init(trainingdata:parameters:)-bztx)*