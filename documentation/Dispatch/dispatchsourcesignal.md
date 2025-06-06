# DispatchSourceSignal

**Framework**: Dispatch  
**Kind**: protocol

A dispatch source that monitors the current process for UNIX signals.

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
protocol DispatchSourceSignal : DispatchSourceProtocol, Sendable
```

#### Overview

You do not adopt this protocol in your objects. Instead, use the [`makeSignalSource(signal:queue:)`](dispatchsource/makesignalsource(signal:queue:).md) method to create an object that adopts this protocol.

## Relationships

### Inherits From
- [DispatchSourceProtocol](dispatchsourceprotocol.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
### Conforming Types
- [DispatchSource](dispatchsource.md)

## See Also

- [class func makeSignalSource(signal: Int32, queue: DispatchQueue?) -> any DispatchSourceSignal](dispatchsource/makesignalsource(signal:queue:).md)
  Creates a new dispatch source object that monitors the arrival of a UNIX signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourcesignal)*