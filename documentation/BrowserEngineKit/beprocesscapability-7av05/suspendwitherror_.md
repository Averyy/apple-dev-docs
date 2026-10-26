# suspendWithError:

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Suspends the capability.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```objc
- (BOOL) suspendWithError:(NSError **) error;
```

#### Return Value

`YES` if the capability was suspended, or `NO` if an error occurred.

## Parameters

- `error`: On failure, populated with an error if the capability cannot be suspended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beprocesscapability-7av05/suspendwitherror:)*