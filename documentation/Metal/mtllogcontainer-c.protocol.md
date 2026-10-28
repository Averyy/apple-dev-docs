# MTLLogContainer

**Framework**: Metal  
**Kind**: protocol  
**Role**: Protocol

A collection of logged messages, created when a Metal device runs a command buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@protocol MTLLogContainer <NSObject, NSFastEnumeration>
```

## Overview

Enumerate a log container object to get a list of [`MTLFunctionLog`](./mtlfunctionlog.md) instances.

## Relationships

### Inherits From
- [NSFastEnumeration](../Foundation/nsfastenumeration.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Shader logs
- [protocol MTLFunctionLog](./mtlfunctionlog.md)
  A log entry a Metal device generates when the it runs a command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllogcontainer-c.protocol)*