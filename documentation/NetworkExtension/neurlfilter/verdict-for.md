# verdict(for:)

**Framework**: Network Extension  
**Kind**: method

Determines if accessing the specified URL is allowed or denied.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
class func verdict(for url: URL) async -> NEURLFilter.Verdict
```

#### Return Value

A [`NEURLFilter.Verdict`](neurlfilter/verdict.md) that indicates whether the filter allows or denies connecting to the URL. If the verdict is deny, the caller should fail the URL request.

#### Discussion

Callers should honor the return verdict to prevent communication with restricted or malicious sites.

## Parameters

- `url`: The URL to be validated.

## See Also

- [NEURLFilter.Verdict](neurlfilter/verdict.md)
  A verdict returned by a URL filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfilter/verdict(for:))*