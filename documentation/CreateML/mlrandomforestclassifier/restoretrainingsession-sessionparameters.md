# restoreTrainingSession(sessionParameters:)

**Framework**: Create ML  
**Kind**: method

Restores an existing training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLRandomForestClassifier>
```

#### Return Value

A `MLTrainingSession` that can be used to resume training.

## Parameters

- `sessionParameters`: Training session parameters. The   parameter is required.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestclassifier/restoretrainingsession(sessionparameters:))*