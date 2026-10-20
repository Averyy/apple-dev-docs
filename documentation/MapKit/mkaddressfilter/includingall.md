# includingAll

**Framework**: MapKit  
**Kind**: property  
**Role**: Type Property

A list of categories to include in a search.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
class var includingAll: MKAddressFilter { get }
```

```objc
@property (class, nonatomic, readonly) MKAddressFilter * filterIncludingAll;
```

## See Also

### Filtering results
- [MKAddressFilter.Options](./options.md)
  A structure that contains options for filtering results in a search.
- [class var excludingAll: MKAddressFilter](./excludingall.md)
  A list of categories to exclude from a search.
- [func excludes(MKAddressFilter.Options) -> Bool](./excludes%28_%29.md)
  Indicates whether options are excluded from filtering.
- [func includes(MKAddressFilter.Options) -> Bool](./includes%28_%29.md)
  Indicates whether options are included for filtering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkaddressfilter/includingall)*