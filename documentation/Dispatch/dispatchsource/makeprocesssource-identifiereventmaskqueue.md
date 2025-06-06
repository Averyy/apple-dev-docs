# makeProcessSource(identifier:eventMask:queue:)

**Framework**: Dispatch  
**Kind**: method

Creates a new dispatch source object for monitoring the specified process.

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
class func makeProcessSource(identifier: pid_t, eventMask: DispatchSource.ProcessEvent, queue: DispatchQueue? = nil) -> any DispatchSourceProcess
```

#### Return Value

A dispatch source object that conforms to the [`DispatchSourceProcess`](dispatchsourceprocess.md) protocol.

#### Discussion

After creating the dispatch source, use the methods of the [`DispatchSourceProtocol`](dispatchsourceprotocol.md) protocol to install the event handlers you need. The returned dispatch source is in the inactive state initially. When you are ready to begin processing events, call its [`activate()`](dispatchobject/activate().md) method.

## Parameters

- `identifier`: The process identifier of the process you want to monitor.
- `eventMask`: The set of events you want to monitor. For a list of possible values, see  .
- `queue`: The dispatch queue to use when executing the installed handlers.

## See Also

- [protocol DispatchSourceProcess](dispatchsourceprocess.md)
  A dispatch source that monitors an external process for events.
- [DispatchSource.ProcessEvent](dispatchsource/processevent.md)
  Events related to a process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource/makeprocesssource(identifier:eventmask:queue:))*