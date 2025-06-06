# ReferenceConvertible

**Framework**: Foundation  
**Kind**: protocol

A decoration applied to types that are backed by a Foundation reference type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol ReferenceConvertible : CustomDebugStringConvertible, CustomStringConvertible, Hashable, _ObjectiveCBridgeable
```

#### Overview

All `ReferenceConvertible` types are hashable, equatable, and provide description functions.

> ⚠️ **Warning**:  Don’t create new conformances to this protocol. `ReferenceConvertible` only supports types provided by the SDK.

 Don’t create new conformances to this protocol. `ReferenceConvertible` only supports types provided by the SDK.

## Topics

### Supporting types
- [associatedtype ReferenceType : NSObject, NSCopying](referenceconvertible/referencetype.md)

## Relationships

### Inherits From
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
### Conforming Types
- [AffineTransform](affinetransform.md)
- [Calendar](calendar.md)
- [CharacterSet](characterset.md)
- [Data](data.md)
- [Date](date.md)
- [DateComponents](datecomponents.md)
- [DateInterval](dateinterval.md)
- [IndexPath](indexpath.md)
- [IndexSet](indexset.md)
- [Locale](locale.md)
- [Measurement](measurement.md)
- [Notification](notification.md)
- [PersonNameComponents](personnamecomponents.md)
- [TimeZone](timezone.md)
- [URL](url.md)
- [URLComponents](urlcomponents.md)
- [URLQueryItem](urlqueryitem.md)
- [URLRequest](urlrequest.md)
- [UUID](uuid.md)

## See Also

- [Classes Bridged to Swift Standard Library Value Types](classes-bridged-to-swift-standard-library-value-types.md)
  Use bridged reference types when you need reference semantics or Foundation-specific behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/referenceconvertible)*