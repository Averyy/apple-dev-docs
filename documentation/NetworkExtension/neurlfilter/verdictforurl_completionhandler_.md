# verdictForURL:completionHandler:

**Framework**: Network Extension  
**Kind**: method  
**Role**: Type Method

Determines if accessing the specified URL is allowed or denied.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```objc
+ (void) verdictForURL:(NSURL *) url completionHandler:(void (^)(NEURLFilterVerdict result)) completionHandler;
```

#### Discussion

Callers should honor the return verdict to prevent communication with restricted or malicious sites.

## Parameters

- `url`: The URL to be validated.
- `completionHandler`: A block that the system calls when it completes validation. The block receives a [`NEURLFilter.Verdict`](./verdict.md) parameter that indicates whether the filter allows or denies connecting to the URL. If the verdict is deny, the caller should fail the URL request.

## See Also

### Evaluating a URL
- [NEURLFilter.Verdict](./verdict.md)
  A verdict returned by a URL filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfilter/verdictforurl:completionhandler:)*