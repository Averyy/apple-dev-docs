# isPrintingAvailable

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether the device supports printing.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class var isPrintingAvailable: Bool { get }
```

```objc
@property (class, nonatomic, readonly, getter=isPrintingAvailable) BOOL printingAvailable;
```

## Discussion

This value is [`true`](../../Swift/true.md) if the device supports printing, otherwise [`false`](../../Swift/false.md). An application can show or hide any print buttons based on this value.

## See Also

### Determining printability
- [class func canPrint(Data) -> Bool](./canprint%28_%29-4e0bs.md)
  Returns a Boolean value that indicates whether UIKit can print the contents of a data object.
- [class func canPrint(URL) -> Bool](./canprint%28_%29-364vj.md)
  Returns a Boolean value that indicates whether UIKit can print the file that the specified URL references.
- [class var printableUTIs: Set<String>](./printableutis.md)
  Returns a set of the Uniform Type Identifiers for the types of data that UIKit can print.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/isprintingavailable)*