# request(_:didFailWithError:)

**Framework**: System Extensions  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate the manager failed to complete the request.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func request(_ request: OSSystemExtensionRequest, didFailWithError error: any Error)
```

```objc
- (void) request:(OSSystemExtensionRequest *) request didFailWithError:(NSError *) error;
```

## Mentions

- [Installing System Extensions and Drivers](../installing-system-extensions-and-drivers.md)

## Parameters

- `request`: The request that failed.
- `error`: The reason the request failed.

## See Also

### Handling Success and Failure
- [func request(OSSystemExtensionRequest, didFinishWithResult: OSSystemExtensionRequest.Result)](./request%28_,didfinishwithresult%29.md)
  Tells the delegate that the manager completed the request.
- [OSSystemExtensionRequest.Result](../ossystemextensionrequest/result.md)
  The result of a completed request, possibly including additional information about the extension’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionrequestdelegate/request(_:didfailwitherror:))*