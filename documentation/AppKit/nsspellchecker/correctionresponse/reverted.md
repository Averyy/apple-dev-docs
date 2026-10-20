# NSSpellChecker.CorrectionResponse.reverted

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

After the correction was accepted, the user reverted the correction back to the original word.

**Availability**:
- macOS

## Declaration

```swift
case reverted
```

```c
NSCorrectionResponseReverted
```

## See Also

### Enumeration Cases
- [NSSpellChecker.CorrectionResponse.accepted](./accepted.md)
  The user accepted the correction.
- [NSSpellChecker.CorrectionResponse.edited](./edited.md)
  After the correction was accepted, the user edited the corrected word (to something other than its original form.
- [NSSpellChecker.CorrectionResponse.ignored](./ignored.md)
  The user continued in such a way as to ignore the correction.
- [NSSpellChecker.CorrectionResponse.none](./none.md)
  No response was received from the user.
- [NSSpellChecker.CorrectionResponse.rejected](./rejected.md)
  The user rejected the correction by dismissing the correction indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/correctionresponse/reverted)*