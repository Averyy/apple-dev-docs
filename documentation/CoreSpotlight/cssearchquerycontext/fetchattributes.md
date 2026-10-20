# fetchAttributes

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

The attributes the system fetches for the searchable items.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var fetchAttributes: [String] { get set }
```

```objc
@property (nonatomic, strong) NSArray<NSString *> * fetchAttributes;
```

## Mentions

- [Searching for information in your app](../searching-for-information-in-your-app.md)

## See Also

### Configuring search behavior
- [var keyboardLanguage: String?](./keyboardlanguage.md)
  The language used for the query.
- [var sourceOptions: CSSearchQueryContext.SourceOptions](./sourceoptions-swift.property.md)
  The query source options to allow or deny Mail messages in the search.
- [CSSearchQueryContext.SourceOptions](./sourceoptions-swift.struct.md)
  The query source options to allow or deny Mail messages in the search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchquerycontext/fetchattributes)*