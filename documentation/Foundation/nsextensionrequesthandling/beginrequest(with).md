# beginRequest(with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the extension to prepare for a host app’s request.

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
func beginRequest(with context: NSExtensionContext)
```

```objc
- (void) beginRequestWithExtensionContext:(NSExtensionContext *) context;
```

## Discussion

An extension prepares for a host app’s request by getting the context passed in this method and requesting related data items, if appropriate. This method is received after the extension is initialized, but before the principal object is asked to do anything with the context. For example, if the principal object is a view controller, it receives this message before [`loadView()`](../../UIKit/uiviewcontroller/loadview%28%29.md) is called. After an extension receives this message, the [`extensionContext`](../../UIKit/uiviewcontroller/extensioncontext.md) property of the view controller returns a non`nil` value.

If your subclass conforms to this protocol and overrides `beginRequestWithExtensionContext:`, the subclass is expected to call `[super beginRequestWithExtensionContext:]`.

## Parameters

- `context`: An [`NSExtensionContext`](../nsextensioncontext.md) object that represents the context in which the host app makes the request. Typically, the context contains data that the extension can work on.

## See Also

### Related Documentation
- [App Extension Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensionrequesthandling/beginrequest(with:))*