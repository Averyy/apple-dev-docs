# BEWebContentFilter.PermissionDecision.denied

**Framework**: BrowserEngineKit  
**Kind**: case  
**Role**: Case

A value that indicates a guardian denies the request.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
case denied
```

```c
BEWebContentFilterPermissionDecisionDenied
```

## See Also

### Determining the result
- [BEWebContentFilter.PermissionDecision.allowed](./allowed.md)
  A value that indicates a guardian approves the request and the system can add the URL to the allow list.
- [BEWebContentFilter.PermissionDecision.pending](./pending.md)
  A value that indicates the request awaits a guardian’s response.
- [BEWebContentFilter.PermissionDecision.error](./error.md)
  A value that indicates the system fails to retrieve a decision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bewebcontentfilter/permissiondecision/denied)*