# makeSignalSource(signal:queue:)

**Framework**: Dispatch  
**Kind**: method

Creates a new dispatch source object that monitors the arrival of a UNIX signal.

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
class func makeSignalSource(signal: Int32, queue: DispatchQueue? = nil) -> any DispatchSourceSignal
```

#### Return Value

A dispatch source object that conforms to the [`DispatchSourceSignal`](dispatchsourcesignal.md) protocol.

#### Discussion

After creating the dispatch source, use the methods of the [`DispatchSourceProtocol`](dispatchsourceprotocol.md) protocol to install the event handlers you need. The returned dispatch source is in the inactive state initially. When you are ready to begin processing events, call its [`activate()`](dispatchobject/activate().md) method.

## Parameters

- `signal`: The Unix signal number to monitor.
- `queue`: The dispatch queue to use when executing the installed handlers.

## See Also

- [protocol DispatchSourceSignal](dispatchsourcesignal.md)
  A dispatch source that monitors the current process for UNIX signals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource/makesignalsource(signal:queue:))*