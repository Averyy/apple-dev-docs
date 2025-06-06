# makeTimerSource(flags:queue:)

**Framework**: Dispatch  
**Kind**: method

Creates a new dispatch source object for monitoring timer events.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func makeTimerSource(flags: DispatchSource.TimerFlags = [], queue: DispatchQueue? = nil) -> any DispatchSourceTimer
```

#### Return Value

A dispatch source object that conforms to the [`DispatchSourceTimer`](dispatchsourcetimer.md) protocol.

#### Discussion

After creating the dispatch source, use the methods of the [`DispatchSourceProtocol`](dispatchsourceprotocol.md) protocol to install the event handlers you need. The returned dispatch source is in the inactive state initially. When you are ready to begin processing events, call its [`activate()`](dispatchobject/activate().md) method.

To schedule timers, use the methods of the [`DispatchSourceTimer`](dispatchsourcetimer.md) protocol. You may schedule timers that fire once or fire multiple times. Each time the timer fires, the dispatch source calls your installed event handler.

## Parameters

- `flags`: Additional flags indicating the behavior of the timer. For a list of possible values, see  .
- `queue`: The dispatch queue to which to execute the installed handlers.

## See Also

- [protocol DispatchSourceTimer](dispatchsourcetimer.md)
  A dispatch source that submits the event handler block based on a timer.
- [DispatchSource.TimerFlags](dispatchsource/timerflags.md)
  Flags to use when configuring a timer dispatch source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource/maketimersource(flags:queue:))*