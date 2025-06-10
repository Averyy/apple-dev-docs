# init(_:for:_:onDocumentOpen:backgroundAccessoryView:overlayAccessoryView:)

**Framework**: SwiftUI  
**Kind**: init

Creates a view to present when launching document-related user experiences using a localized title, custom actions, and accessory views.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
init(_ title: LocalizedStringKey, for contentTypes: [UTType], @ViewBuilder _ actions: () -> Actions, @ViewBuilder onDocumentOpen: @escaping (URL) -> DocumentView, @ViewBuilder backgroundAccessoryView: @escaping (DocumentLaunchGeometryProxy) -> some View, @ViewBuilder overlayAccessoryView: @escaping (DocumentLaunchGeometryProxy) -> some View)
```

#### Discussion

> **Note**:  An alternative to `DocumentLaunchView` is a scene variant of this API: [`DocumentGroupLaunchScene`](documentgrouplaunchscene.md). If the app definition contains `DocumentGroup` scenes, consider using a `DocumentGroupLaunchScene` instead of this view.

## Parameters

- `title`: A title key to use for the view title.
- `contentTypes`: Content types that the view can open.
- `actions`: A view builder returning the view’s actions
- `onDocumentOpen`: A closure that handles an open file.
- `backgroundAccessoryView`: A view builder for returning the view’s   background accessory view.
- `overlayAccessoryView`: A view builder for returning the view’s overlay   accessory view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentlaunchview/init(_:for:_:ondocumentopen:backgroundaccessoryview:overlayaccessoryview:))*