# canPrint(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether UIKit can print the contents of a data object.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func canPrint(_ data: Data) -> Bool
```

```objc
+ (BOOL) canPrintData:(NSData *) data;
```

## Return Value

[`true`](../../Swift/true.md) if UIKit can print the contents of the data object, otherwise [`false`](../../Swift/false.md). The method returns [`false`](../../Swift/false.md) if `data` is PDF data that specifies that printing is not allowed.

## Discussion

You should call this method to test a data object prior to assigning it to [`printingItem`](./printingitem.md) or [`printingItems`](./printingitems.md).

## Parameters

- `data`: An instance of the [`NSData`](../../Foundation/nsdata.md) class that contains PDF data or an image in a format supported by the Image I/O framework. See [View Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewPG_iPhoneOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009503) in [View Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewPG_iPhoneOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009503) for a list of the supported image formats.

## See Also

### Determining printability
- [class var isPrintingAvailable: Bool](./isprintingavailable.md)
  A Boolean value that indicates whether the device supports printing.
- [class func canPrint(URL) -> Bool](./canprint%28_%29-364vj.md)
  Returns a Boolean value that indicates whether UIKit can print the file that the specified URL references.
- [class var printableUTIs: Set<String>](./printableutis.md)
  Returns a set of the Uniform Type Identifiers for the types of data that UIKit can print.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/canprint(_:)-4e0bs)*