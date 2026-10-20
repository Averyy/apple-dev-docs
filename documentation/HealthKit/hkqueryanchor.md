# HKQueryAnchor

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HKQueryAnchor : NSObject
```

#### Overview

The system returns [`HKQueryAnchor`](./hkqueryanchor.md) objects in both the anchored object query’s results handler and it’s update handler. Use the anchors to query for samples added or deleted after the result or update.

## Topics

### Creating Anchor Objects
- [convenience init(fromValue: Int)](./hkqueryanchor/init%28fromvalue%29.md)
  Returns an anchor object from the provided anchor value.
### Initializers
- [init?(coder: NSCoder)](./hkqueryanchor/init%28coder%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkqueryanchor)*