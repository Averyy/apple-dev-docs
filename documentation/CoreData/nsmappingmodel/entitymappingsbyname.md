# entityMappingsByName

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The entity mappings for the mapping model, keyed by name.

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
var entityMappingsByName: [String : NSEntityMapping] { get }
```

```objc
@property (copy, readonly) NSDictionary<NSString *,NSEntityMapping *> * entityMappingsByName;
```

## See Also

### Managing Entity Mappings
- [var entityMappings: [NSEntityMapping]!](./entitymappings.md)
  The entity mappings for the mapping model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmappingmodel/entitymappingsbyname)*