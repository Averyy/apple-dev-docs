# init(dictionary:)

**Framework**: UIKit  
**Kind**: init

Returns a print-information object that is initialized with the data in the passed-in dictionary.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(dictionary: [AnyHashable : Any]?)
```

#### Return Value

An instance of `UIPrintInfo` or `nil` if the object could not be created.

#### Discussion

You use the `dictionary` parameter to initialize a `UIPrintInfo` object with stored print-job information.  Some applications might archive a previous `UIPrintInfo` object and use that for a future print job with this method.

You can later access the dictionary by calling the [`dictionaryRepresentation`](uiprintinfo/dictionaryrepresentation.md) method on the `UIPrintInfo` object.

## Parameters

- `dictionary`: A dictionary that contains data to initialize the   object with.

## See Also

- [class func printInfo() -> UIPrintInfo](uiprintinfo/printinfo.md)
  Returns a print-information object initialized with default values.
- [var dictionaryRepresentation: [AnyHashable : Any]](uiprintinfo/dictionaryrepresentation.md)
  A dictionary representation of a print-information object.
- [init?(coder: NSCoder)](uiprintinfo/init(coder:).md)
  Creates a print info object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinfo/init(dictionary:))*