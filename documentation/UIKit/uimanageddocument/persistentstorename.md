# persistentStoreName

**Framework**: UIKit  
**Kind**: property

Returns the name for the persistent store file inside the document’s file package.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class var persistentStoreName: String { get }
```

#### Return Value

The name for the persistent store file inside the document’s file package.

#### Discussion

This path component is appended to the document URL provided by [`UIDocument`](uidocument.md). The default name is `persistentStore`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimanageddocument/persistentstorename)*