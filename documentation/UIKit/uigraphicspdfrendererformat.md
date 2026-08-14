# UIGraphicsPDFRendererFormat

**Framework**: UIKit  
**Kind**: class

A set of drawing attributes that represents the configuration of a PDF renderer context.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class UIGraphicsPDFRendererFormat
```

#### Overview

Use this subclass of [`UIGraphicsRendererFormat`](uigraphicsrendererformat.md) to provide context configuration parameters to a [`UIGraphicsPDFRenderer`](uigraphicspdfrenderer.md).

Create an instance and then add PDF configuration parameters to the [`documentInfo`](uigraphicspdfrendererformat/documentinfo.md) dictionary.

The following code demonstrates how you can use a PDF renderer format object to specify the author of the PDFs created by a PDF renderer.

**Swift**:

```swift
let format = UIGraphicsPDFRendererFormat()
format.documentInfo = [ kCGPDFContextAuthor as String : "Kate Bell" ]
let renderer =
  UIGraphicsPDFRenderer(bounds: CGRect(x: 0, y: 0, width: 500, height: 300),
                        format: format)
```

**Objective-C**:

```objc
UIGraphicsPDFRendererFormat *format = [[UIGraphicsPDFRendererFormat alloc] init];
format.documentInfo = @{ (NSString *)kCGPDFContextAuthor : @"Kate Bell" };
UIGraphicsPDFRenderer *renderer =
    [[UIGraphicsPDFRenderer alloc] initWithBounds:CGRectMake(0, 0, 500, 300)
                                           format:format];
```

## Topics

### Getting the PDF document info
- [var documentInfo: [String : Any]](uigraphicspdfrendererformat/documentinfo.md)
  A dictionary that specifies additional information to be associated with the PDFs created by the PDF renderer.

## Relationships

### Inherits From
- [UIGraphicsRendererFormat](uigraphicsrendererformat.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class UIGraphicsRenderer](uigraphicsrenderer.md)
  An abstract base class for creating graphics renderers.
- [class UIGraphicsRendererContext](uigraphicsrenderercontext.md)
  The base class for the drawing environments for graphics renderers.
- [class UIGraphicsRendererFormat](uigraphicsrendererformat.md)
  A set of drawing attributes that represents the configuration of a graphics renderer context.
- [class UIGraphicsImageRenderer](uigraphicsimagerenderer.md)
  A graphics renderer for creating Core Graphics-backed images.
- [class UIGraphicsImageRendererContext](uigraphicsimagerenderercontext.md)
  The drawing environment for an image renderer.
- [class UIGraphicsImageRendererFormat](uigraphicsimagerendererformat.md)
  A set of drawing attributes that represents the configuration of an image renderer context.
- [class UIGraphicsPDFRenderer](uigraphicspdfrenderer.md)
  A graphics renderer for creating PDFs.
- [class UIGraphicsPDFRendererContext](uigraphicspdfrenderercontext.md)
  The drawing environment for a PDF renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicspdfrendererformat)*