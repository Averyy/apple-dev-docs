# grammarDetails

**Framework**: Foundation  
**Kind**: property

The details of a located grammatical type checking result.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var grammarDetails: [[String : Any]]? { get }
```

#### Discussion

This array of strings is suitable for presenting to the user.

## See Also

- [class func grammarCheckingResult(range: NSRange, details: [[String : Any]]) -> NSTextCheckingResult](nstextcheckingresult/grammarcheckingresult(range:details:).md)
  Creates and returns a text checking result with the specified array of grammatical errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/grammardetails)*