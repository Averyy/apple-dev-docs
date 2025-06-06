# NSAssertionHandlerKey

**Framework**: Foundation  
**Kind**: var

A key with a corresponding value in the thread dictionary.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSAssertionHandlerKey: String
```

#### Discussion

If you need to customize the behavior of `NSAssertionHandler`, create a subclass, overriding [`handleFailureInMethod:object:file:lineNumber:description:`](nsassertionhandler/handlefailureinmethod:object:file:linenumber:description:.md) and [`handleFailureInFunction:file:lineNumber:description:`](nsassertionhandler/handlefailureinfunction:file:linenumber:description:.md), and install your instance into the current thread’s attributes dictionary with this key.

## See Also

- [var threadDictionary: NSMutableDictionary](thread/threaddictionary.md)
  The thread object’s dictionary.
- [var name: String?](thread/name.md)
  The name of the receiver.
- [var stackSize: Int](thread/stacksize.md)
  The stack size of the receiver, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsassertionhandlerkey)*