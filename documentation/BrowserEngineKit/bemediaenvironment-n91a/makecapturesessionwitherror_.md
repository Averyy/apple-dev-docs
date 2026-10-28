# makeCaptureSessionWithError:

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Creates a new capture session in this media environment.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```objc
- (AVCaptureSession *) makeCaptureSessionWithError:(NSError **) error;
```

## Discussion

The system only allows a capture session to start when its media environment is active (see [`activateWithError:`](./activatewitherror_.md)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bemediaenvironment-n91a/makecapturesessionwitherror:)*