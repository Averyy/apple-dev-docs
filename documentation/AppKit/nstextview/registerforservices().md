# registerForServices()

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Registers send and return types for the Services facility.

**Availability**:
- macOS

## Declaration

```swift
class func registerForServices()
```

```objc
+ (void) registerForServices;
```

## Discussion

This method is invoked automatically when the first instance of a text view is created; you should never need to invoke it directly.

Subclasses of  `NSTextView` that wish to add support for new service types should override [`registerForServices()`](./registerforservices%28%29.md) to call `super` and then register their own new types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/registerforservices())*