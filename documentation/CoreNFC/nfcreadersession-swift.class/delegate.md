# delegate

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property

The delegate of the reader session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
weak var delegate: AnyObject? { get }
```

```objc
@property (nonatomic, weak, readonly) id delegate;
```

## See Also

### Working with a Session
- [var sessionQueue: dispatch_queue_t](./sessionqueue.md)
  The queue on which the reader session delegate callbacks and completion block handlers are dispatched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadersession-swift.class/delegate)*