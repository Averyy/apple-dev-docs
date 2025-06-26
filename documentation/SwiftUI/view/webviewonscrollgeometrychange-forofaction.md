# webViewOnScrollGeometryChange(for:of:action:)

**Framework**: SwiftUI  
**Kind**: method

Adds an action to be performed when a value, created from a scroll geometry, changes.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
nonisolated
func webViewOnScrollGeometryChange<T>(for type: T.Type, of transform: @escaping (ScrollGeometry) -> T, action: @escaping (T, T) -> Void) -> some View where T : Hashable
```

#### Return Value

A view that invokes the action when the relevant part of a web view’s scroll geometry changes.

#### Discussion

> **Note**: The content size of web content may exceed the current size of the view’s frame, however it will never be smaller than it.

## Parameters

- `type`: The type of value transformed from a  .
- `transform`: A closure that transforms a   to your type.
- `action`: A closure to run when the transformed data changes.

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
- [func webViewScrollInputBehavior(ScrollInputBehavior, for: ScrollInputKind) -> some View](view/webviewscrollinputbehavior(_:for:).md)
  Enables or disables scrolling in web views when using particular inputs.
- [func webViewScrollPosition(Binding<ScrollPosition>) -> some View](view/webviewscrollposition(_:).md)
  Associates a binding to a scroll position with the web view.
- [func webViewTextSelection<S>(S) -> some View](view/webviewtextselection(_:).md)
  Determines whether to allow people to select or otherwise interact with text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/webviewonscrollgeometrychange(for:of:action:))*