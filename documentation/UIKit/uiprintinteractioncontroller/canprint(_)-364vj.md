# canPrint(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether UIKit can print the file that the specified URL references.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func canPrint(_ url: URL) -> Bool
```

```objc
+ (BOOL) canPrintURL:(NSURL *) url;
```

## Return Value

[`true`](../../Swift/true.md) if UIKit can print the contents of the referenced file, otherwise [`false`](../../Swift/false.md). The method returns [`false`](../../Swift/false.md) if `url` references PDF data that specifies that printing is not allowed.

## Discussion

You should call this method to test the data referenced by a URL prior to assigning that URL to [`printingItem`](./printingitem.md) or [`printingItems`](./printingitems.md).

## Parameters

- `url`: An object representing a URL. Valid `NSURL` objects must use the `file:` or any scheme that can return an [`NSData`](../../Foundation/nsdata.md) object with a registered protocol. The file referenced by the URL must contain PDF data or an image in a format supported by the Image I/O framework. See [View Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewPG_iPhoneOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009503) in [View Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewPG_iPhoneOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009503) for a list of the supported image formats.

## See Also

### Determining printability
- [class var isPrintingAvailable: Bool](./isprintingavailable.md)
  A Boolean value that indicates whether the device supports printing.
- [class func canPrint(Data) -> Bool](./canprint%28_%29-4e0bs.md)
  Returns a Boolean value that indicates whether UIKit can print the contents of a data object.
- [class var printableUTIs: Set<String>](./printableutis.md)
  Returns a set of the Uniform Type Identifiers for the types of data that UIKit can print.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/canprint(_:)-364vj)*