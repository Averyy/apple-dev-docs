# regularExpression

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The regular expression of a type checking result.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var regularExpression: NSRegularExpression? { get }
```

```objc
@property (copy, readonly, nullable) NSRegularExpression * regularExpression;
```

## See Also

### Text Checking Results for Regular Expressions
- [class func regularExpressionCheckingResult(ranges: NSRangePointer, count: Int, regularExpression: NSRegularExpression) -> NSTextCheckingResult](./regularexpressioncheckingresult%28ranges,count,regularexpression%29.md)
  Creates and returns a type checking result with the specified regular expression data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/regularexpression)*