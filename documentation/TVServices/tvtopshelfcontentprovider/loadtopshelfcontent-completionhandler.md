# loadTopShelfContent(completionHandler:)

**Framework**: TV Services  
**Kind**: method

Provides the content you want to display in the top shelf for your app.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
func loadTopShelfContent() async -> (any TVTopShelfContent)?
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func loadTopShelfContent() async -> (any TVTopShelfContent)?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func loadTopShelfContent() async -> (any TVTopShelfContent)?
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

The system calls this method when it needs your app’s top shelf content. In your implementation, create the [`TVTopShelfItem`](tvtopshelfitem.md) objects you want to display and wrap them in a matching [`TVTopShelfContent`](tvtopshelfcontent.md) object. The specific objects you create depends on how you want to display your content. You can display items using one of the following interface styles:

- A  displays [`TVTopShelfCarouselItem`](tvtopshelfcarouselitem.md) objects in a horizontal line. The user swipes left and right to navigate from item to item.
- A  groups [`TVTopShelfSectionedItem`](tvtopshelfsectioneditem.md) objects together and presents them in a scrolling list.
- An  organizes either carousel or sectioned items and insets them by a specified amount.

If you call the completionHandler with a `nil` value, the system displays a static image provided by your app.

## Parameters

- `completionHandler`: The handler block to execute with your content. This block has no return value and takes the following parameter:


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfcontentprovider/loadtopshelfcontent(completionhandler:))*