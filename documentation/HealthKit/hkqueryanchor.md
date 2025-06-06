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

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkqueryanchor)*