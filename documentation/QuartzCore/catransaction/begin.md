# begin()

**Framework**: Core Animation  
**Kind**: method

Begin a new transaction for the current thread.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func begin()
```

#### Discussion

The transaction is nested within the thread’s current transaction, if there is one.

## See Also

- [Core Animation Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)
- [class func commit()](catransaction/commit.md)
  Commit all changes made during the current transaction.
- [class func flush()](catransaction/flush.md)
  Flushes any extant implicit transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransaction/begin())*