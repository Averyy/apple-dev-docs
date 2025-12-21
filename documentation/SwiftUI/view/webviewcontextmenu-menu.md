# webViewContextMenu(menu:)

**Framework**: SwiftUI  
**Kind**: method

Adds an item-based context menu to a WebView, replacing the default set of context menu items.

**Availability**:
- macOS 26.0+

## Declaration

```swift
nonisolated
func webViewContextMenu(@ViewBuilder menu: @escaping @MainActor (WebView.ActivatedElementInfo) -> some View) -> some View
```

#### Return Value

A view that can display an item-based context menu.

## Parameters

- `menu`: A closure that produces the menu. The single parameter to the closure describes the type of webpage element that was acted upon.

## See Also

- [struct WebView](../WebKit/WebView-swift.struct.md)
  A view that displays some web content.
- [class WebPage](../WebKit/WebPage.md)
  An object that controls and manages the behavior of interactive web content.
- [func webViewBackForwardNavigationGestures(WebView.BackForwardNavigationGesturesBehavior) -> some View](view/webviewbackforwardnavigationgestures(_:).md)
  Determines whether horizontal swipe gestures trigger backward and forward page navigation.
- [func webViewContentBackground(Visibility) -> some View](view/webviewcontentbackground(_:).md)
  Specifies the visibility of the webpage’s natural background color within this view.
- [func webViewElementFullscreenBehavior(WebView.ElementFullscreenBehavior) -> some View](view/webviewelementfullscreenbehavior(_:).md)
  Determines whether a web view can display content full screen.
- [func webViewLinkPreviews(WebView.LinkPreviewBehavior) -> some View](view/webviewlinkpreviews(_:).md)
  Determines whether pressing a link displays a preview of the destination for the link.
- [func webViewMagnificationGestures(WebView.MagnificationGesturesBehavior) -> some View](view/webviewmagnificationgestures(_:).md)
  Determines whether magnify gestures change the view’s magnification.
- [func webViewOnScrollGeometryChange<T>(for: T.Type, of: (ScrollGeometry) -> T, action: (T, T) -> Void) -> some View](view/webviewonscrollgeometrychange(for:of:action:).md)
  Adds an action to be performed when a value, created from a scroll geometry, changes.
- [func webViewScrollInputBehavior(ScrollInputBehavior, for: ScrollInputKind) -> some View](view/webviewscrollinputbehavior(_:for:).md)
  Enables or disables scrolling in web views when using particular inputs.
- [func webViewScrollPosition(Binding<ScrollPosition>) -> some View](view/webviewscrollposition(_:).md)
  Associates a binding to a scroll position with the web view.
- [func webViewTextSelection<S>(S) -> some View](view/webviewtextselection(_:).md)
  Determines whether to allow people to select or otherwise interact with text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/webviewcontextmenu(menu:))*