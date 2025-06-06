# dictionaryRepresentation

**Framework**: UIKit  
**Kind**: property

A dictionary representation of a print-information object.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var dictionaryRepresentation: [AnyHashable : Any] { get }
```

#### Return Value

A dictionary representation of a `UIPrintInfo` object that can be archived and used to create a new `UIPrintInfo` object. Returns `nil` if no dictionary can be created.

## See Also

- [class func printInfo() -> UIPrintInfo](uiprintinfo/printinfo.md)
  Returns a print-information object initialized with default values.
- [init(dictionary: [AnyHashable : Any]?)](uiprintinfo/init(dictionary:).md)
  Returns a print-information object that is initialized with the data in the passed-in dictionary.
- [init?(coder: NSCoder)](uiprintinfo/init(coder:).md)
  Creates a print info object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinfo/dictionaryrepresentation)*