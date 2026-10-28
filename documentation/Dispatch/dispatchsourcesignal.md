# DispatchSourceSignal

**Framework**: Dispatch  
**Kind**: protocol  
**Role**: Protocol

A dispatch source that monitors the current process for UNIX signals.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
protocol DispatchSourceSignal : DispatchSourceProtocol, Sendable
```

## Overview

You do not adopt this protocol in your objects. Instead, use the [`makeSignalSource(signal:queue:)`](./dispatchsource/makesignalsource%28signal,queue%29.md) method to create an object that adopts this protocol.

## Relationships

### Inherits From
- [DispatchSourceProtocol](./dispatchsourceprotocol.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Conforming Types
- [DispatchSource](./dispatchsource.md)

## See Also

### Creating a Signal Source
- [class func makeSignalSource(signal: Int32, queue: DispatchQueue?) -> any DispatchSourceSignal](./dispatchsource/makesignalsource%28signal,queue%29.md)
  Creates a new dispatch source object that monitors the arrival of a UNIX signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourcesignal)*