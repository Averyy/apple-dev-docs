# HKQueryAnchor

**Framework**: HealthKit  
**Kind**: class

An object used to identify all the samples previously returned by an anchored object query.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKQueryAnchor
```

#### Overview

The system returns [`HKQueryAnchor`](hkqueryanchor.md) objects in both the anchored object query’s results handler and it’s update handler. Use the anchors to query for samples added or deleted after the result or update.

## Topics

### Creating Anchor Objects
- [convenience init(fromValue: Int)](hkqueryanchor/init(fromvalue:).md)
  Returns an anchor object from the provided anchor value.
### Initializers
- [init?(coder: NSCoder)](hkqueryanchor/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkqueryanchor)*