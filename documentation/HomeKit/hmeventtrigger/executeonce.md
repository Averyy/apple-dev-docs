# executeOnce

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that can execute the trigger many times.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var executeOnce: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL executeOnce;
```

#### Discussion

Disables the trigger after its first execution if [`true`](../../Swift/true.md).

## See Also

### Controlling recurrence
- [var recurrences: [DateComponents]?](./recurrences.md)
  Specifies the days on which the trigger can execute.
- [func updateRecurrences([DateComponents]?, completionHandler: ((any Error)?) -> Void)](./updaterecurrences%28_,completionhandler%29.md)
  Updates the days of the week the trigger can repeat.
- [func updateExecuteOnce(Bool, completionHandler: ((any Error)?) -> Void)](./updateexecuteonce%28_,completionhandler%29.md)
  Updates the repetition status of the event trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtrigger/executeonce)*