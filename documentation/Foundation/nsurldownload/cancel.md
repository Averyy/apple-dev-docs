# cancel()

**Framework**: Foundation  
**Kind**: method

Cancels the receiver’s download and deletes the downloaded file.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func cancel()
```

#### Discussion

This method deletes the partially downloaded file unless you have previously called [`deletesFileUponFailure`](nsurldownload/deletesfileuponfailure.md), passing [`false`](https://developer.apple.com/documentation/swift/false).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownload/cancel())*