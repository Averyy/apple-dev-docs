# versionHash

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The relationship’s unique identity.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var versionHash: Data { get }
```

```objc
@property (copy, readonly) NSData * versionHash;
```

#### Discussion

To calculate its version hash, the relationship combines its superclass’s [`versionHash`](../nspropertydescription/versionhash.md) property with the values of [`inverseRelationship`](./inverserelationship.md), [`destinationEntity`](./destinationentity.md), [`minCount`](./mincount.md), and [`maxCount`](./maxcount.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsrelationshipdescription/versionhash)*