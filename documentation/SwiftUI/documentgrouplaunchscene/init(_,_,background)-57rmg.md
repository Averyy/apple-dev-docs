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
nonisolated
init(_ title: LocalizedStringKey, @ContentBuilder _ actions: () -> Actions, @ContentBuilder background: () -> some View)
```

Available when `Actions` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ title: LocalizedStringResource, @ContentBuilder _ actions: () -> Actions, @ContentBuilder background: () -> some View)
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

- `title`: A key to use for the view title.
- `actions`: A content builder for returning the view’s actions.
- `background`: The background of the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgrouplaunchscene/init(_:_:background:)-57rmg)*