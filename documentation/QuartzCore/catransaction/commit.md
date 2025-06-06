# commit()

**Framework**: Core Animation  
**Kind**: method

Commit all changes made during the current transaction.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func commit()
```

#### Discussion

Raises an exception if no current transaction exists.

## See Also

- [class func begin()](catransaction/begin.md)
  Begin a new transaction for the current thread.
- [class func flush()](catransaction/flush.md)
  Flushes any extant implicit transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransaction/commit())*