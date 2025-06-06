# isPrintingAvailable

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the device supports printing.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class var isPrintingAvailable: Bool { get }
```

#### Discussion

This value is [`true`](https://developer.apple.com/documentation/swift/true) if the device supports printing, otherwise [`false`](https://developer.apple.com/documentation/swift/false). An application can show or hide any print buttons based on this value.

## See Also

- [class func canPrint(Data) -> Bool](uiprintinteractioncontroller/canprint(_:)-4e0bs.md)
  Returns a Boolean value that indicates whether UIKit can print the contents of a data object.
- [class func canPrint(URL) -> Bool](uiprintinteractioncontroller/canprint(_:)-364vj.md)
  Returns a Boolean value that indicates whether UIKit can print the file that the specified URL references.
- [class var printableUTIs: Set<String>](uiprintinteractioncontroller/printableutis.md)
  Returns a set of the Uniform Type Identifiers for the types of data that UIKit can print.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/isprintingavailable)*