# indexName()

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns the index’s name.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
func indexName() -> String?
```

```objc
- (NSString *) indexName;
```

## Discussion

The default value is `nil`.

## See Also

### Configuring the Index
- [var isIndexingEnabled: Bool](./isindexingenabled.md)
  A Boolean value that indicates whether Core Data is currently updating the Core Spotlight index with the persistent store’s entities.
- [func domainIdentifier() -> String](./domainidentifier%28%29.md)
  Returns the domain identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/indexname())*