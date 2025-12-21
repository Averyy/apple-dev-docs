# dictionaryHasDefinition(forTerm:)

**Framework**: UIKit  
**Kind**: method

Returns whether a definition is available for the given term.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func dictionaryHasDefinition(forTerm term: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if a definition for `term` is available; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `term`: The term to be defined.

## See Also

- [init(term: String)](uireferencelibraryviewcontroller/init(term:).md)
  Initializes a newly created reference-library view controller to display the definition of the given term.
- [init(coder: NSCoder)](uireferencelibraryviewcontroller/init(coder:).md)
  Creates a reference-library view controller from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uireferencelibraryviewcontroller/dictionaryhasdefinition(forterm:))*