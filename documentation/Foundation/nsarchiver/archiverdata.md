# archiverData

**Framework**: Foundation  
**Kind**: property

The receiver’s archive data.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
var archiverData: NSMutableData { get }
```

#### Discussion

The returned data object is the same one specified as the argument to [`init(forWritingWith:)`](nsarchiver/init(forwritingwith:).md). It contains whatever data has been encoded thus far by invocations of the various encoding methods. It is safest not to invoke this method until after [`encodeRootObject(_:)`](nsarchiver/encoderootobject(_:).md) has returned. In other words, although it is possible for a class to invoke this method from within its [`encode(with:)`](nscoding/encode(with:).md) method, that method must not alter the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarchiver/archiverdata)*