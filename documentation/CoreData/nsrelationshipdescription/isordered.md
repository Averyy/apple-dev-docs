# isOrdered

**Framework**: Core Data  
**Kind**: property

A Boolean value that determines whether the relationship preserves the order of the referenced managed objects.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isOrdered: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var inverseRelationship: NSRelationshipDescription?](nsrelationshipdescription/inverserelationship.md)
  The relationship that represents the inverse of the current relationship.
- [var destinationEntity: NSEntityDescription?](nsrelationshipdescription/destinationentity.md)
  The type of object the relationship contains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsrelationshipdescription/isordered)*