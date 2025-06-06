# SuspendingClock.Instant

**Framework**: Swift  
**Kind**: struct

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct Instant
```

## Topics

### Operators
- [static func + (SuspendingClock.Instant, Duration) -> SuspendingClock.Instant](suspendingclock/instant/+(_:_:).md)
- [static func += (inout SuspendingClock.Instant, Duration)](suspendingclock/instant/+=(_:_:).md)
- [static func - (SuspendingClock.Instant, Duration) -> SuspendingClock.Instant](suspendingclock/instant/-(_:_:)-7hsct.md)
- [static func - (SuspendingClock.Instant, SuspendingClock.Instant) -> Duration](suspendingclock/instant/-(_:_:)-883fd.md)
- [static func -= (inout SuspendingClock.Instant, Duration)](suspendingclock/instant/-=(_:_:).md)
### Initializers
- [init(from: any Decoder) throws](suspendingclock/instant/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](suspendingclock/instant/encode(to:).md)
  Encodes this value into the given encoder.
### Type Properties
- [static var now: SuspendingClock.Instant](suspendingclock/instant/now.md)
### Default Implementations
- [Comparable Implementations](suspendingclock/instant/comparable-implementations.md)
- [Equatable Implementations](suspendingclock/instant/equatable-implementations.md)
- [Hashable Implementations](suspendingclock/instant/hashable-implementations.md)
- [InstantProtocol Implementations](suspendingclock/instant/instantprotocol-implementations.md)

## Relationships

### Conforms To
- [Comparable](comparable.md)
- [Copyable](copyable.md)
- [Decodable](decodable.md)
- [Encodable](encodable.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [InstantProtocol](instantprotocol.md)
- [Sendable](sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/suspendingclock/instant)*