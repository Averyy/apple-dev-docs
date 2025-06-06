# current

**Framework**: Foundation  
**Kind**: property

Returns the operation queue that launched the current operation.

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
class var current: OperationQueue? { get }
```

#### Return Value

The operation queue that started the operation or `nil` if the queue could not be determined.

#### Discussion

You can use this method from within a running operation object to get a reference to the operation queue that started it. Calling this method from outside the context of a running operation typically results in `nil` being returned.

## See Also

- [Concurrency Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091)
- [class var main: OperationQueue](operationqueue/main.md)
  Returns the operation queue associated with the main thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/current)*