# NSExtensionItemsAndErrorsKey

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

The extension items and errors key.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSExtensionItemsAndErrorsKey: String
```

```c
extern NSString * const NSExtensionItemsAndErrorsKey;
```

#### Discussion

This key appears in the [`userInfo`](./nserror/userinfo.md) dictionary of the [`NSError`](./nserror.md) object that [`cancelRequest(withError:)`](./nsextensioncontext/cancelrequest%28witherror%29.md) returns.

This key’s value is a dictionary of [`NSExtensionItem`](./nsextensionitem.md) objects and associated [`NSError`](./nserror.md) instances.

## See Also

### Handling requests
- [func completeRequest(returningItems: [Any]?, completionHandler: ((Bool) -> Void)?)](./nsextensioncontext/completerequest%28returningitems,completionhandler%29.md)
  Tells the host app to complete the app extension request with an array of result items.
- [func cancelRequest(withError: any Error)](./nsextensioncontext/cancelrequest%28witherror%29.md)
  Tells the host app to cancel the app extension request, with a supplied error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensionitemsanderrorskey)*