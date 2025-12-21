# excludes(_:)

**Framework**: MapKit  
**Kind**: method

Indicates whether options are excluded from filtering.

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
func excludes(_ options: MKAddressFilter.Options) -> Bool
```

#### Return Value

Returns `true` if the passed options are excluded from the filtering options; otherwise, `false`.

#### Discussion

A filter includes or excludes a set of filter options. Use this method to query the filter instance for one or more options.

```swift
let filter = MKAddressFilter(including: [.locality,  .subLocality])
let result = filter.excludes(.postalCode)
```

The method returns `true` because `filter` doesn’t include [`PostalCode`](https://developer.apple.com/documentation/MapKitJS/AddressCategory/PostalCode).

## Parameters

- `options`: The filters to check for exclusion.

## See Also

- [MKAddressFilter.Options](mkaddressfilter/options.md)
  A structure that contains options for filtering results in a search.
- [class var excludingAll: MKAddressFilter](mkaddressfilter/excludingall.md)
  A list of categories to exclude from a search.
- [class var includingAll: MKAddressFilter](mkaddressfilter/includingall.md)
  A list of categories to include in a search.
- [func includes(MKAddressFilter.Options) -> Bool](mkaddressfilter/includes(_:).md)
  Indicates whether options are included for filtering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkaddressfilter/excludes(_:))*