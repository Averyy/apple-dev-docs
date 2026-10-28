# primaryActionClicked(forMessageContext:completionHandler:)

**Framework**: MailKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- macOS 12.0+

## Declaration

```swift
func primaryActionClicked(forMessageContext context: Data, completionHandler: @escaping (MEExtensionViewController?) -> Void)
```

```swift
func primaryActionClicked(forMessageContext context: Data) async -> MEExtensionViewController?
```

```objc
- (void) primaryActionClickedForMessageContext:(NSData *) context completionHandler:(void (^)(MEExtensionViewController *result)) completionHandler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func primaryActionClicked(forMessageContext context: Data) async -> MEExtensionViewController?
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## See Also

### Instance Methods
- [func extensionViewController(messageContext: Data) -> MEExtensionViewController?](./extensionviewcontroller%28messagecontext%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessagesecurityhandler/primaryactionclicked(formessagecontext:completionhandler:))*