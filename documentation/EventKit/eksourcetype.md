# EKSourceType

**Framework**: EventKit  
**Kind**: enum  
**Role**: Enumeration

The type of source object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
enum EKSourceType
```

```c
enum EKSourceType : NSInteger;
```

#### Overview

The [`sourceType`](./eksource/sourcetype.md) property will be set to one of these values.

## Topics

### EventKit Source Types
- [EKSourceType.local](./eksourcetype/local.md)
  Represents a local source.
- [EKSourceType.exchange](./eksourcetype/exchange.md)
  Represents an Exchange source.
- [EKSourceType.calDAV](./eksourcetype/caldav.md)
  Represents a CalDAV or iCloud source.
- [EKSourceType.mobileMe](./eksourcetype/mobileme.md)
  Represents a MobileMe source.
- [EKSourceType.subscribed](./eksourcetype/subscribed.md)
  Represents a subscribed source.
- [EKSourceType.birthdays](./eksourcetype/birthdays.md)
  Represents a birthday source.
### Initializers
- [init?(rawValue: Int)](./eksourcetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing Source Properties
- [var sourceIdentifier: String](./eksource/sourceidentifier.md)
  A unique identifier for the source object.
- [var sourceType: EKSourceType](./eksource/sourcetype.md)
  The type of this source object.
- [var title: String](./eksource/title.md)
  The name of this source object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/eksourcetype)*