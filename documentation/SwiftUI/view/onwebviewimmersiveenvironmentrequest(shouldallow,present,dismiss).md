# onWebViewImmersiveEnvironmentRequest(shouldAllow:present:dismiss:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Manages the lifecycle of immersive environments requested by websites.

**Availability**:
- visionOS 27.0+

## Declaration

```swift
nonisolated
func onWebViewImmersiveEnvironmentRequest(shouldAllow: @escaping @MainActor @Sendable (WebPage.FrameInfo) async -> Bool, present: @escaping @MainActor @Sendable (WebPage.ImmersiveEnvironment) async throws -> Void, dismiss: @escaping @MainActor @Sendable (WebPage.ImmersiveEnvironment) async -> Void) -> some View
```

#### Return Value

A modified view that manages immersive environment lifecycle.

#### Discussion

Use this modifier to control authorization, presentation, and dismissal of immersive environments from websites.

## Parameters

- `shouldAllow`: An async closure called when a website requests an immersive environment. This can be used to request user consent or apply custom authorization logic. It receives the source `WebPage.FrameInfo` and should return `true` to allow the environment presentation, or `false` to deny it.
- `present`: An async throwing closure called after the environment has loaded and is ready for presentation. It receives the `WebPage.ImmersiveEnvironment`. Use this to open an Immersive Space containing a `WebViewImmersiveEnvironmentView` initialized with this environment. If another immersive space is already being presented, dismiss it first. This closure should return after the presentation transition completes.
- `dismiss`: An async closure called when the website or the application asks to dismiss the immersive environment. It receives the `WebPage.ImmersiveEnvironment` to dismiss. This closure should return after the dismissal transition completes.

## See Also

### Displaying web content
- [struct WebView](../../WebKit/webview-swift.struct.md)
  A view that displays some web content.
- [class WebPage](../../WebKit/webpage.md)
  An object that controls and manages the behavior of interactive web content.
- [func webViewBackForwardNavigationGestures(WebView.BackForwardNavigationGesturesBehavior) -> some View](./webviewbackforwardnavigationgestures%28_%29.md)
  Determines whether horizontal swipe gestures trigger backward and forward page navigation.
- [func webViewContentBackground(Visibility) -> some View](./webviewcontentbackground%28_%29.md)
  Specifies the visibility of the webpage’s natural background color within this view.
- [func webViewContextMenu(menu: (WebView.ActivatedElementInfo) -> some View) -> some View](./webviewcontextmenu%28menu%29.md)
  Adds an item-based context menu to a WebView, replacing the default set of context menu items.
- [func webViewElementFullscreenBehavior(WebView.ElementFullscreenBehavior) -> some View](./webviewelementfullscreenbehavior%28_%29.md)
  Determines whether a web view can display content full screen.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onwebviewimmersiveenvironmentrequest(shouldallow:present:dismiss:))*