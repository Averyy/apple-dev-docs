# NotificationCenter.BaseMessageIdentifier

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A type for use when defining optional Message identifiers.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct BaseMessageIdentifier<MessageType>
```

## Overview

See [`NotificationCenter.MessageIdentifier`](./messageidentifier.md) for an example of how to use this type when defining your own message identifiers.

## Topics

### Creating an identifier for a main actor message
- [init()](./basemessageidentifier/init%28%29-66tt2.md)
### Creating an identifier for an asynchronous message
- [init()](./basemessageidentifier/init%28%29-2yi72.md)

## Relationships

### Conforms To
- [NotificationCenter.MessageIdentifier](./messageidentifier.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Using message identifiers
- [NotificationCenter.MessageIdentifier](./messageidentifier.md)
  An optional identifier to associate a given message with a given type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/basemessageidentifier)*