# init(_:backgroundStyle:_:)

**Framework**: SwiftUI  
**Kind**: init

Creates a launch scene for document-based applications with a title, a background style, and a set of actions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
@export(implementation)
nonisolated init<B>(_ title: LocalizedStringResource, backgroundStyle: B = BackgroundStyle(), @ContentBuilder _ actions: () -> Actions = { DefaultDocumentGroupLaunchActions() }) where B : ShapeStyle
```

#### Discussion

Use a `DocumentGroupLaunchScene` alongside any [`DocumentGroup`](documentgroup.md) scenes. If you don’t implement a `DocumentGroup` in the app declaration, you can get the same design by implementing a [`DocumentLaunchView`](documentlaunchview.md).

## Parameters

- `title`: A resource to use for the view title.
- `backgroundStyle`: A background style of the view.
- `actions`: A content builder for returning the view’s actions.

## See Also

- [init(_:backgroundStyle:_:backgroundAccessoryView:)](documentgrouplaunchscene/init(_:backgroundstyle:_:backgroundaccessoryview:).md)
  Creates a launch scene for document-based applications with a title, a background style, a set of actions, and a background accessory view.
- [init(_:backgroundStyle:_:backgroundAccessoryView:overlayAccessoryView:)](documentgrouplaunchscene/init(_:backgroundstyle:_:backgroundaccessoryview:overlayaccessoryview:).md)
  Creates a launch scene for document-based applications with a title, a background style, a set of actions, and background and overlay accessory views.
- [init(_:backgroundStyle:_:overlayAccessoryView:)](documentgrouplaunchscene/init(_:backgroundstyle:_:overlayaccessoryview:).md)
  Creates a launch scene for document-based applications with a title, a background style, a set of actions, and an overlay accessory view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgrouplaunchscene/init(_:backgroundstyle:_:))*