# backgroundDownload:didReceiveChallenge:completionHandler:

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```objc
- (void) backgroundDownload:(BADownload *) download didReceiveChallenge:(NSURLAuthenticationChallenge *) challenge completionHandler:(void (^)(NSURLSessionAuthChallengeDisposition disposition, NSURLCredential *credential)) completionHandler;
```

## See Also

### Processing downloads
- [- backgroundDownload:finishedWithFileURL:](./backgrounddownload_finishedwithfileurl_.md)
- [- backgroundDownload:failedWithError:](./backgrounddownload_failedwitherror_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloaderextension-zuvm/backgrounddownload:didreceivechallenge:completionhandler:)*