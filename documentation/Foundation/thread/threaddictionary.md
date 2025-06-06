# threadDictionary

**Framework**: Foundation  
**Kind**: property

The thread object’s dictionary.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var threadDictionary: NSMutableDictionary { get }
```

#### Discussion

You can use the returned dictionary to store thread-specific data. The thread dictionary is not used during any manipulations of the `NSThread` object—it is simply a place where you can store any interesting data. For example, Foundation uses it to store the thread’s default `NSConnection` and `NSAssertionHandler` instances. You may define your own keys for the dictionary.

## See Also

- [let NSAssertionHandlerKey: String](nsassertionhandlerkey.md)
  A key with a corresponding value in the thread dictionary.
- [var name: String?](thread/name.md)
  The name of the receiver.
- [var stackSize: Int](thread/stacksize.md)
  The stack size of the receiver, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/threaddictionary)*