# init(_:backgroundStyle:_:backgroundAccessoryView:overlayAccessoryView:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a launch scene for document-based applications with a title, a background style, a set of actions, and background and overlay accessory views.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
init<B>(_ title: Text? = nil, backgroundStyle: B = BackgroundStyle(), @ContentBuilder _ actions: () -> Actions = { DefaultDocumentGroupLaunchActions() }, @ContentBuilder backgroundAccessoryView: @escaping (DocumentLaunchGeometryProxy) -> some View, @ContentBuilder overlayAccessoryView: @escaping (DocumentLaunchGeometryProxy) -> some View) where B : ShapeStyle
```

Available when `Actions` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init<B>(_ title: LocalizedStringResource, backgroundStyle: B = BackgroundStyle(), @ContentBuilder _ actions: () -> Actions = { DefaultDocumentGroupLaunchActions() }, @ContentBuilder backgroundAccessoryView: @escaping (DocumentLaunchGeometryProxy) -> some View, @ContentBuilder overlayAccessoryView: @escaping (DocumentLaunchGeometryProxy) -> some View) where B : ShapeStyle
```

```swift
nonisolated
init<B>(_ title: LocalizedStringKey, backgroundStyle: B = BackgroundStyle(), @ContentBuilder _ actions: () -> Actions = { DefaultDocumentGroupLaunchActions() }, @ContentBuilder backgroundAccessoryView: @escaping (DocumentLaunchGeometryProxy) -> some View, @ContentBuilder overlayAccessoryView: @escaping (DocumentLaunchGeometryProxy) -> some View) where B : ShapeStyle
```

```swift
nonisolated
init<B>(_ title: some StringProtocol, backgroundStyle: B = BackgroundStyle(), @ContentBuilder _ actions: () -> Actions = { DefaultDocumentGroupLaunchActions() }, @ContentBuilder backgroundAccessoryView: @escaping (DocumentLaunchGeometryProxy) -> some View, @ContentBuilder overlayAccessoryView: @escaping (DocumentLaunchGeometryProxy) -> some View) where B : ShapeStyle
```

## Discussion

Use a `DocumentGroupLaunchScene` alongside any [`DocumentGroup`](../documentgroup.md) scenes. If you don’t implement a `DocumentGroup` in the app declaration, you can get the same design by implementing a [`DocumentLaunchView`](../documentlaunchview.md).

## Parameters

- `title`: A text value to use for the title.
- `backgroundStyle`: A background style of the view.
- `actions`: A content builder for returning the view’s actions.
- `backgroundAccessoryView`: A content builder for returning the view’s background accessory view.
- `overlayAccessoryView`: A content builder for returning the view’s overlay accessory view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgrouplaunchscene/init(_:backgroundstyle:_:backgroundaccessoryview:overlayaccessoryview:)-2d13c)*