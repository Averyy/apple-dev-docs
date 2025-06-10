# range

**Framework**: Speech  
**Kind**: property  
**Required**: Yes

The audio input range that this result applies to.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var range: CMTimeRange { get }
```

## See Also

- [var isFinal: Bool](speechmoduleresult/isfinal.md)
  Whether this result is final at the time it is produced.
- [var resultsFinalizationTime: CMTime](speechmoduleresult/resultsfinalizationtime.md)
  The audio input time up to which results from this module have been finalized (after this result). The module’s results are final up to but not including this time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechmoduleresult/range)*