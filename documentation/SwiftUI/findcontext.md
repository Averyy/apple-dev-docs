# FindContext

**Framework**: SwiftUI  
**Kind**: struct

The status of the find navigator for views which support text editing.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct FindContext
```

#### Overview

Views which support text editing can use this information to implement a a find navigator that is controlled using the modifiers used for controlling the find navigator throughout the rest of SwiftUI.

For example, the following shows a minimal find navigator implementation driven by the find context which falls back to local state if no `isPresented` binding is provided:

```swift
struct FindNavigatorDrivenTextInput: View {
    @State var text: String = ""
    @State var showFindNavigator = false
    @Environment(\.findContext) var findContext
    var body: some View {
        MyTextInputView(text: $text)
            .overlay(alignment: .topTrailing) {
                if let context = findContext &&
                    context.isPresented?.wrappedValue ?? showFindNavigator
                {
                    HStack {
                        FindInputView(text: text)
                        if context.allowedOperations == .findAndReplace {
                            ReplaceInputView(text: $text)
                        }
                        Button("Close") {
                            context.isPresented?.wrappedValue = false
                            showFindNavigator = false
                        }
                    }
                } else {
                    Button("Show Find Navigator") {
                        context.isPresented?.wrappedValue = true
                        showFindNavigator = true
                    }
                }
            }
    }
}
```

## Topics

### Instance Properties
- [var isPresented: Binding<Bool>?](findcontext/ispresented.md)
  A binding controlling if the find navigator is presented, or nil if no binding has been provided via the [`findNavigator(isPresented:)`](view/findnavigator(ispresented:).md) modifier.
- [var supportsReplace: Bool](findcontext/supportsreplace.md)
  If the find navigators in this context should support replacing.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func findNavigator(isPresented: Binding<Bool>) -> some View](view/findnavigator(ispresented:).md)
  Programmatically presents the find and replace interface for text editor views.
- [func findDisabled(Bool) -> some View](view/finddisabled(_:).md)
  Prevents find and replace operations in a text editor.
- [func replaceDisabled(Bool) -> some View](view/replacedisabled(_:).md)
  Prevents replace operations in a text editor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/findcontext)*