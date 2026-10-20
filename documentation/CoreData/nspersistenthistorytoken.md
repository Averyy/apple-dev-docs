# NSPersistentHistoryToken

**Framework**: Core Data  
**Kind**: class  
**Role**: Class

A bookmark for keeping track the most recent history that you’ve processed.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class NSPersistentHistoryToken
```

```objc
@interface NSPersistentHistoryToken : NSObject
```

## Mentions

- [Consuming relevant store changes](./consuming-relevant-store-changes.md)

#### Overview

You can save a token to disk and fetch history when your app loads based on that token. See [Keep track of the most recent history](./consuming-relevant-store-changes.md#Keep-track-of-the-most-recent-history) in [Consuming relevant store changes](./consuming-relevant-store-changes.md).

## Topics

### Initializers
- [init?(coder: NSCoder)](./nspersistenthistorytoken/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistenthistorytoken)*