# OSSystemExtensionRequest.Result

**Framework**: System Extensions  
**Kind**: enum

The result of a completed request, possibly including additional information about the extension’s state.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum Result
```

## Topics

### Results
- [OSSystemExtensionRequest.Result.completed](ossystemextensionrequest/result/completed.md)
  The request completed successfully.
- [OSSystemExtensionRequest.Result.willCompleteAfterReboot](ossystemextensionrequest/result/willcompleteafterreboot.md)
  The request requires a restart to complete successfully.
### Initializers
- [init?(rawValue: Int)](ossystemextensionrequest/result/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func request(OSSystemExtensionRequest, didFinishWithResult: OSSystemExtensionRequest.Result)](ossystemextensionrequestdelegate/request(_:didfinishwithresult:).md)
  Tells the delegate that the manager completed the request.
- [func request(OSSystemExtensionRequest, didFailWithError: any Error)](ossystemextensionrequestdelegate/request(_:didfailwitherror:).md)
  Tells the delegate the manager failed to complete the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionrequest/result)*