# OSSystemExtensionRequest.Result

**Framework**: System Extensions  
**Kind**: enum  
**Role**: Enumeration

The result of a completed request, possibly including additional information about the extension’s state.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum Result
```

```c
enum OSSystemExtensionRequestResult : NSInteger;
```

## Topics

### Results
- [OSSystemExtensionRequest.Result.completed](./result/completed.md)
  The request completed successfully.
- [OSSystemExtensionRequest.Result.willCompleteAfterReboot](./result/willcompleteafterreboot.md)
  The request requires a restart to complete successfully.
### Initializers
- [init?(rawValue: Int)](./result/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling Success and Failure
- [func request(OSSystemExtensionRequest, didFinishWithResult: OSSystemExtensionRequest.Result)](../ossystemextensionrequestdelegate/request%28_,didfinishwithresult%29.md)
  Tells the delegate that the manager completed the request.
- [func request(OSSystemExtensionRequest, didFailWithError: any Error)](../ossystemextensionrequestdelegate/request%28_,didfailwitherror%29.md)
  Tells the delegate the manager failed to complete the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionrequest/result)*