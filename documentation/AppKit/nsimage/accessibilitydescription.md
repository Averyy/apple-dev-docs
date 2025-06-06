# accessibilityDescription

**Framework**: AppKit  
**Kind**: property

The image’s accessibility description.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var accessibilityDescription: String? { get set }
```

#### Discussion

This description is used automatically by interface elements that display images.  Like all accessibility descriptions, use a short localized string that does not include the name of the interface element.  For instance, “delete” rather than “delete button”.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/accessibilitydescription)*