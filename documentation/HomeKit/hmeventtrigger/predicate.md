# predicate

**Framework**: HomeKit  
**Kind**: property

The predicate to evaluate before executing the scene associated with the event trigger.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var predicate: NSPredicate? { get }
```

#### Discussion

By default, the value of this property is `nil`, which means that it evaluates as [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [func updatePredicate(NSPredicate?, completionHandler: ((any Error)?) -> Void)](hmeventtrigger/updatepredicate(_:completionhandler:).md)
  Replaces the predicate used to evaluate execution of the scene associated with the event trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtrigger/predicate)*