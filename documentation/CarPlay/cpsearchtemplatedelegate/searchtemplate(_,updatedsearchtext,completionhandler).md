# searchTemplate(_:updatedSearchText:completionHandler:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that the user updated the search criteria text.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func searchTemplate(_ searchTemplate: CPSearchTemplate, updatedSearchText searchText: String, completionHandler: @escaping ([CPListItem]) -> Void)
```

```swift
func searchTemplate(_ searchTemplate: CPSearchTemplate, updatedSearchText searchText: String) async -> [CPListItem]
```

```objc
- (void) searchTemplate:(CPSearchTemplate *) searchTemplate updatedSearchText:(NSString *) searchText completionHandler:(void (^)(NSArray<CPListItem *> *searchResults)) completionHandler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func searchTemplate(_ searchTemplate: CPSearchTemplate, updatedSearchText searchText: String) async -> [CPListItem]
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

After the method retrieves the search result, the method must call `completionHandler` for the system to display the result to the user.

## Parameters

- `searchTemplate`: The current search template.
- `searchText`: The search criteria text entered by the user.
- `completionHandler`: The block your implementation calls after retrieving the search result.

  - **searchResults**: An array of [`CPListItem`](../cplistitem.md) objects—one list item for each search result item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsearchtemplatedelegate/searchtemplate(_:updatedsearchtext:completionhandler:))*