# init(_:for:backgroundStyle:_:onDocumentOpen:overlayAccessoryView:)

**Framework**: SwiftUI  
**Kind**: init

Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background style, and an overlay accessory view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
nonisolated
init<B>(_ title: LocalizedStringKey, for contentTypes: [UTType], backgroundStyle: B, @ContentBuilder _ actions: () -> Actions, @ContentBuilder onDocumentOpen: @escaping (URL) -> DocumentView, @ContentBuilder overlayAccessoryView: @escaping (DocumentLaunchGeometryProxy) -> some View) where B : ShapeStyle
```

#### Discussion

> **Note**:  An alternative to `DocumentLaunchView` is a scene variant of this API: [`DocumentGroupLaunchScene`](documentgrouplaunchscene.md). If the app definition contains `DocumentGroup` scenes, consider using a `DocumentGroupLaunchScene` instead of this view.

## Parameters

- `title`: A title key to use for the view title.
- `contentTypes`: Content types that the view can open.
- `backgroundStyle`: An optional background style of the view.
- `actions`: A content builder returning the view’s actions
- `onDocumentOpen`: A closure that handles an open file.
- `overlayAccessoryView`: A content builder for returning the view’s overlay accessory view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentlaunchview/init(_:for:backgroundstyle:_:ondocumentopen:overlayaccessoryview:))*