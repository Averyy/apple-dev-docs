# contextualStrings

**Framework**: Speech  
**Kind**: property

An array of phrases that should be recognized, even if they are not in the system vocabulary.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var contextualStrings: [String] { get set }
```

#### Discussion

Use this property to specify short custom phrases that are unique to your app. You might include phrases with the names of characters, products, or places that are specific to your app. You might also include domain-specific terminology or unusual or made-up words. Assigning custom phrases to this property improves the likelihood of those phrases being recognized.

Keep phrases relatively brief, limiting them to one or two words whenever possible. Lengthy phrases are less likely to be recognized. In addition, try to limit each phrase to something the user can say without pausing.

Limit the total number of phrases to no more than 100.

## See Also

- [var requiresOnDeviceRecognition: Bool](sfspeechrecognitionrequest/requiresondevicerecognition.md)
  A Boolean value that determines whether a request must keep its audio data on the device.
- [var shouldReportPartialResults: Bool](sfspeechrecognitionrequest/shouldreportpartialresults.md)
  A Boolean value that indicates whether you want intermediate results returned for each utterance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitionrequest/contextualstrings)*