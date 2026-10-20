# searchTemplate(_:selectedResult:completionHandler:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that the user selected an item from the search result.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func searchTemplate(_ searchTemplate: CPSearchTemplate, selectedResult item: CPListItem, completionHandler: @escaping () -> Void)
```

```swift
func searchTemplate(_ searchTemplate: CPSearchTemplate, selectedResult item: CPListItem) async
```

```objc
- (void) searchTemplate:(CPSearchTemplate *) searchTemplate selectedResult:(CPListItem *) item completionHandler:(void (^)()) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func searchTemplate(_ searchTemplate: CPSearchTemplate, selectedResult item: CPListItem) async
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

Your implementation must call the completion handler after processing the selected result item.

## Parameters

- `searchTemplate`: The current search template.
- `item`: The search result item selected by the user.
- `completionHandler`: The block that you must call after processing the selected result item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsearchtemplatedelegate/searchtemplate(_:selectedresult:completionhandler:))*