# init(path:root:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a navigation stack with homogeneous navigation state that you can control.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
init(path: Binding<Data>, @ContentBuilder root: () -> Root) where Data : MutableCollection, Data : RandomAccessCollection, Data : RangeReplaceableCollection, Data.Element : Hashable
```

**Other overloads**:

```swift
nonisolated
init(path: Binding<NavigationPath>, @ContentBuilder root: () -> Root) where Data == NavigationPath
```

## Mentions

- [Understanding the navigation stack](../understanding-the-navigation-stack.md)
- [Migrating to new navigation types](../migrating-to-new-navigation-types.md)

#### Discussion

If you don’t need access to the navigation state, use [`init(root:)`](./init%28root%29.md).

## Parameters

- `path`: A [`Binding`](../binding.md) to the navigation state for this stack.
- `root`: The view to display when the stack is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationstack/init(path:root:))*