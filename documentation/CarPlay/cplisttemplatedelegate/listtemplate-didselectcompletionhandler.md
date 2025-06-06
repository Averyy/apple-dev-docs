# listTemplate(_:didSelect:completionHandler:)

**Framework**: CarPlay  
**Kind**: method  
**Required**: Yes

Tells the delegate when the user selects a list item.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func listTemplate(_ listTemplate: CPListTemplate, didSelect item: CPListItem) async
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func listTemplate(_ listTemplate: CPListTemplate, didSelect item: CPListItem) async
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func listTemplate(_ listTemplate: CPListTemplate, didSelect item: CPListItem) async
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

When implementing this method, perform any necessary operations to prepare for completing the item selection, including updating your user interface. You must call `completionHandler` after handling the selected item to tell the system that it can continue. The list template displays an activity indicator—after a short delay—while it waits for your implementation to call the completion handler.

## Parameters

- `listTemplate`: The list template that contains the selected item.
- `item`: The item that the user selects.
- `completionHandler`: The block that your app must call after handling the selected item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplatedelegate/listtemplate(_:didselect:completionhandler:))*