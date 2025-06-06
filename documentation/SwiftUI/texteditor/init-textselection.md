# init(text:selection:)

**Framework**: SwiftUI  
**Kind**: init

Creates a plain text editor that captures the current selection.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init(text: Binding<String>, selection: Binding<TextSelection?>)
```

#### Discussion

Use this initializer to create a view in which users can enter and edit long-form text and access the current selection.

In this example, the text editor renders gray text using the 13 point Helvetica Neue font with 5 points of spacing between each line:

```swift
struct TextEditingView: View {
    @State private var fullText: String = "This is some editable text..."
    @State var selection: TextSelection? = nil

    var body: some View {
        TextEditor(text: $fullText, selection: $selection)
            .foregroundColor(Color.gray)
            .font(.custom("HelveticaNeue", size: 13))
            .lineSpacing(5)
    }
}
```

## Parameters

- `text`: A   to the variable containing the text to edit.
- `selection`: A   to the variable containing the selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/texteditor/init(text:selection:))*