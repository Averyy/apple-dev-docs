# recurrences

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

Specifies the days on which the trigger can execute.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var recurrences: [DateComponents]? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<NSDateComponents *> * recurrences;
```

#### Discussion

This property represents the days of the week that the trigger recurs; the trigger ignores all properties other than [`weekday`](../../Foundation/datecomponents/weekday.md) on the [`DateComponents`](../../Foundation/datecomponents.md) object.

## See Also

### Controlling recurrence
- [func updateRecurrences([DateComponents]?, completionHandler: ((any Error)?) -> Void)](./updaterecurrences%28_,completionhandler%29.md)
  Updates the days of the week the trigger can repeat.
- [var executeOnce: Bool](./executeonce.md)
  A Boolean that can execute the trigger many times.
- [func updateExecuteOnce(Bool, completionHandler: ((any Error)?) -> Void)](./updateexecuteonce%28_,completionhandler%29.md)
  Updates the repetition status of the event trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtrigger/recurrences)*