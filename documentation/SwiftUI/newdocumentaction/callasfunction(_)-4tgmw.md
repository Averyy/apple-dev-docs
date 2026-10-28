# callAsFunction(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents a new reference type document window.

**Availability**:
- macOS 13.0+ - Deprecated in 27.2

> **Deprecated**: Conform your document type to Document protocol instead.

## Declaration

```swift
@MainActor
@preconcurrency func callAsFunction<D>(_ newDocument: @escaping @Sendable () -> D) where D : ReferenceFileDocument
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func callAsFunction<D>(_ newDocument: @autoclosure @escaping @Sendable () -> D) where D : FileDocument
```

```swift
@MainActor
@preconcurrency func callAsFunction<D>(_ newDocument: @autoclosure @escaping @Sendable () -> sending D) where D : ReadableDocument
```

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the [`newDocument`](../environmentvalues/newdocument.md) action:

```swift
newDocument(TextDocument(text: selectedText))
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in *The Swift Programming Language*.

## Parameters

- `newDocument`: The new reference type file document to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/newdocumentaction/callasfunction(_:)-4tgmw)*