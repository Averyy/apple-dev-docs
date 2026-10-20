# init()

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns an empty document object.

**Availability**:
- macOS

## Declaration

```swift
init()
```

```objc
- (instancetype) init;
```

#### Return Value

An initialized `NSDocument` object.

#### Discussion

This initializer (the designated initializer) is invoked by each of the other `NSDocument` initialization methods.

You can override this method to perform initialization that must be done both when creating new empty documents and when opening existing documents. Your override must invoke `super` to initialize private `NSDocument` instance variables. It must never return `nil`. If an error can occur during object initialization, check for the error in an override of [`init(type:)`](./init%28type%29.md), [`init(contentsOf:ofType:)`](./init%28contentsof,oftype%29.md), or [`init(for:withContentsOf:ofType:)`](./init%28for,withcontentsof,oftype%29.md), because those methods can return `NSError` objects.

## See Also

### Related Documentation
- [Developing a Document-Based App](../developing-a-document-based-app.md)
  Write an app that creates, manages, edits, and saves text documents.
### Creating a Document Object
- [convenience init(contentsOf: URL, ofType: String) throws](./init%28contentsof,oftype%29.md)
  Initializes a document located by a URL of a specified type.
- [convenience init(for: URL?, withContentsOf: URL, ofType: String) throws](./init%28for,withcontentsof,oftype%29.md)
  Initializes a document with the specified contents, and places the resulting document’s file at the designated location.
- [convenience init(type: String) throws](./init%28type%29.md)
  Initializes a document of a specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/init())*