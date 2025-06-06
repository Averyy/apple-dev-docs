# canPrint(_:)

**Framework**: UIKit  
**Kind**: method

Returns a Boolean value that indicates whether UIKit can print the contents of a data object.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func canPrint(_ data: Data) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if UIKit can print the contents of the data object, otherwise [`false`](https://developer.apple.com/documentation/swift/false). The method returns [`false`](https://developer.apple.com/documentation/swift/false) if `data` is PDF data that specifies that printing is not allowed.

#### Discussion

You should call this method to test a data object prior to assigning it to [`printingItem`](uiprintinteractioncontroller/printingitem.md) or [`printingItems`](uiprintinteractioncontroller/printingitems.md).

## Parameters

- `data`: An instance of the   class that contains PDF data or an image in a format supported by the Image I/O framework. See   in   for a list of the supported image formats.

## See Also

- [class var isPrintingAvailable: Bool](uiprintinteractioncontroller/isprintingavailable.md)
  A Boolean value that indicates whether the device supports printing.
- [class func canPrint(URL) -> Bool](uiprintinteractioncontroller/canprint(_:)-364vj.md)
  Returns a Boolean value that indicates whether UIKit can print the file that the specified URL references.
- [class var printableUTIs: Set<String>](uiprintinteractioncontroller/printableutis.md)
  Returns a set of the Uniform Type Identifiers for the types of data that UIKit can print.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/canprint(_:)-4e0bs)*