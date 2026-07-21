# bookmarkData

**Framework**: Core AI  
**Kind**: property

Create a bookmark for this AIModel’s cached specialized asset entry as serialized data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var bookmarkData: Data { get }
```

#### Discussion

The data returned  can be stored and later resolved to re-create a model with init?(resolvingBookmark:). It contains information about the cache and entry backing the model

> **Note**: Bookmark data is just data. It does not pin entries in the cache. Only a `AIModel` will pin its associated entry in the cache while it is held.

## See Also

- [static var deviceArchitectureName: String](aimodel/devicearchitecturename.md)
  The Core AI architecture name of the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodel/bookmarkdata)*