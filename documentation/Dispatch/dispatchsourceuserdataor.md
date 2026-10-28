# DispatchSourceUserDataOr

**Framework**: Dispatch  
**Kind**: protocol  
**Role**: Protocol

A dispatch source that coalesces data you provide using an OR operation.

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
protocol DispatchSourceUserDataOr : DispatchSourceProtocol, Sendable
```

## Overview

You do not adopt this protocol in your objects. Instead, use the [`makeUserDataOrSource(queue:)`](./dispatchsource/makeuserdataorsource%28queue%29.md) method to create an object that adopts this protocol.

To add custom data to the dispatch source, call the [`or(data:)`](./dispatchsourceuserdataor/or%28data%29.md) method.

## Topics

### Getting the Event Data
- [func or(data: UInt)](./dispatchsourceuserdataor/or%28data%29.md)

## Relationships

### Inherits From
- [DispatchSourceProtocol](./dispatchsourceprotocol.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Conforming Types
- [DispatchSource](./dispatchsource.md)

## See Also

### Creating a Custom Source
- [class func makeUserDataAddSource(queue: DispatchQueue?) -> any DispatchSourceUserDataAdd](./dispatchsource/makeuserdataaddsource%28queue%29.md)
  Creates a new dispatch source object that you use to coalesce custom app data using an AND operator.
- [class func makeUserDataOrSource(queue: DispatchQueue?) -> any DispatchSourceUserDataOr](./dispatchsource/makeuserdataorsource%28queue%29.md)
  Creates a new dispatch source object that you use to coalesce custom app data using an OR operator.
- [class func makeUserDataReplaceSource(queue: DispatchQueue?) -> any DispatchSourceUserDataReplace](./dispatchsource/makeuserdatareplacesource%28queue%29.md)
  Creates a new dispatch source object that you use to track custom app data.
- [protocol DispatchSourceUserDataAdd](./dispatchsourceuserdataadd.md)
  A dispatch source that coalesces data you provide using an AND operation.
- [protocol DispatchSourceUserDataReplace](./dispatchsourceuserdatareplace.md)
  A dispatch source that replaces any pending data with the new value you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourceuserdataor)*