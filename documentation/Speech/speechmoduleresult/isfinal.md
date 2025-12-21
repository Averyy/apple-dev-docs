# isFinal

**Framework**: Speech  
**Kind**: property

Whether this result is final at the time it is produced.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var isFinal: Bool { get }
```

#### Discussion

- If `true`, then this result is final. There will be no later result over its range.
- If `false`, then this result is volatile. There may or may not be a later result over this result’s range. In particular, there is no guarantee that this result will be reissued with this property set to `true`.

Equivalent to `resultsFinalizationTime >= range.end`.

## See Also

- [var resultsFinalizationTime: CMTime](speechmoduleresult/resultsfinalizationtime.md)
  The audio input time up to which results from this module have been finalized (after this result). The module’s results are final up to but not including this time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechmoduleresult/isfinal)*