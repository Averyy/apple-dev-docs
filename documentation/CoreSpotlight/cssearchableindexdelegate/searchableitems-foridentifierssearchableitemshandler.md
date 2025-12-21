# searchableItems(forIdentifiers:searchableItemsHandler:)

**Framework**: Core Spotlight  
**Kind**: method

Requests that the delegate provide searchable items for the provided identifiers.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
optional func searchableItems(forIdentifiers identifiers: [String], searchableItemsHandler: @escaping ([CSSearchableItem]) -> Void)
```

#### Discussion

Use this method to provide the framework with a list of identifiers to search for.

## Parameters

- `identifiers`: An array of strings that represent the identifiers.
- `searchableItemsHandler`: A method the framework calls that provides an array of   objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindexdelegate/searchableitems(foridentifiers:searchableitemshandler:))*