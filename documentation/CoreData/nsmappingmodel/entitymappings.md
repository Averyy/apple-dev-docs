# entityMappings

**Framework**: Core Data  
**Kind**: property

The entity mappings for the mapping model.

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
var entityMappings: [NSEntityMapping]! { get set }
```

#### Discussion

The order of the mappings in the array determines the order in which they will be processed during migration.

## See Also

- [var entityMappingsByName: [String : NSEntityMapping]](nsmappingmodel/entitymappingsbyname.md)
  The entity mappings for the mapping model, keyed by name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmappingmodel/entitymappings)*