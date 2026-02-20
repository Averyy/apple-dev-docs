# Safari Services

**Framework**: Safari Services  
**Kind**: module

Enable web views and services in your app.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.0+
- macOS 10.12+
- visionOS 1.0+

#### Overview

Use the Safari Services framework to integrate Safari behaviors into your iOS or macOS app, or to extend the behavior of Safari.

You can:

- Provide a user interface that is almost identical to the user interface that the Safari app provides. Users can browse the web in this view and then return to your app’s content. This view is more consistent with the Safari user interface than implementing your own custom browsing solution and can be done using fewer lines of code. (iOS)
- Add items to the user’s Safari Reading List. (iOS)
- Convert your existing Chrome, Firefox, or Edge extensions into a Safari web extension, or create a new Safari web extension that can work in other browsers. (iOS and macOS)
- Determine from your app whether your content blocker extension is loaded, and if it is, tell it to refresh its contents. (iOS and macOS)
- Implement Safari app extensions. Determine from your app whether a Safari app extension is loaded. (macOS)
- Allow the user to share cookies and website data between an app and Safari for a single sign-on (SSO) experience with  [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession).

## Topics

### Safari web extensions
- [Safari web extensions](safari-web-extensions.md)
  Create web extensions that work in Safari and other browsers.
### Content blockers
- [Creating a content blocker](creating-a-content-blocker.md)
  Create a content blocker for Safari in Xcode.
- [class SFContentBlockerManager](sfcontentblockermanager.md)
  A class that your app uses to interact with a content blocker extension.
- [class SFContentBlockerState](sfcontentblockerstate.md)
  The state of a content blocker extension.
### Safari app extensions
- [Safari app extensions](safari-app-extensions.md)
  Learn how Safari app extensions extend the web-browsing experience in Safari by leveraging web technologies and native code.
- [class SFSafariExtension](sfsafariextension.md)
  A proxy for the Safari extension.
- [class SFSafariApplication](sfsafariapplication.md)
  A proxy for the Safari app.
- [class SFSafariWindow](sfsafariwindow.md)
  A proxy for a Safari window.
- [class SFSafariPage](sfsafaripage.md)
  A proxy for a Safari webpage.
- [class SFSafariTab](sfsafaritab.md)
  A proxy for a tab in a Safari window.
### Safari Settings
- [class SFSafariSettings](sfsafarisettings.md)
  A class you use to open Safari Settings from your app.
### Safari content in your app
- [class SFSafariViewController](sfsafariviewcontroller.md)
  An object that provides a visible standard interface for browsing the web.
- [SFAuthenticationSession.CompletionHandler](sfauthenticationsession/completionhandler.md)
  The completion handler for an authentication session when the user cancels or finishes the login.
- [Importing data exported from Safari](importing-data-exported-from-safari.md)
  Transfer bookmarks, saved passwords, and other information between browsers.
### Associated domains
- [Supporting associated domains](../Xcode/supporting-associated-domains.md)
  Connect your app and a website to provide both a native app and a browser experience.
- [class SFUniversalLink](sfuniversallink.md)
  An object that provides browsers with the ability to discover associations between an app and a website.
- [Associated Domains Entitlement](../BundleResources/Entitlements/com.apple.developer.associated-domains.md)
  The associated domains for specific services, such as shared web credentials, universal links, and App Clips.
### Availability
- [func SFSafariServicesAvailable(SFSafariServicesVersion) -> Bool](sfsafariservicesavailable(_:).md)
  Indicates whether a given version of Safari services is available.
- [enum SFSafariServicesVersion](sfsafariservicesversion.md)
  The version of Safari services.
### Safari Reading List
- [class SSReadingList](ssreadinglist.md)
  An object for adding items to a user’s Safari Reading List.
- [let SSReadingListErrorDomain: String](ssreadinglisterrordomain.md)
  The domain for Safari Reading List errors.
- [SSReadingListError.Code](ssreadinglisterror/code.md)
  Messages that describe a Safari Reading List error.
- [struct SSReadingListError](ssreadinglisterror.md)
  A Safari Reading List error.
### Home Screen bookmarks
- [protocol SFAddToHomeScreenActivityItem](sfaddtohomescreenactivityitem.md)
  A protocol that describes a bookmark someone can add to their Home Screen.
### Miscellaneous errors
- [struct SFError](sferror.md)
  A content blocker or Safari app extension error.
- [SFError.Code](sferror/code.md)
  Messages that describe a content blocker or Safari app extension error.
- [let SFErrorDomain: String](sferrordomain.md)
  The domain for content blocker or Safari app extension errors.
### Deprecated
- [Deprecated symbols](deprecated-symbols.md)
  Review unsupported symbols and their replacements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SafariServices)*