# grammarCheckingResult(range:details:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns a text checking result with the specified array of grammatical errors.

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
class func grammarCheckingResult(range: NSRange, details: [[String : Any]]) -> NSTextCheckingResult
```

```objc
+ (NSTextCheckingResult *) grammarCheckingResultWithRange:(NSRange) range details:(NSArray<NSDictionary<NSString *,id> *> *) details;
```

#### Return Value

Returns an `NSTextCheckingResult` with the specified [`range`](./range.md) and a [`resultType`](./resulttype.md) of [`grammar`](./checkingtype/grammar.md).

## Parameters

- `range`: The range of the detected result.
- `details`: An array of details regarding the grammatical errors. This array of strings is suitable for presenting to the user.

## See Also

### Text Checking Results for Grammar
- [var grammarDetails: [[String : Any]]?](./grammardetails.md)
  The details of a located grammatical type checking result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/grammarcheckingresult(range:details:))*