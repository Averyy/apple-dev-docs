# request(_:didFinishWithResult:)

**Framework**: System Extensions  
**Kind**: method  
**Required**: Yes

Tells the delegate that the manager completed the request.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func request(_ request: OSSystemExtensionRequest, didFinishWithResult result: OSSystemExtensionRequest.Result)
```

#### Discussion

If the request completes with the [`OSSystemExtensionRequest.Result.willCompleteAfterReboot`](ossystemextensionrequest/result/willcompleteafterreboot.md) result, then the extension isn’t active until after the next restart. After restarting, the most recently-processed request determines the extension’s state. Consider the following scenarios:

- Activate extension and restart: the extension is active upon restarting.
- Activate extension, deactivate extension, and restart: the extension is inactive upon restarting.

## Parameters

- `request`: The request that completed.
- `result`: Additional information about the completion state.

## See Also

- [OSSystemExtensionRequest.Result](ossystemextensionrequest/result.md)
  The result of a completed request, possibly including additional information about the extension’s state.
- [func request(OSSystemExtensionRequest, didFailWithError: any Error)](ossystemextensionrequestdelegate/request(_:didfailwitherror:).md)
  Tells the delegate the manager failed to complete the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionrequestdelegate/request(_:didfinishwithresult:))*