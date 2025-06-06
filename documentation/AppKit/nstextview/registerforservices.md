# registerForServices()

**Framework**: AppKit  
**Kind**: method

Registers send and return types for the Services facility.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class func registerForServices()
```

#### Discussion

This method is invoked automatically when the first instance of a text view is created; you should never need to invoke it directly.

Subclasses of  `NSTextView` that wish to add support for new service types should override [`registerForServices()`](nstextview/registerforservices().md) to call `super` and then register their own new types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/registerforservices())*