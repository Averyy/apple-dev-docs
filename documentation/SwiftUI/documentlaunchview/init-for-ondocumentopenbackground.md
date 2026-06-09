# init(_:for:_:onDocumentOpen:background:)

**Framework**: SwiftUI  
**Kind**: init

Creates a view to present when launching document-related user experiences using a localized title, custom actions, and a background view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
nonisolated
init(_ title: LocalizedStringKey, for contentTypes: [UTType], @ContentBuilder _ actions: () -> Actions, @ContentBuilder onDocumentOpen: @escaping (URL) -> DocumentView, @ContentBuilder background: () -> some View)
```

#### Discussion

> **Note**:  An alternative to `DocumentLaunchView` is a scene variant of this API: [`DocumentGroupLaunchScene`](documentgrouplaunchscene.md). If the app definition contains `DocumentGroup` scenes, consider using a `DocumentGroupLaunchScene` instead of this view.

## Parameters

- `title`: A title key to use for the view title.
- `contentTypes`: Content types that the view can open.
- `actions`: A content builder returning the view’s actions
- `onDocumentOpen`: A closure that handles an open file.
- `background`: A background of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentlaunchview/init(_:for:_:ondocumentopen:background:))*