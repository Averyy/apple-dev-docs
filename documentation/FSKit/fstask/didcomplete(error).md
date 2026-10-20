# didComplete(error:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method

Informs the client that the task completed.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func didComplete(error: (any Error)?)
```

```objc
- (void) didCompleteWithError:(NSError *) error;
```

## Parameters

- `error`: `nil` if the task completed successfully; otherwise, an error that caused the task to fail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fstask/didcomplete(error:))*