# isIndexingEnabled

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether Core Data is currently updating the Core Spotlight index with the persistent store’s entities.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var isIndexingEnabled: Bool { get }
```

```objc
@property (readonly, getter=isIndexingEnabled) BOOL indexingEnabled;
```

## See Also

### Configuring the Index
- [func domainIdentifier() -> String](./domainidentifier%28%29.md)
  Returns the domain identifier.
- [func indexName() -> String?](./indexname%28%29.md)
  Returns the index’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/isindexingenabled)*