# callAsFunction(contentType:prepareDocument:)

**Framework**: SwiftUI  
**Kind**: method

Presents a new document window with preset contents.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
@preconcurrency func callAsFunction(contentType: UTType, prepareDocument: @escaping (ModelContext) -> Void)
```

#### Discussion

Don’t call this method directly. SwiftUI calls it when you call the [`newDocument`](environmentvalues/newdocument.md) action.

For example, a Todo app might have a way to create a sample prepopulated Todo list as a part of onboarding experience:

```swift
newDocument(contentType: .todoList) { modelContext in
    let todoList = TodoList(
        title: "🎬 Movie night",
        items: [
            TodoItem(title: "🍿 Buy popcorn"),
            TodoItem(title: "🍨 Make some ice cream",
            TodoItem(title: "💡 Hang a string of lights")
        ]
    )
    modelContext.insert(todoList)
}
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [`Methods with Special Names`](https://developer.apple.comhttps://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in *The Swift Programming Language*.

## Parameters

- `contentType`: The content type of the document.
- `prepareDocument`: The closure that accepts `ModelContext` associated with the new document. Use this closure to set the document’s initial contents before it is displayed: insert preconfigured models in the provided `ModelContext`.

## See Also

- [func callAsFunction(_:)](newdocumentaction/callasfunction(_:).md)
  Presents a new document window.
- [func callAsFunction(contentType: UTType)](newdocumentaction/callasfunction(contenttype:).md)
  Presents a new document window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/newdocumentaction/callasfunction(contenttype:preparedocument:))*