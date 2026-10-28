# init(_:_:background:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a launch scene for document-based applications with a title, a set of actions, and a background.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ title: LocalizedStringResource, @ContentBuilder _ actions: () -> Actions, @ContentBuilder background: () -> some View)
```

Available when `Actions` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(_ title: LocalizedStringKey, @ContentBuilder _ actions: () -> Actions, @ContentBuilder background: () -> some View)
```

```swift
nonisolated
init(_ title: Text? = nil, @ContentBuilder _ actions: () -> Actions, @ContentBuilder background: () -> some View)
```

```swift
nonisolated
init(_ title: some StringProtocol, @ContentBuilder _ actions: () -> Actions, @ContentBuilder background: () -> some View)
```

## Discussion

Use a `DocumentGroupLaunchScene` alongside any [`DocumentGroup`](../documentgroup.md) scenes. If you don’t implement a `DocumentGroup` in the app declaration, you can get the same design by implementing a [`DocumentLaunchView`](../documentlaunchview.md).

## Parameters

- `title`: A resource to use for the view title.
- `actions`: A content builder for returning the view’s actions.
- `background`: The background of the scene.

## See Also

### Creating a launch scene with a background view
- [init(_:_:background:backgroundAccessoryView:)](./init%28_,_,background,backgroundaccessoryview%29.md)
  Creates a launch scene for document-based applications with a title, a set of actions, a background, and a background accessory view.
- [init(_:_:background:backgroundAccessoryView:overlayAccessoryView:)](./init%28_,_,background,backgroundaccessoryview,overlayaccessoryview%29.md)
  Creates a launch scene for document-based applications with a title, a set of actions, and a background.
- [init(_:_:background:overlayAccessoryView:)](./init%28_,_,background,overlayaccessoryview%29.md)
  Creates a launch scene for document-based applications with a title, a set of actions, a background, and an overlay accessory view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgrouplaunchscene/init(_:_:background:))*