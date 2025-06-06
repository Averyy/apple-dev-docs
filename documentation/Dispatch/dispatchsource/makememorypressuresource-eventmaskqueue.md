# makeMemoryPressureSource(eventMask:queue:)

**Framework**: Dispatch  
**Kind**: method

Creates a new dispatch source object that monitors the system for changes in the memory pressure condition.

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
class func makeMemoryPressureSource(eventMask: DispatchSource.MemoryPressureEvent, queue: DispatchQueue? = nil) -> any DispatchSourceMemoryPressure
```

#### Return Value

A dispatch source object that conforms to the [`DispatchSourceMemoryPressure`](dispatchsourcememorypressure.md) protocol.

#### Discussion

After creating the dispatch source, use the methods of the [`DispatchSourceProtocol`](dispatchsourceprotocol.md) protocol to install the event handlers you need. The returned dispatch source is in the inactive state initially. When you are ready to begin processing events, call its [`activate()`](dispatchobject/activate().md) method.

## Parameters

- `eventMask`: The set of events you want to monitor. For a list of possible values, see  .
- `queue`: The dispatch queue to use when executing the installed handlers.

## See Also

- [protocol DispatchSourceMemoryPressure](dispatchsourcememorypressure.md)
  A dispatch source that monitors the system for changes in the memory pressure condition.
- [DispatchSource.MemoryPressureEvent](dispatchsource/memorypressureevent.md)
  Memory pressure events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource/makememorypressuresource(eventmask:queue:))*