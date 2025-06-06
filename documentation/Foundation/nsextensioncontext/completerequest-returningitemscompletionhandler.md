# completeRequest(returningItems:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Tells the host app to complete the app extension request with an array of result items.

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
func completeRequest(returningItems items: [Any]?, completionHandler: ((Bool) -> Void)? = nil)
```

#### Discussion

Calling this method eventually dismisses the app extension’s view controller.

## Parameters

- `items`: An array of result items, each an   object, to return to the host app.
- `completionHandler`: This parameter is   when the system prematurely terminates a   block that was previously invoked and had not otherwise expired.

## See Also

- [func cancelRequest(withError: any Error)](nsextensioncontext/cancelrequest(witherror:).md)
  Tells the host app to cancel the app extension request, with a supplied error.
- [let NSExtensionItemsAndErrorsKey: String](nsextensionitemsanderrorskey.md)
  The extension items and errors key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensioncontext/completerequest(returningitems:completionhandler:))*