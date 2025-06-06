# init(condition:)

**Framework**: Foundation  
**Kind**: init

Initializes a newly allocated `NSConditionLock` object and sets its condition.

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
init(condition: Int)
```

#### Return Value

An initialized condition lock object; may be different than the original receiver.

## Parameters

- `condition`: The user-defined condition for the lock. The value of   is user-defined; see the class description for more information.

## See Also

- [Threading Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconditionlock/init(condition:))*