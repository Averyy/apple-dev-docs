# init(_:for:_:onDocumentOpen:backgroundAccessoryView:overlayAccessoryView:)

**Framework**: SwiftUI  
**Kind**: init

Creates a view to present when launching document-related user experiences using a localized title, custom actions, and accessory views.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ title: LocalizedStringResource, for contentTypes: [UTType], @ContentBuilder _ actions: () -> Actions, @ContentBuilder onDocumentOpen: @escaping (URL) -> DocumentView, @ContentBuilder backgroundAccessoryView: @escaping (DocumentLaunchGeometryProxy) -> some View, @ContentBuilder overlayAccessoryView: @escaping (DocumentLaunchGeometryProxy) -> some View)
```

#### Discussion

> **Note**:  An alternative to `DocumentLaunchView` is a scene variant of this API: [`DocumentGroupLaunchScene`](documentgrouplaunchscene.md). If the app definition contains `DocumentGroup` scenes, consider using a `DocumentGroupLaunchScene` instead of this view.

## Parameters

- `title`: A title resource to use for the view title.
- `contentTypes`: Content types that the view can open.
- `actions`: A content builder returning the view’s actions
- `onDocumentOpen`: A closure that handles an open file.
- `backgroundAccessoryView`: A content builder for returning the view’s background accessory view.
- `overlayAccessoryView`: A content builder for returning the view’s overlay accessory view.

## See Also

- [init(_:for:_:onDocumentOpen:)](documentlaunchview/init(_:for:_:ondocumentopen:).md)
  Creates a view to present when launching document-related user experiences using a localized title and custom actions.
- [init(_:for:_:onDocumentOpen:background:)](documentlaunchview/init(_:for:_:ondocumentopen:background:).md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, and a background view.
- [init(_:for:_:onDocumentOpen:background:backgroundAccessoryView:)](documentlaunchview/init(_:for:_:ondocumentopen:background:backgroundaccessoryview:).md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background view, and a background accessory view.
- [init(_:for:_:onDocumentOpen:background:backgroundAccessoryView:overlayAccessoryView:)](documentlaunchview/init(_:for:_:ondocumentopen:background:backgroundaccessoryview:overlayaccessoryview:).md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background view, and accessory views.
- [init(_:for:_:onDocumentOpen:background:overlayAccessoryView:)](documentlaunchview/init(_:for:_:ondocumentopen:background:overlayaccessoryview:).md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background view, and an overlay accessory view.
- [init(_:for:_:onDocumentOpen:backgroundAccessoryView:)](documentlaunchview/init(_:for:_:ondocumentopen:backgroundaccessoryview:).md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, and a background accessory view.
- [init(_:for:_:onDocumentOpen:overlayAccessoryView:)](documentlaunchview/init(_:for:_:ondocumentopen:overlayaccessoryview:).md)
  Creates a view to present when launching document-related user experiences using a localized title, custom actions, and an overlay accessory view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentlaunchview/init(_:for:_:ondocumentopen:backgroundaccessoryview:overlayaccessoryview:))*