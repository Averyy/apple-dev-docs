# cancel()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Cancels the receiver’s download and deletes the downloaded file.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func cancel()
```

```objc
- (void) cancel;
```

## Discussion

This method deletes the partially downloaded file unless you have previously called [`deletesFileUponFailure`](./deletesfileuponfailure.md), passing [`false`](../../Swift/false.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownload/cancel())*