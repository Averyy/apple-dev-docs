# dictionaryHasDefinition(forTerm:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Returns whether a definition is available for the given term.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func dictionaryHasDefinition(forTerm term: String) -> Bool
```

```objc
+ (BOOL) dictionaryHasDefinitionForTerm:(NSString *) term;
```

#### Return Value

[`true`](../../Swift/true.md) if a definition for `term` is available; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `term`: The term to be defined.

## See Also

### Creating a reference-library view controller
- [init(term: String)](./init%28term%29.md)
  Initializes a newly created reference-library view controller to display the definition of the given term.
- [init(coder: NSCoder)](./init%28coder%29.md)
  Creates a reference-library view controller from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uireferencelibraryviewcontroller/dictionaryhasdefinition(forterm:))*