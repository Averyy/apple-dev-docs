# searchTerritory

**Framework**: MarketplaceKit  
**Kind**: property

A country code that iOS uses to filter the search results of apps that aren’t available in that country.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
nonisolated
final var searchTerritory: String? { get async }
```

#### Discussion

This property is an optional two-letter country code in the ISO 3166-1 alpha-2 standard that the alternative marketplace sets. For more information, see [`setSearchTerritory(_:)`](applibrary/setsearchterritory(_:).md).

## See Also

- [func setSearchTerritory(String?) async](applibrary/setsearchterritory(_:).md)
  Defines a country code that iOS uses to filter the search results of apps that aren’t available in that country.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/searchterritory)*