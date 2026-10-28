# callAsFunction(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents a new document window for the in-memory document returned by the provided closure.

**Availability**:
- macOS 27.0+

## Declaration

```swift
@MainActor
@preconcurrency func callAsFunction<D>(_ newDocument: @autoclosure @escaping @Sendable () -> sending D) where D : ReadableDocument
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func callAsFunction<D>(_ newDocument: @autoclosure @escaping @Sendable () -> D) where D : FileDocument
```

```swift
@MainActor
@preconcurrency func callAsFunction<D>(_ newDocument: @escaping @Sendable () -> D) where D : ReferenceFileDocument
```

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the [`newDocument`](../environmentvalues/newdocument.md) action with a [`ReadableDocument`](../readabledocument.md) factory.

The factory closure runs when SwiftUI needs the document instance. SwiftUI then injects the instance into the matching [`DocumentGroup`](../documentgroup.md) and presents its window. The matching document group is the first creatable group whose readable content types overlap with `D.readableContentTypes`.

## Parameters

- `newDocument`: A closure that produces the in-memory document to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/newdocumentaction/callasfunction(_:)-9h3ie)*