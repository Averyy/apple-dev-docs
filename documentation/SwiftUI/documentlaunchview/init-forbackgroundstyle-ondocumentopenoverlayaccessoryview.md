# init(_:for:backgroundStyle:_:onDocumentOpen:overlayAccessoryView:)

**Framework**: SwiftUI  
**Kind**: init

Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background style, and an overlay accessory view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
init<B>(_ title: LocalizedStringKey, for contentTypes: [UTType], backgroundStyle: B, @ViewBuilder _ actions: () -> Actions, @ViewBuilder onDocumentOpen: @escaping (URL) -> DocumentView, @ViewBuilder overlayAccessoryView: @escaping (DocumentLaunchGeometryProxy) -> some View) where B : ShapeStyle
```

#### Discussion

> **Note**:  An alternative to `DocumentLaunchView` is a scene variant of this API: [`DocumentGroupLaunchScene`](documentgrouplaunchscene.md). If the app definition contains `DocumentGroup` scenes, consider using a `DocumentGroupLaunchScene` instead of this view.

 An alternative to `DocumentLaunchView` is a scene variant of this API: [`DocumentGroupLaunchScene`](documentgrouplaunchscene.md). If the app definition contains `DocumentGroup` scenes, consider using a `DocumentGroupLaunchScene` instead of this view.

## Parameters

- `title`: A title key to use for the view title.
- `contentTypes`: Content types that the view can open.
- `backgroundStyle`: An optional background style of the view.
- `actions`: A view builder returning the view’s actions
- `onDocumentOpen`: A closure that handles an open file.
- `overlayAccessoryView`: A view builder for returning the view’s overlay   accessory view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentlaunchview/init(_:for:backgroundstyle:_:ondocumentopen:overlayaccessoryview:))*