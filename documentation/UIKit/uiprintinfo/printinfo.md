# printInfo()

**Framework**: UIKit  
**Kind**: method

Returns a print-information object initialized with default values.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func printInfo() -> UIPrintInfo
```

#### Return Value

An instance of `UIPrintInfo` or `nil` if the object could not be created.

## See Also

- [init(dictionary: [AnyHashable : Any]?)](uiprintinfo/init(dictionary:).md)
  Returns a print-information object that is initialized with the data in the passed-in dictionary.
- [var dictionaryRepresentation: [AnyHashable : Any]](uiprintinfo/dictionaryrepresentation.md)
  A dictionary representation of a print-information object.
- [init?(coder: NSCoder)](uiprintinfo/init(coder:).md)
  Creates a print info object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinfo/printinfo())*