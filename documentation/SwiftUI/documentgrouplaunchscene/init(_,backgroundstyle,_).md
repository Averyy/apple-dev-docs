# init(_:backgroundStyle:_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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

Available when `Actions` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init<B>(_ title: LocalizedStringKey, backgroundStyle: B = BackgroundStyle(), @ContentBuilder _ actions: () -> Actions = { DefaultDocumentGroupLaunchActions() }) where B : ShapeStyle
```

```swift
nonisolated
init<B>(_ title: Text? = nil, backgroundStyle: B = BackgroundStyle(), @ContentBuilder _ actions: () -> Actions = { DefaultDocumentGroupLaunchActions() }) where B : ShapeStyle
```

```swift
nonisolated
init<B>(_ title: some StringProtocol, backgroundStyle: B = BackgroundStyle(), @ContentBuilder _ actions: () -> Actions = { DefaultDocumentGroupLaunchActions() }) where B : ShapeStyle
```

## Discussion

Use a `DocumentGroupLaunchScene` alongside any [`DocumentGroup`](../documentgroup.md) scenes. If you don’t implement a `DocumentGroup` in the app declaration, you can get the same design by implementing a [`DocumentLaunchView`](../documentlaunchview.md).

## Parameters

- `title`: A resource to use for the view title.
- `backgroundStyle`: A background style of the view.
- `actions`: A content builder for returning the view’s actions.

## See Also

### Creating a launch scene with a background style
- [init(_:backgroundStyle:_:backgroundAccessoryView:)](./init%28_,backgroundstyle,_,backgroundaccessoryview%29.md)
  Creates a launch scene for document-based applications with a title, a background style, a set of actions, and a background accessory view.
- [init(_:backgroundStyle:_:backgroundAccessoryView:overlayAccessoryView:)](./init%28_,backgroundstyle,_,backgroundaccessoryview,overlayaccessoryview%29.md)
  Creates a launch scene for document-based applications with a title, a background style, a set of actions, and background and overlay accessory views.
- [init(_:backgroundStyle:_:overlayAccessoryView:)](./init%28_,backgroundstyle,_,overlayaccessoryview%29.md)
  Creates a launch scene for document-based applications with a title, a background style, a set of actions, and an overlay accessory view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgrouplaunchscene/init(_:backgroundstyle:_:))*