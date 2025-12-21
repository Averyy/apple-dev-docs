# init(_:)

**Framework**: Foundation  
**Kind**: init

Creates a new template from its text form.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init?(_ template: String)
```

#### Discussion

The template string needs to be a valid RFC 6570 template.

This will parse the template and return `nil` if the template is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/template/init(_:))*