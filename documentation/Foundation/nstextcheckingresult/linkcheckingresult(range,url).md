# linkCheckingResult(range:url:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns a text checking result with the specified URL.

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
class func linkCheckingResult(range: NSRange, url: URL) -> NSTextCheckingResult
```

```objc
+ (NSTextCheckingResult *) linkCheckingResultWithRange:(NSRange) range URL:(NSURL *) url;
```

## Return Value

Returns an `NSTextCheckingResult` with the specified [`range`](./range.md) and a [`resultType`](./resulttype.md) of [`link`](./checkingtype/link.md).

## Parameters

- `range`: The range of the detected result.
- `url`: The URL.

## See Also

### Text Checking Results for URLs
- [var url: URL?](./url.md)
  The URL of a type checking result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/linkcheckingresult(range:url:))*