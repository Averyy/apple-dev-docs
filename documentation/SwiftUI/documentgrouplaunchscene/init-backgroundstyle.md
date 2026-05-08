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
nonisolated
init<B>(_ title: LocalizedStringKey, backgroundStyle: B = BackgroundStyle(), @ViewBuilder _ actions: () -> Actions = { DefaultDocumentGroupLaunchActions() }) where B : ShapeStyle
```

#### Discussion

Use a `DocumentGroupLaunchScene` alongside any [`DocumentGroup`](documentgroup.md) scenes. If you don’t implement a `DocumentGroup` in the app declaration, you can get the same design by implementing a [`DocumentLaunchView`](documentlaunchview.md).

## Parameters

- `title`: A key to use for the view title.
- `backgroundStyle`: A background style of the view.
- `actions`: A view builder for returning the view’s actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgrouplaunchscene/init(_:backgroundstyle:_:))*