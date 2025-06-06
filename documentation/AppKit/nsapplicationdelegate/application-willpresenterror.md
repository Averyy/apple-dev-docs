# application(_:willPresentError:)

**Framework**: AppKit  
**Kind**: method

Returns an error for the app to display to the user.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func application(_ application: NSApplication, willPresentError error: any Error) -> any Error
```

#### Return Value

The error object to display.

#### Discussion

You can implement this delegate method to customize the presentation of any error presented by your application, as long as no code in your application overrides either of the `NSResponder` methods `presentError:modalForWindow:delegate:didPresentSelector:contextInfo:` or `presentError:` in a way that prevents errors from being passed down the responder chain to the application object.

Your implementation of this delegate method can examine `error` and, if its localized description or recovery information is unhelpfully generic, return an error object with specific localized text that is more suitable for presentation in alert sheets and dialogs. If you do this, always use the domain and error code of the `NSError` object to distinguish between errors whose presentation you want to customize and those you do not. Don’t make decisions based on the localized description, recovery suggestion, or recovery options because parsing localized text is problematic. If you decide not to customize the error presentation, just return the passed-in error object.

## Parameters

- `application`: The application object associated with the delegate.
- `error`: The error object that is used to construct the error message. Your implementation of this method can return a new   object or the same one in this parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:willpresenterror:))*