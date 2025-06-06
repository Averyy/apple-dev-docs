# accessibilityIdentifier

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

A string that identifies the element.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var accessibilityIdentifier: String? { get set }
```

#### Discussion

An identifier can be used to uniquely identify an element in the scripts you write using the UI Automation interfaces. Using an identifier allows you to avoid inappropriately setting or accessing an element’s accessibility label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityidentification/accessibilityidentifier)*