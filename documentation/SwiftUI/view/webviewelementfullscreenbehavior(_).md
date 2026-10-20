# webViewElementFullscreenBehavior(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Determines whether a web view can display content full screen.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
func webViewElementFullscreenBehavior(_ value: WebView.ElementFullscreenBehavior) -> some View
```

## See Also

### Displaying web content
- [struct WebView](../../WebKit/webview-swift.struct.md)
  A view that displays some web content.
- [class WebPage](../../WebKit/webpage.md)
  An object that controls and manages the behavior of interactive web content.
- [func onWebViewImmersiveEnvironmentRequest(shouldAllow: (WebPage.FrameInfo) async -> Bool, present: (WebPage.ImmersiveEnvironment) async throws -> Void, dismiss: (WebPage.ImmersiveEnvironment) async -> Void) -> some View](./onwebviewimmersiveenvironmentrequest%28shouldallow,present,dismiss%29.md)
  Manages the lifecycle of immersive environments requested by websites.
- [func webViewBackForwardNavigationGestures(WebView.BackForwardNavigationGesturesBehavior) -> some View](./webviewbackforwardnavigationgestures%28_%29.md)
  Determines whether horizontal swipe gestures trigger backward and forward page navigation.
- [func webViewContentBackground(Visibility) -> some View](./webviewcontentbackground%28_%29.md)
  Specifies the visibility of the webpage’s natural background color within this view.
- [func webViewContextMenu(menu: (WebView.ActivatedElementInfo) -> some View) -> some View](./webviewcontextmenu%28menu%29.md)
  Adds an item-based context menu to a WebView, replacing the default set of context menu items.
- [func webViewLinkPreviews(WebView.LinkPreviewBehavior) -> some View](./webviewlinkpreviews%28_%29.md)
  Determines whether pressing a link displays a preview of the destination for the link.
- [func webViewMagnificationGestures(WebView.MagnificationGesturesBehavior) -> some View](./webviewmagnificationgestures%28_%29.md)
  Determines whether magnify gestures change the view’s magnification.
- [func webViewOnScrollGeometryChange<T>(for: T.Type, of: (ScrollGeometry) -> T, action: (T, T) -> Void) -> some View](./webviewonscrollgeometrychange%28for,of,action%29.md)
  Adds an action to be performed when a value, created from a scroll geometry, changes.
- [func webViewScrollInputBehavior(ScrollInputBehavior, for: ScrollInputKind) -> some View](./webviewscrollinputbehavior%28_,for%29.md)
  Enables or disables scrolling in web views when using particular inputs.
- [func webViewScrollPosition(Binding<ScrollPosition>) -> some View](./webviewscrollposition%28_%29.md)
  Associates a binding to a scroll position with the web view.
- [func webViewTextSelection<S>(S) -> some View](./webviewtextselection%28_%29.md)
  Determines whether to allow people to select or otherwise interact with text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/webviewelementfullscreenbehavior(_:))*