# init()

**Framework**: AppKit  
**Kind**: init

Initializes and returns an empty document object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
init()
```

#### Return Value

An initialized `NSDocument` object.

#### Discussion

This initializer (the designated initializer) is invoked by each of the other `NSDocument` initialization methods.

You can override this method to perform initialization that must be done both when creating new empty documents and when opening existing documents. Your override must invoke `super` to initialize private `NSDocument` instance variables. It must never return `nil`. If an error can occur during object initialization, check for the error in an override of [`init(type:)`](nsdocument/init(type:).md), [`init(contentsOf:ofType:)`](nsdocument/init(contentsof:oftype:).md), or [`init(for:withContentsOf:ofType:)`](nsdocument/init(for:withcontentsof:oftype:).md), because those methods can return `NSError` objects.

## See Also

- [Document-Based App Programming Guide for Mac](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/DocBasedAppProgrammingGuideForOSX/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011179)
- [convenience init(contentsOf: URL, ofType: String) throws](nsdocument/init(contentsof:oftype:).md)
  Initializes a document located by a URL of a specified type.
- [convenience init(for: URL?, withContentsOf: URL, ofType: String) throws](nsdocument/init(for:withcontentsof:oftype:).md)
  Initializes a document with the specified contents, and places the resulting document’s file at the designated location.
- [convenience init(type: String) throws](nsdocument/init(type:).md)
  Initializes a document of a specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/init())*