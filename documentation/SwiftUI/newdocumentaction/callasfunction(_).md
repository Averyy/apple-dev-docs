# callAsFunction(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents a new document window.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
@preconcurrency func callAsFunction<D>(_ newDocument: @autoclosure @escaping @Sendable () -> D) where D : FileDocument
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func callAsFunction<D>(_ newDocument: @autoclosure @escaping @Sendable () -> sending D) where D : ReadableDocument
```

```swift
@MainActor
@preconcurrency func callAsFunction<D>(_ newDocument: @escaping @Sendable () -> D) where D : ReferenceFileDocument
```

#### Discussion

Don’t call this method directly. SwiftUI calls it when you call the [`newDocument`](../environmentvalues/newdocument.md) action:

```swift
newDocument(TextDocument(text: selectedText))
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in *The Swift Programming Language*.

## Parameters

- `newDocument`: The new file document to present.

## See Also

### Calling the action
- [func callAsFunction(contentType: UTType)](./callasfunction%28contenttype%29.md)
  Presents a new document window.
- [func callAsFunction(contentType: UTType, prepareDocument: (ModelContext) -> Void)](./callasfunction%28contenttype,preparedocument%29.md)
  Presents a new document window with preset contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/newdocumentaction/callasfunction(_:))*