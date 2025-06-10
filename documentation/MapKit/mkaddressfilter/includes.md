# includes(_:)

**Framework**: MapKit  
**Kind**: method

Indicates whether options are included for filtering.

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
func includes(_ options: MKAddressFilter.Options) -> Bool
```

#### Return Value

Returns `true` if the passed options are included in the filtering options; otherwise, `false`.

#### Discussion

A filter includes or excludes a set of filter options. Use this method to query the filter instance for one or more options.

```swift
let filter = MKAddressFilter(including: [.locality,  .subLocality])
let result = filter.includes(.locality)
```

The method returns `true` because `filter` includes [`Locality`](https://developer.apple.com/documentation/MapKitJS/mapkit.AddressCategory/Locality).

## Parameters

- `options`: The filters to check for inclusion.

## See Also

- [MKAddressFilter.Options](mkaddressfilter/options.md)
  A structure that contains options for filtering results in a search.
- [class var excludingAll: MKAddressFilter](mkaddressfilter/excludingall.md)
  A list of categories to exclude from a search.
- [class var includingAll: MKAddressFilter](mkaddressfilter/includingall.md)
  A list of categories to include in a search.
- [func excludes(MKAddressFilter.Options) -> Bool](mkaddressfilter/excludes(_:).md)
  Indicates whether options are excluded from filtering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkaddressfilter/includes(_:))*