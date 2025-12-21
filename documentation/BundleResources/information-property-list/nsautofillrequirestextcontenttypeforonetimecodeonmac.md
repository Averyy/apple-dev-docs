# NSAutoFillRequiresTextContentTypeForOneTimeCodeOnMac

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether text fields receive AutoFill of one-time codes only if they adopt the suitable content type.

**Availability**:
- macOS 26.0+

#### Discussion

In macOS 26 and later, all macOS apps that support typing text also enable Security Code AutoFill of delivered codes. These are the one-time codes received by Messages or Mail as part of an authentication flow.

AutoFill is available when all of the following are true:

- Messages or Mail detects a one-time code.
- A text-input experience is active, such as a text field having focus.
- Fewer than three minutes elapses since detection of the code.

In this case, an AutoFill menu can appear next to the text-insertion cursor. The person using the app can accept the proposed fill to enter it into the text field. They can also mark the message as read or press the ESC key while the AutoFill menu is visible, which prevents the code from appearing again.

If an app rarely or never uses one-time codes, and doesn’t need to show the AutoFill menu in most or all scenarios, it can use `NSAutoFillRequiresTextContentTypeForOneTimeCodeOnMac`. With this property set to `true`:

- The system doesn’t show the AutoFill menu for one-time codes in most text fields.
- The app can still support the AutoFill behavior for specific fields by annotating them with the one-time code text content type. In AppKit, set the field’s [`contentType`](https://developer.apple.com/documentation/AppKit/NSTextContent/contentType) to [`oneTimeCode`](https://developer.apple.com/documentation/AppKit/NSTextContentType/oneTimeCode). For a SwiftUI app, use the view modifier [`textContentType(_:)`](https://developer.apple.com/documentation/SwiftUI/View/textContentType(_:)-ufdv) to set the content type to [`oneTimeCode`](https://developer.apple.com/documentation/UIKit/UITextContentType/oneTimeCode). Otherwise, without these annotations, the app never shows AutoFill for detected one-time codes.

macOS doesn’t perform Security Code AutoFill for a small number of apps because of compatibility. To receive AutoFill of delivered codes in all text fields, set `NSAutoFillRequiresTextContentTypeForOneTimeCodeOnMac` to `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsautofillrequirestextcontenttypeforonetimecodeonmac)*