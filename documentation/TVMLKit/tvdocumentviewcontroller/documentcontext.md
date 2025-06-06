# documentContext

**Framework**: TVMLKit  
**Kind**: property

The current document context.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
@MainActor
var documentContext: [String : Any] { get }
```

#### Discussion

Use this property to retrieve the current context, whether it’s new or updated.

## See Also

- [var appController: TVApplicationController?](tvdocumentviewcontroller/appcontroller.md)
  The document’s app controller that bridges UI, navigation stack, storage, and event handling from JavaScript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvdocumentviewcontroller/documentcontext)*