# requestWithError:

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Requests a capability for the current process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```objc
- (id<BEProcessCapabilityGrant>) requestWithError:(NSError **) error;
```

#### Discussion

This method returns the granted capability, if possible; otherwise, it returns `nil` and sets the argument error object.

## Parameters

- `error`: A pointer to an error object that describes why the method failed, or `nil` if no error occurred. Pass `nil` to ignore the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beprocesscapability-7av05/requestwitherror:)*