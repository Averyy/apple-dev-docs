# isOrdered

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the relationship preserves the order of the referenced managed objects.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isOrdered: Bool { get set }
```

```objc
@property (getter=isOrdered) BOOL ordered;
```

#### Discussion

The default value is [`false`](../../Swift/false.md).

## See Also

### Configuring the Destination
- [var inverseRelationship: NSRelationshipDescription?](./inverserelationship.md)
  The relationship that represents the inverse of the current relationship.
- [var destinationEntity: NSEntityDescription?](./destinationentity.md)
  The type of object the relationship contains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsrelationshipdescription/isordered)*