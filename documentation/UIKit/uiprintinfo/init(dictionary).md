# init(dictionary:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Returns a print-information object that is initialized with the data in the passed-in dictionary.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(dictionary: [AnyHashable : Any]?)
```

```objc
+ (UIPrintInfo *) printInfoWithDictionary:(NSDictionary *) dictionary;
```

## Return Value

An instance of `UIPrintInfo` or `nil` if the object could not be created.

## Discussion

You use the `dictionary` parameter to initialize a `UIPrintInfo` object with stored print-job information.  Some applications might archive a previous `UIPrintInfo` object and use that for a future print job with this method.

You can later access the dictionary by calling the [`dictionaryRepresentation`](./dictionaryrepresentation.md) method on the `UIPrintInfo` object.

## Parameters

- `dictionary`: A dictionary that contains data to initialize the `UIPrintInfo` object with.

## See Also

### Creating a print info object
- [class func printInfo() -> UIPrintInfo](./printinfo%28%29.md)
  Returns a print-information object initialized with default values.
- [var dictionaryRepresentation: [AnyHashable : Any]](./dictionaryrepresentation.md)
  A dictionary representation of a print-information object.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a print info object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinfo/init(dictionary:))*