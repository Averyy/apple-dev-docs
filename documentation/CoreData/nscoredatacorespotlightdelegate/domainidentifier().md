# domainIdentifier()

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns the domain identifier.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
func domainIdentifier() -> String
```

```objc
- (NSString *) domainIdentifier;
```

#### Discussion

The default value is the persistent store’s identifier.

## See Also

### Configuring the Index
- [var isIndexingEnabled: Bool](./isindexingenabled.md)
  A Boolean value that indicates whether Core Data is currently updating the Core Spotlight index with the persistent store’s entities.
- [func indexName() -> String?](./indexname%28%29.md)
  Returns the index’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/domainidentifier())*