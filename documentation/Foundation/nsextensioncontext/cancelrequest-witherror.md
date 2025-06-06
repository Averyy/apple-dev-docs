# cancelRequest(withError:)

**Framework**: Foundation  
**Kind**: method

Tells the host app to cancel the app extension request, with a supplied error.

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
func cancelRequest(withError error: any Error)
```

#### Discussion

On return, the `userInfo` dictionary of the [`NSError`](nserror.md) object contains a key named [`NSExtensionItemsAndErrorsKey`](nsextensionitemsanderrorskey.md) which has as its value a dictionary of [`NSExtensionItem`](nsextensionitem.md) objects and associated [`NSError`](nserror.md) instances.

## Parameters

- `error`: The error object to return. It must be non- .

## See Also

- [App Extension Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214)
- [func completeRequest(returningItems: [Any]?, completionHandler: ((Bool) -> Void)?)](nsextensioncontext/completerequest(returningitems:completionhandler:).md)
  Tells the host app to complete the app extension request with an array of result items.
- [let NSExtensionItemsAndErrorsKey: String](nsextensionitemsanderrorskey.md)
  The extension items and errors key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensioncontext/cancelrequest(witherror:))*