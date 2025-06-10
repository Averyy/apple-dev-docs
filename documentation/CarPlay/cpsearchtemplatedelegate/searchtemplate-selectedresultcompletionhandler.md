# searchTemplate(_:selectedResult:completionHandler:)

**Framework**: CarPlay  
**Kind**: method  
**Required**: Yes

Tells the delegate that the user selected an item from the search result.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func searchTemplate(_ searchTemplate: CPSearchTemplate, selectedResult item: CPListItem) async
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func searchTemplate(_ searchTemplate: CPSearchTemplate, selectedResult item: CPListItem) async
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Your implementation must call the completion handler after processing the selected result item.

## Parameters

- `searchTemplate`: The current search template.
- `item`: The search result item selected by the user.
- `completionHandler`: The block that you must call after processing the selected result item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsearchtemplatedelegate/searchtemplate(_:selectedresult:completionhandler:))*