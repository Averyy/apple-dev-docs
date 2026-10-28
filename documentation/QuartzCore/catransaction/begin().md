# begin()

**Framework**: Core Animation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (void) begin;
```

## Discussion

The transaction is nested within the thread’s current transaction, if there is one.

## See Also

### Related Documentation
- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)
### Creating and Committing Transactions
- [class func commit()](./commit%28%29.md)
  Commit all changes made during the current transaction.
- [class func flush()](./flush%28%29.md)
  Flushes any extant implicit transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransaction/begin())*