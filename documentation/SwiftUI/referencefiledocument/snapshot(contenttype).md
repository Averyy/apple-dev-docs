# snapshot(contentType:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a snapshot that represents the current state of the document.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+

> **Deprecated**: Use Document protocol instead.

## Declaration

```swift
func snapshot(contentType: UTType) throws -> Self.Snapshot
```

#### Return Value

A snapshot of the document content that the system provides to the [`fileWrapper(snapshot:configuration:)`](./filewrapper%28snapshot,configuration%29.md) method for serialization.

#### Discussion

To store a document — for example, in response to a Save command — SwiftUI begins by calling this method. Return a copy of the document’s content from your implementation of the method. For example, you might define an initializer for your document’s model object that copies the contents of the document’s instance, and return that:

```swift
func snapshot(contentType: UTType) throws -> Snapshot {
    Model(from: model) // Creates a copy.
}
```

SwiftUI prevents document edits during the snapshot operation to ensure that the model state remains coherent. After the call completes, SwiftUI reenables edits, and then calls the [`fileWrapper(snapshot:configuration:)`](./filewrapper%28snapshot,configuration%29.md) method, where you serialize the snapshot and store it to a file.

> **Note**: SwiftUI calls this method on a background thread. Don’t make user interface changes from that thread.

## Parameters

- `contentType`: The content type that you create the document snapshot for.

## See Also

### Getting a snapshot
- [associatedtype Snapshot](./snapshot.md)
  A type that represents the document’s stored content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/referencefiledocument/snapshot(contenttype:))*