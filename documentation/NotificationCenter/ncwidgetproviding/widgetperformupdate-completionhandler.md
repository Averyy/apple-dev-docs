# widgetPerformUpdate(completionHandler:)

**Framework**: Notification Center  
**Kind**: method

Called to give a widget an opportunity to update its contents.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+

## Declaration

```swift
optional func widgetPerformUpdate() async -> NCUpdateResult
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
optional func widgetPerformUpdate() async -> NCUpdateResult
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
optional func widgetPerformUpdate() async -> NCUpdateResult
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

This method is called to give a widget an opportunity to update its contents and redraw its view prior to an operation such as a snapshot. When the widget is finished updating its contents (and redrawing, if necessary), the widget should call the completion handler block, passing the appropriate `NCUpdateResult` value.

## Parameters

- `completionHandler`: The block takes the following parameter:

## See Also

- [enum NCUpdateResult](ncupdateresult.md)
  The result of updating a widget’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/widgetperformupdate(completionhandler:))*