# TimerOccurred

**Framework**: DriverKit  
**Kind**: method

Executes custom code when the timer fires.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
void TimerOccurred(OSAction * action, uint64_t time);
```

#### Discussion

Use this method as a prototype for declaring your own custom timer handlers. When declaring your method, use the [`TYPE`](type.md) macro to indicate that your method has the same parameters and return value as this method.

Use the implementation of your method to perform any custom actions related to the timer’s expiration.

## Parameters

- `action`: The action object being executed.
- `time`: The actual time at which the timer fired. The system calls   precisely when the timer fires and passes that value to this parameter.

## See Also

- [CheckForWork](iotimerdispatchsource/checkforwork.md)
  Checks for events to handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iotimerdispatchsource/timeroccurred)*