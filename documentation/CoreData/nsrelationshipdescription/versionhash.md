# versionHash

**Framework**: Core Data  
**Kind**: property

The relationship’s unique identity.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var versionHash: Data { get }
```

#### Discussion

To calculate its version hash, the relationship combines its superclass’s [`versionHash`](nspropertydescription/versionhash.md) property with the values of [`inverseRelationship`](nsrelationshipdescription/inverserelationship.md), [`destinationEntity`](nsrelationshipdescription/destinationentity.md), [`minCount`](nsrelationshipdescription/mincount.md), and [`maxCount`](nsrelationshipdescription/maxcount.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsrelationshipdescription/versionhash)*