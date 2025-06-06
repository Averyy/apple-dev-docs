# analyze(completionHandler:)

**Framework**: Sound Analysis  
**Kind**: method

Analyzes the audio file asynchronously.

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
func analyze() async -> Bool
```

## Mentions

- [Classifying Sounds in an Audio File](classifying-sounds-in-an-audio-file.md)

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func analyze() async -> Bool
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func analyze() async -> Bool
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

The method executes asynchronously and calls the completion handler after the analyzer finishes analyzing the entire file. The audio file analyzer sends errors to each request’s results observer.

If you call the [`cancelAnalysis()`](snaudiofileanalyzer/cancelanalysis().md) method, the analyzer calls your completion handler and passes `false` because it can’t reach the end of the file.

## Parameters

- `completionHandler`: A completion closure (Swift) or block (Objective-C) the analyzer calls when it finishes analyzing a file.

## See Also

- [func analyze()](snaudiofileanalyzer/analyze.md)
  Analyzes the audio file synchronously.
- [func cancelAnalysis()](snaudiofileanalyzer/cancelanalysis.md)
  Cancels all the asynchronous sound analysis requests the analyzer is currently processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snaudiofileanalyzer/analyze(completionhandler:))*