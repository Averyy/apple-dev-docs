# linkCheckingResult(range:url:)

**Framework**: Foundation  
**Kind**: method

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

#### Return Value

Returns an `NSTextCheckingResult` with the specified [`range`](nstextcheckingresult/range.md) and a [`resultType`](nstextcheckingresult/resulttype.md) of [`link`](nstextcheckingresult/checkingtype/link.md).

## Parameters

- `range`: The range of the detected result.
- `url`: The URL.

## See Also

- [var url: URL?](nstextcheckingresult/url.md)
  The URL of a type checking result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/linkcheckingresult(range:url:))*