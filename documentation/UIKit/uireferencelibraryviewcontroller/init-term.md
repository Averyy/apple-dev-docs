# init(term:)

**Framework**: UIKit  
**Kind**: init

Initializes a newly created reference-library view controller to display the definition of the given term.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(term: String)
```

#### Return Value

The newly initialized reference library view controller.

#### Discussion

If a definition for the term is not available, a localized message is displayed instead. Use the [`dictionaryHasDefinition(forTerm:)`](uireferencelibraryviewcontroller/dictionaryhasdefinition(forterm:).md) class method to determine whether a definition is available before creating instances of this class.

## Parameters

- `term`: The term to define.

## See Also

- [class func dictionaryHasDefinition(forTerm: String) -> Bool](uireferencelibraryviewcontroller/dictionaryhasdefinition(forterm:).md)
  Returns whether a definition is available for the given term.
- [init(coder: NSCoder)](uireferencelibraryviewcontroller/init(coder:).md)
  Creates a reference-library view controller from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uireferencelibraryviewcontroller/init(term:))*