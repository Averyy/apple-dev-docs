# reloadContentBlocker(withIdentifier:completionHandler:)

**Framework**: Safari Services  
**Kind**: method

Tells Safari to reload the specified extension’s content-blocking rules.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.4+
- macOS 10.12+
- visionOS 1.0+

## Declaration

```swift
class func reloadContentBlocker(withIdentifier identifier: String) async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
class func reloadContentBlocker(withIdentifier identifier: String) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
class func reloadContentBlocker(withIdentifier identifier: String) async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Call this method when your extension’s content-blocking rules change.

## Parameters

- `identifier`: The bundle identifier of your content blocker extension.
- `completionHandler`: The code to run after the content-blocking rules are reloaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfcontentblockermanager/reloadcontentblocker(withidentifier:completionhandler:))*