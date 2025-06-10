# searchTemplate(_:updatedSearchText:completionHandler:)

**Framework**: CarPlay  
**Kind**: method  
**Required**: Yes

Tells the delegate that the user updated the search criteria text.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func searchTemplate(_ searchTemplate: CPSearchTemplate, updatedSearchText searchText: String) async -> [CPListItem]
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func searchTemplate(_ searchTemplate: CPSearchTemplate, updatedSearchText searchText: String) async -> [CPListItem]
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

After the method retrieves the search result, the method must call `completionHandler` for the system to display the result to the user.

## Parameters

- `searchTemplate`: The current search template.
- `searchText`: The search criteria text entered by the user.
- `completionHandler`: The block your implementation calls after retrieving the search result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsearchtemplatedelegate/searchtemplate(_:updatedsearchtext:completionhandler:))*