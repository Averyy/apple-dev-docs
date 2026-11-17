# BEWebContentFilter.PermissionDecision.pending

**Framework**: BrowserEngineKit  
**Kind**: case  
**Role**: Case

A value that indicates the request awaits a guardian’s response.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
case pending
```

```c
BEWebContentFilterPermissionDecisionPending
```

## See Also

### Determining the result
- [BEWebContentFilter.PermissionDecision.allowed](./allowed.md)
  A value that indicates a guardian approves the request and the system can add the URL to the allow list.
- [BEWebContentFilter.PermissionDecision.denied](./denied.md)
  A value that indicates a guardian denies the request.
- [BEWebContentFilter.PermissionDecision.error](./error.md)
  A value that indicates the system fails to retrieve a decision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bewebcontentfilter/permissiondecision/pending)*