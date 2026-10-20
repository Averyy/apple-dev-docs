# request(_:didFinishWithResult:)

**Framework**: System Extensions  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that the manager completed the request.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func request(_ request: OSSystemExtensionRequest, didFinishWithResult result: OSSystemExtensionRequest.Result)
```

```objc
- (void) request:(OSSystemExtensionRequest *) request didFinishWithResult:(OSSystemExtensionRequestResult) result;
```

#### Discussion

If the request completes with the [`OSSystemExtensionRequest.Result.willCompleteAfterReboot`](../ossystemextensionrequest/result/willcompleteafterreboot.md) result, then the extension isn’t active until after the next restart. After restarting, the most recently-processed request determines the extension’s state. Consider the following scenarios:

- Activate extension and restart: the extension is active upon restarting.
- Activate extension, deactivate extension, and restart: the extension is inactive upon restarting.

## Parameters

- `request`: The request that completed.
- `result`: Additional information about the completion state.

## See Also

### Handling Success and Failure
- [OSSystemExtensionRequest.Result](../ossystemextensionrequest/result.md)
  The result of a completed request, possibly including additional information about the extension’s state.
- [func request(OSSystemExtensionRequest, didFailWithError: any Error)](./request%28_,didfailwitherror%29.md)
  Tells the delegate the manager failed to complete the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionrequestdelegate/request(_:didfinishwithresult:))*