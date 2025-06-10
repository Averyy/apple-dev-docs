# NavigationPath

**Framework**: SwiftUI  
**Kind**: struct

A type-erased list of data representing the content of a navigation stack.

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
struct NavigationPath
```

## Mentions

- [Understanding the navigation stack](understanding-the-composition-of-navigation-stack.md)
- [Migrating to new navigation types](migrating-to-new-navigation-types.md)

#### Overview

You can manage the state of a [`NavigationStack`](navigationstack.md) by initializing the stack with a binding to a collection of data. The stack stores data items in the collection for each view on the stack. You also can read and write the collection to observe and alter the stack’s state.

When a stack displays views that rely on only one kind of data, you can use a standard collection, like an array, to hold the data. If you need to present different kinds of data in a single stack, use a navigation path instead. The path uses type erasure so you can manage a collection of heterogeneous elements. The path also provides the usual collection controls for adding, counting, and removing data elements.

##### Serialize the Path

When the values you present on the navigation stack conform to the [`Codable`](https://developer.apple.com/documentation/Swift/Codable) protocol, you can use the path’s [`codable`](navigationpath/codable.md) property to get a serializable representation of the path. Use that representation to save and restore the contents of the stack. For example, you can define an [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject) that handles serializing and deserializing the path:

```swift
class MyModelObject: ObservableObject {
    @Published var path: NavigationPath

    static func readSerializedData() -> Data? {
        // Read data representing the path from app's persistent storage.
    }

    static func writeSerializedData(_ data: Data) {
        // Write data representing the path to app's persistent storage.
    }

    init() {
        if let data = Self.readSerializedData() {
            do {
                let representation = try JSONDecoder().decode(
                    NavigationPath.CodableRepresentation.self,
                    from: data)
                self.path = NavigationPath(representation)
            } catch {
                self.path = NavigationPath()
            }
        } else {
            self.path = NavigationPath()
        }
    }

    func save() {
        guard let representation = path.codable else { return }
        do {
            let encoder = JSONEncoder()
            let data = try encoder.encode(representation)
            Self.writeSerializedData(data)
        } catch {
            // Handle error.
        }
    }
}
```

Then, using that object in your view, you can save the state of the navigation path when the [`Scene`](scene.md) enters the [`ScenePhase.background`](scenephase/background.md) state:

```swift
@StateObject private var pathState = MyModelObject()
@Environment(\.scenePhase) private var scenePhase

var body: some View {
    NavigationStack(path: $pathState.path) {
        // Add a root view here.
    }
    .onChange(of: scenePhase) { phase in
        if phase == .background {
            pathState.save()
        }
    }
}
```

## Topics

### Creating a navigation path
- [init()](navigationpath/init.md)
  Creates a new, empty navigation path.
- [init(_:)](navigationpath/init(_:).md)
  Creates a new navigation path from a serializable version.
### Managing path contents
- [var isEmpty: Bool](navigationpath/isempty.md)
  A Boolean that indicates whether this path is empty.
- [var count: Int](navigationpath/count.md)
  The number of elements in this path.
- [func append(_:)](navigationpath/append(_:).md)
  Appends a new codable value to the end of this path.
- [func removeLast(Int)](navigationpath/removelast(_:).md)
  Removes values from the end of this path.
### Encoding a path
- [var codable: NavigationPath.CodableRepresentation?](navigationpath/codable.md)
  A value that describes the contents of this path in a serializable format.
- [NavigationPath.CodableRepresentation](navigationpath/codablerepresentation.md)
  A serializable representation of a navigation path.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct NavigationStack](navigationstack.md)
  A view that displays a root view and enables you to present additional views over the root view.
- [func navigationDestination<D, C>(for: D.Type, destination: (D) -> C) -> some View](view/navigationdestination(for:destination:).md)
  Associates a destination view with a presented data type for use within a navigation stack.
- [func navigationDestination<V>(isPresented: Binding<Bool>, destination: () -> V) -> some View](view/navigationdestination(ispresented:destination:).md)
  Associates a destination view with a binding that can be used to push the view onto a [`NavigationStack`](navigationstack.md).
- [func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D) -> C) -> some View](view/navigationdestination(item:destination:).md)
  Associates a destination view with a bound value for use within a navigation stack or navigation split view


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationpath)*