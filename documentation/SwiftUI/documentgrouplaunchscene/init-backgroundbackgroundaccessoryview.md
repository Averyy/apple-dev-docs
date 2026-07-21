# init(_:_:background:backgroundAccessoryView:)

**Framework**: SwiftUI  
**Kind**: init

Creates a launch scene for document-based applications with a title, a set of actions, a background, and a background accessory view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ title: LocalizedStringResource, @ContentBuilder _ actions: () -> Actions, @ContentBuilder background: () -> some View, @ContentBuilder backgroundAccessoryView: @escaping (DocumentLaunchGeometryProxy) -> some View)
```

#### Discussion

Use a `DocumentGroupLaunchScene` alongside any [`DocumentGroup`](documentgroup.md) scenes. If you don’t implement a `DocumentGroup` in the app declaration, you can get the same design by implementing a [`DocumentLaunchView`](documentlaunchview.md).

## Parameters

- `title`: A resource to use for the view title.
- `actions`: A content builder for returning the view’s actions.
- `background`: The background of the scene.
- `backgroundAccessoryView`: A content builder for returning the view’s background accessory view.

## See Also

- [init(_:_:background:)](documentgrouplaunchscene/init(_:_:background:).md)
  Creates a launch scene for document-based applications with a title, a set of actions, and a background.
- [init(_:_:background:backgroundAccessoryView:overlayAccessoryView:)](documentgrouplaunchscene/init(_:_:background:backgroundaccessoryview:overlayaccessoryview:).md)
  Creates a launch scene for document-based applications with a title, a set of actions, and a background.
- [init(_:_:background:overlayAccessoryView:)](documentgrouplaunchscene/init(_:_:background:overlayaccessoryview:).md)
  Creates a launch scene for document-based applications with a title, a set of actions, a background, and an overlay accessory view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgrouplaunchscene/init(_:_:background:backgroundaccessoryview:))*