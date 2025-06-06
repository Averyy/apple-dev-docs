# NSKeyValueObservingCustomization

**Framework**: Foundation  
**Kind**: protocol

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
- [static func automaticallyNotifiesObservers(for: AnyKeyPath) -> Bool](nskeyvalueobservingcustomization/automaticallynotifiesobservers(for:).md)
- [static func keyPathsAffectingValue(for: AnyKeyPath) -> Set<AnyKeyPath>](nskeyvalueobservingcustomization/keypathsaffectingvalue(for:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol DiscreteFormatStyle](discreteformatstyle.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyvalueobservingcustomization)*