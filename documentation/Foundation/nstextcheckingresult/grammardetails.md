# grammarDetails

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly, nullable) NSArray<NSDictionary<NSString *,id> *> * grammarDetails;
```

## Discussion

This array of strings is suitable for presenting to the user.

## See Also

### Text Checking Results for Grammar
- [class func grammarCheckingResult(range: NSRange, details: [[String : Any]]) -> NSTextCheckingResult](./grammarcheckingresult%28range,details%29.md)
  Creates and returns a text checking result with the specified array of grammatical errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/grammardetails)*