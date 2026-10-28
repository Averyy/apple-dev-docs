# printInfo()

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Returns a print-information object initialized with default values.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func printInfo() -> UIPrintInfo
```

```objc
+ (UIPrintInfo *) printInfo;
```

## Return Value

An instance of `UIPrintInfo` or `nil` if the object could not be created.

## See Also

### Creating a print info object
- [init(dictionary: [AnyHashable : Any]?)](./init%28dictionary%29.md)
  Returns a print-information object that is initialized with the data in the passed-in dictionary.
- [var dictionaryRepresentation: [AnyHashable : Any]](./dictionaryrepresentation.md)
  A dictionary representation of a print-information object.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a print info object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinfo/printinfo())*