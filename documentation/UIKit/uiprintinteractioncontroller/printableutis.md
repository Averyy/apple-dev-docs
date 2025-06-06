# printableUTIs

**Framework**: UIKit  
**Kind**: property

Returns a set of the Uniform Type Identifiers for the types of data that UIKit can print.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class var printableUTIs: Set<String> { get }
```

#### Return Value

A set object that contains, as strings, the UTIs identifying data types that UIKit knows how to print natively.

## See Also

- [class var isPrintingAvailable: Bool](uiprintinteractioncontroller/isprintingavailable.md)
  A Boolean value that indicates whether the device supports printing.
- [class func canPrint(Data) -> Bool](uiprintinteractioncontroller/canprint(_:)-4e0bs.md)
  Returns a Boolean value that indicates whether UIKit can print the contents of a data object.
- [class func canPrint(URL) -> Bool](uiprintinteractioncontroller/canprint(_:)-364vj.md)
  Returns a Boolean value that indicates whether UIKit can print the file that the specified URL references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/printableutis)*