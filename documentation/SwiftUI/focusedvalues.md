# FocusedValues

**Framework**: SwiftUI  
**Kind**: struct

A collection of state exported by the focused scene or view and its ancestors.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
struct FocusedValues
```

#### Creating Custom Focused Values

Use the `Entry` macro to create custom focused values by extending `FocusedValues` with new properties:

```swift
extension FocusedValues {
    @Entry var focusedDocument: Binding<MyDocument>?
}
```

The `Entry` macro automatically generates the underlying key type and provides the getter and setter for the focused value. Since the default value for focused values is always `nil`, all focused values must be optional.

##### Publishing Values in Your Views

Views publish focused values using the [`focusedValue(_:_:)`](view/focusedvalue(_:_:).md) modifier:

```swift
struct DocumentCellView: View {
    @Binding var document: MyDocument

    var body: some View {
        Text("Document Content")
            .focusedValue(\.focusedDocument, $document)
    }
}
```

For scene-wide values that should be available depending on the focused scene, use [`focusedSceneValue(_:_:)`](view/focusedscenevalue(_:_:).md):

```swift
struct DocumentViewer: View {
    @Binding var document: MyDocument

    var body: some View {
        Text("Document Content")
            .focusedSceneValue(\.focusedDocument, $document)
    }
}
```

##### Accessing the Current Focused Value

Use the [`FocusedValue`](focusedvalue.md) property wrapper in your [`App`](app.md) or [`View`](view.md) to read the current value in the `body`. The [`FocusedBinding`](focusedbinding.md) can be used as a convenient way to access the `wrappedValue` if the value type of the focused value is a `Binding`:

```swift
@main
struct DocumentApp: App {
    @FocusedBinding(\.focusedDocument) var currentDocument: MyDocument?

    var body: some Scene {
        DocumentGroup(newDocument: MyDocument()) { file in
            ContentView(document: file.$document)
                .focusedValue(\.focusedDocument, file.$document)
        }
        .commands {
            CommandGroup(after: .undoRedo) {
                Button("Increment") {
                    currentDocument?.value += 1
                }.disabled(currentDocument == nil)
            }
        }
    }
}
```

## Topics

### Getting the value for a key
- [subscript<Key>(Key.Type) -> Key.Value?](focusedvalues/subscript(_:).md)
  Reads and writes values associated with a given focused value key.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [func focusedValue<T>(T?) -> some View](view/focusedvalue(_:).md)
  Sets the focused value for the given object type.
- [func focusedValue(_:_:)](view/focusedvalue(_:_:).md)
  Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused view hierarchy.
- [func focusedSceneValue<T>(T?) -> some View](view/focusedscenevalue(_:).md)
  Sets the focused value for the given object type at a scene-wide scope.
- [func focusedSceneValue(_:_:)](view/focusedscenevalue(_:_:).md)
  Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/focusedvalues)*