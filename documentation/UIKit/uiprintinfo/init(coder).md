# init(coder:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a print info object from data in an unarchiver.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## See Also

### Creating a print info object
- [class func printInfo() -> UIPrintInfo](./printinfo%28%29.md)
  Returns a print-information object initialized with default values.
- [init(dictionary: [AnyHashable : Any]?)](./init%28dictionary%29.md)
  Returns a print-information object that is initialized with the data in the passed-in dictionary.
- [var dictionaryRepresentation: [AnyHashable : Any]](./dictionaryrepresentation.md)
  A dictionary representation of a print-information object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinfo/init(coder:))*