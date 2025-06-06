# DispatchSourceUserDataAdd

**Framework**: Dispatch  
**Kind**: protocol

A dispatch source that coalesces data you provide using an AND operation.

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
protocol DispatchSourceUserDataAdd : DispatchSourceProtocol, Sendable
```

#### Overview

You do not adopt this protocol in your objects. Instead, use the [`makeUserDataAddSource(queue:)`](dispatchsource/makeuserdataaddsource(queue:).md) method to create an object that adopts this protocol.

To add custom data to the dispatch source, call the [`add(data:)`](dispatchsourceuserdataadd/add(data:).md) method.

## Topics

### Getting the Event Data
- [func add(data: UInt)](dispatchsourceuserdataadd/add(data:).md)
  Adds the value to the current pending data.

## Relationships

### Inherits From
- [DispatchSourceProtocol](dispatchsourceprotocol.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
### Conforming Types
- [DispatchSource](dispatchsource.md)

## See Also

- [class func makeUserDataAddSource(queue: DispatchQueue?) -> any DispatchSourceUserDataAdd](dispatchsource/makeuserdataaddsource(queue:).md)
  Creates a new dispatch source object that you use to coalesce custom app data using an AND operator.
- [class func makeUserDataOrSource(queue: DispatchQueue?) -> any DispatchSourceUserDataOr](dispatchsource/makeuserdataorsource(queue:).md)
  Creates a new dispatch source object that you use to coalesce custom app data using an OR operator.
- [class func makeUserDataReplaceSource(queue: DispatchQueue?) -> any DispatchSourceUserDataReplace](dispatchsource/makeuserdatareplacesource(queue:).md)
  Creates a new dispatch source object that you use to track custom app data.
- [protocol DispatchSourceUserDataOr](dispatchsourceuserdataor.md)
  A dispatch source that coalesces data you provide using an OR operation.
- [protocol DispatchSourceUserDataReplace](dispatchsourceuserdatareplace.md)
  A dispatch source that replaces any pending data with the new value you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourceuserdataadd)*