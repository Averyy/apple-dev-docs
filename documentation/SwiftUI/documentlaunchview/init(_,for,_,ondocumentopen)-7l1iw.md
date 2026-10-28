# init(_:for:_:onDocumentOpen:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a view to present when launching document-related user experiences using a localized title and custom actions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
nonisolated
init(_ title: LocalizedStringKey, for contentTypes: [UTType], @ContentBuilder _ actions: () -> Actions, @ContentBuilder onDocumentOpen: @escaping (URL) -> DocumentView)
```

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ title: LocalizedStringResource, for contentTypes: [UTType], @ContentBuilder _ actions: () -> Actions, @ContentBuilder onDocumentOpen: @escaping (URL) -> DocumentView)
```

```swift
nonisolated
init(_ title: Text? = nil, for contentTypes: [UTType], @ContentBuilder _ actions: () -> Actions, @ContentBuilder onDocumentOpen: @escaping (URL) -> DocumentView)
```

```swift
nonisolated
init(_ title: some StringProtocol, for contentTypes: [UTType], @ContentBuilder _ actions: () -> Actions, @ContentBuilder onDocumentOpen: @escaping (URL) -> DocumentView)
```

## Discussion

> **Note**:  An alternative to `DocumentLaunchView` is a scene variant of this API: [`DocumentGroupLaunchScene`](../documentgrouplaunchscene.md). If the app definition contains `DocumentGroup` scenes, consider using a `DocumentGroupLaunchScene` instead of this view.

## Parameters

- `title`: A title key to use for the view title.
- `contentTypes`: Content types that the view can open.
- `actions`: A content builder returning the view’s actions
- `onDocumentOpen`: A closure that handles an open file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentlaunchview/init(_:for:_:ondocumentopen:)-7l1iw)*