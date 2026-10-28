# resumeMonitoring:completionHandler:

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Informs the system that it needs to resume monitoring the download.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```objc
- (void) resumeMonitoring:(NSURL *) url completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

Call this method when your browser resumes the download after an interruption, for example, someone cancels the download, or your networking extension encounters a network error.

## Parameters

- `url`: The placeholder location your networking extension previously received when it called [`beginMonitoring:`](./beginmonitoring_.md).
- `completionHandler`: A closure the system calls when it finishes processing the request. If it fails, the parameter is an error object that describes the failure; otherwise, it’s `nil`.

## See Also

### Reporting progress to the system
- [- beginMonitoring:](./beginmonitoring_.md)
  Informs the system to start monitoring the download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedownloadmonitor-9y4hu/resumemonitoring:completionhandler:)*