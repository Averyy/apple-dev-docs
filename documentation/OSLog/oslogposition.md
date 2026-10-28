# OSLogPosition

**Framework**: OSLog  
**Kind**: class  
**Role**: Class

A representation of a point in a sequence of entries in the unified logging system.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class OSLogPosition
```

```objc
@interface OSLogPosition : NSObject
```

## Overview

Generate positions with [`OSLogStore`](./oslogstore.md) instance methods and use them to view entries from a particular starting point.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Entry Data
- [class OSLogMessageComponent](./oslogmessagecomponent.md)
  The message arguments for a particular entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogposition)*