# archiverData

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The receiver’s archive data.

**Availability**:
- iOS 2.0+ - Deprecated in 11.0
- iPadOS 2.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use NSKeyedArchiver instead

## Declaration

```swift
var archiverData: NSMutableData { get }
```

```objc
@property (retain, readonly) NSMutableData * archiverData;
```

## Discussion

The returned data object is the same one specified as the argument to [`init(forWritingWith:)`](./init%28forwritingwith%29.md). It contains whatever data has been encoded thus far by invocations of the various encoding methods. It is safest not to invoke this method until after [`encodeRootObject(_:)`](./encoderootobject%28_%29.md) has returned. In other words, although it is possible for a class to invoke this method from within its [`encode(with:)`](../nscoding/encode%28with%29.md) method, that method must not alter the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarchiver/archiverdata)*