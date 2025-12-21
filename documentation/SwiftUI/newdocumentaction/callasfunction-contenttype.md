# callAsFunction(contentType:)

**Framework**: SwiftUI  
**Kind**: method

Presents a new document window.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
@preconcurrency func callAsFunction(contentType: UTType)
```

#### Discussion

Don’t call this method directly. SwiftUI calls it when you call the [`newDocument`](environmentvalues/newdocument.md) action:

```swift
newDocument(contentType: .todoList)

 extension UTType {
     static let todoList = UTType(exportedAs: "com.myApp.todoList")
 }
```

> ❗ **Important**: If your app declares custom uniform type identifiers, include corresponding entries in the app’s `Info.plist` file. For more information, see [`Defining file and data types for your app`](https://developer.apple.com/documentation/UniformTypeIdentifiers/defining-file-and-data-types-for-your-app). Also, remember to specify the supported Document types in the `Info.plist` file as well.

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [`Methods with Special Names`](https://developer.apple.comhttps://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in .

## Parameters

- `contentType`: The content type of the document.

## See Also

- [func callAsFunction(_:)](newdocumentaction/callasfunction(_:).md)
  Presents a new document window.
- [func callAsFunction(contentType: UTType, prepareDocument: (ModelContext) -> Void)](newdocumentaction/callasfunction(contenttype:preparedocument:).md)
  Presents a new document window with preset contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/newdocumentaction/callasfunction(contenttype:))*