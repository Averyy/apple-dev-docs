# init(context:for:)

**Framework**: TVMLKit  
**Kind**: init

Creates a new document view controller with a specific context and app controller.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
@MainActor
convenience init(context: [String : Any], for appController: TVApplicationController)
```

#### Discussion

The `context` parameter provides information to `TVMLKit JS` to determine which document to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvdocumentviewcontroller/init(context:for:))*