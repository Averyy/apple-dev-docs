# sessionQueue

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property

The queue on which the reader session delegate callbacks and completion block handlers are dispatched.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var sessionQueue: dispatch_queue_t { get }
```

```objc
@property (nonatomic, readonly) dispatch_queue_t sessionQueue;
```

## See Also

### Working with a Session
- [var delegate: AnyObject?](./delegate.md)
  The delegate of the reader session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadersession-swift.class/sessionqueue)*