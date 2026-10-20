# init(url:)

**Framework**: OSLog  
**Kind**: init  
**Role**: Initializer

Creates a log store based on a log archive.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
convenience init(url: URL) throws
```

```objc
+ (instancetype) storeWithURL:(NSURL *) url error:(NSError **) error;
```

## See Also

### Creating Log Stores
- [class func local() throws -> Self](./local%28%29.md)
  Creates a log store representing the Mac’s local store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogstore/init(url:)-5v3w7)*