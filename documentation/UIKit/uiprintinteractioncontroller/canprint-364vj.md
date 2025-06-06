# canPrint(_:)

**Framework**: UIKit  
**Kind**: method

Returns a Boolean value that indicates whether UIKit can print the file that the specified URL references.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func canPrint(_ url: URL) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if UIKit can print the contents of the referenced file, otherwise [`false`](https://developer.apple.com/documentation/swift/false). The method returns [`false`](https://developer.apple.com/documentation/swift/false) if `url` references PDF data that specifies that printing is not allowed.

#### Discussion

You should call this method to test the data referenced by a URL prior to assigning that URL to [`printingItem`](uiprintinteractioncontroller/printingitem.md) or [`printingItems`](uiprintinteractioncontroller/printingitems.md).

## Parameters

- `url`: An object representing a URL. Valid   objects must use the   or any scheme that can return an   object with a registered protocol. The file referenced by the URL must contain PDF data or an image in a format supported by the Image I/O framework. See   in   for a list of the supported image formats.

## See Also

- [class var isPrintingAvailable: Bool](uiprintinteractioncontroller/isprintingavailable.md)
  A Boolean value that indicates whether the device supports printing.
- [class func canPrint(Data) -> Bool](uiprintinteractioncontroller/canprint(_:)-4e0bs.md)
  Returns a Boolean value that indicates whether UIKit can print the contents of a data object.
- [class var printableUTIs: Set<String>](uiprintinteractioncontroller/printableutis.md)
  Returns a set of the Uniform Type Identifiers for the types of data that UIKit can print.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/canprint(_:)-364vj)*