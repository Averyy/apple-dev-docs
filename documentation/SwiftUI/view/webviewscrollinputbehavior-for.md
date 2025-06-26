# webViewScrollInputBehavior(_:for:)

**Framework**: SwiftUI  
**Kind**: method

Enables or disables scrolling in web views when using particular inputs.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
nonisolated
func webViewScrollInputBehavior(_ behavior: ScrollInputBehavior, for input: ScrollInputKind) -> some View
```

#### Return Value

A view with the configured scroll input behavior for web views.

## Parameters

- `behavior`: Whether scrolling should be enabled or disabled for this input.
- `input`: The input for which to enable or disable scrolling.

## See Also

- [@MainActor @preconcurrency struct WebView](../WebKit/WebView-swift.struct.md)
  A view that displays some web content.
- [@MainActor final class WebPage](../WebKit/WebPage.md)
  An object that controls and manages the behavior of interactive web content.
- [func webViewBackForwardNavigationGestures(WebView.BackForwardNavigationGesturesBehavior) -> some View](view/webviewbackforwardnavigationgestures(_:).md)
  Determines whether horizontal swipe gestures trigger backward and forward page navigation.
- [func webViewContentBackground(Visibility) -> some View](view/webviewcontentbackground(_:).md)
  Specifies the visibility of the webpage’s natural background color within this view.
- [func webViewContextMenu(menu: (WebView.ActivatedElementInfo) -> some View) -> some View](view/webviewcontextmenu(menu:).md)
  Adds an item-based context menu to a WebView, replacing the default set of context menu items.
- [func webViewElementFullscreenBehavior(WebView.ElementFullscreenBehavior) -> some View](view/webviewelementfullscreenbehavior(_:).md)
  Determines whether a web view can display content full screen.
- [func webViewLinkPreviews(WebView.LinkPreviewBehavior) -> some View](view/webviewlinkpreviews(_:).md)
  Determines whether pressing a link displays a preview of the destination for the link.
- [func webViewMagnificationGestures(WebView.MagnificationGesturesBehavior) -> some View](view/webviewmagnificationgestures(_:).md)
  Determines whether magnify gestures change the view’s magnification.
- [func webViewOnScrollGeometryChange<T>(for: T.Type, of: (ScrollGeometry) -> T, action: (T, T) -> Void) -> some View](view/webviewonscrollgeometrychange(for:of:action:).md)
  Adds an action to be performed when a value, created from a scroll geometry, changes.
- [func webViewScrollPosition(Binding<ScrollPosition>) -> some View](view/webviewscrollposition(_:).md)
  Associates a binding to a scroll position with the web view.
- [func webViewTextSelection<S>(S) -> some View](view/webviewtextselection(_:).md)
  Determines whether to allow people to select or otherwise interact with text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/webviewscrollinputbehavior(_:for:))*