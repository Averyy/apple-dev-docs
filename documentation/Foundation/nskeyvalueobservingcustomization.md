# NSKeyValueObservingCustomization

**Framework**: Foundation  
**Kind**: protocol  
**Role**: Protocol

Conforming to NSKeyValueObservingCustomization is not required to use Key-Value Observing. Provide an implementation of these functions if you need to disable auto-notifying for a key, or add dependent keys

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
protocol NSKeyValueObservingCustomization : NSObjectProtocol
```

## Topics

### Type Methods
- [static func automaticallyNotifiesObservers(for: AnyKeyPath) -> Bool](./nskeyvalueobservingcustomization/automaticallynotifiesobservers%28for%29.md)
- [static func keyPathsAffectingValue(for: AnyKeyPath) -> Set<AnyKeyPath>](./nskeyvalueobservingcustomization/keypathsaffectingvalue%28for%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Protocols
- [protocol DiscreteFormatStyle](./discreteformatstyle.md)
  A format style that transforms a continuous input into a discrete output and provides information about its discretization boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyvalueobservingcustomization)*