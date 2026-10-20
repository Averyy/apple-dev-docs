# reloadVisibleMessages(completionHandler:)

**Framework**: MailKit  
**Kind**: method  
**Role**: Type Method

**Availability**:
- macOS 12.0+

## Declaration

```swift
class func reloadVisibleMessages(completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
class func reloadVisibleMessages() async throws
```

```objc
+ (void) reloadVisibleMessagesWithCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> class func reloadVisibleMessages() async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## See Also

### Type Methods
- [class func reloadContentBlocker(withIdentifier: String, completionHandler: (((any Error)?) -> Void)?)](./reloadcontentblocker%28withidentifier,completionhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meextensionmanager/reloadvisiblemessages(completionhandler:))*