# reloadVisibleMessages(completionHandler:)

**Framework**: MailKit  
**Kind**: method

**Availability**:
- macOS 12.0+

## Declaration

```swift
class func reloadVisibleMessages() async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
class func reloadVisibleMessages() async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
class func reloadVisibleMessages() async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## See Also

- [class func reloadContentBlocker(withIdentifier: String, completionHandler: (((any Error)?) -> Void)?)](meextensionmanager/reloadcontentblocker(withidentifier:completionhandler:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meextensionmanager/reloadvisiblemessages(completionhandler:))*