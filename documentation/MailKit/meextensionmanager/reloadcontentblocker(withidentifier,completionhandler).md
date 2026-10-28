# reloadContentBlocker(withIdentifier:completionHandler:)

**Framework**: MailKit  
**Kind**: method  
**Role**: Type Method

**Availability**:
- macOS 12.0+

## Declaration

```swift
class func reloadContentBlocker(withIdentifier identifier: String, completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
class func reloadContentBlocker(withIdentifier identifier: String) async throws
```

```objc
+ (void) reloadContentBlockerWithIdentifier:(NSString *) identifier completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> class func reloadContentBlocker(withIdentifier identifier: String) async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## See Also

### Type Methods
- [class func reloadVisibleMessages(completionHandler: (((any Error)?) -> Void)?)](./reloadvisiblemessages%28completionhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meextensionmanager/reloadcontentblocker(withidentifier:completionhandler:))*