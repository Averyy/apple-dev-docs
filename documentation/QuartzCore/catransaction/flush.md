# flush()

**Framework**: Core Animation  
**Kind**: method

Flushes any extant implicit transaction.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func flush()
```

#### Discussion

Delays the commit until any nested explicit transactions have completed.

Flush is typically called automatically at the end of the current runloop, regardless of the runloop mode. If your application does not have a runloop, you must call this method explicitly.

However, you should attempt to avoid calling `flush` explicitly. By allowing `flush` to execute during the runloop your application will achieve better performance, atomic screen updates will be preserved, and transactions and animations that work from transaction to transaction will continue to function.

## See Also

- [class func begin()](catransaction/begin.md)
  Begin a new transaction for the current thread.
- [class func commit()](catransaction/commit.md)
  Commit all changes made during the current transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransaction/flush())*