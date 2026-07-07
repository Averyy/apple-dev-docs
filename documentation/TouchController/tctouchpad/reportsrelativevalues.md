# reportsRelativeValues

**Framework**: Touch Controller  
**Kind**: property

A Boolean value that represents the touchpad reports deltas.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var reportsRelativeValues: Bool { get set }
```

#### Discussion

If `YES`, the touchpad will report relative delta changes between frames as touch moves instead of absolute positions.

## See Also

- [var contents: TCControlContents?](tctouchpad/contents.md)
  The contents for the touchpad. May be `nil`.
- [var highlightDuration: TimeInterval](tctouchpad/highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchpad/reportsrelativevalues)*