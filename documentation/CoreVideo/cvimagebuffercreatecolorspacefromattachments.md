# CVImageBufferCreateColorSpaceFromAttachments(_:)

**Framework**: Core Video  
**Kind**: func

Attempts to create a Core Graphics color space from the image buffer’s attachments that you specify.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func CVImageBufferCreateColorSpaceFromAttachments(_ attachments: CFDictionary) -> Unmanaged<CGColorSpace>?
```

#### Return Value

A [`CGColorSpace`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace) object that represents the color space of the image buffer, or [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) if the dictionary doesn’t contain the information required to create a [`CGColorSpace`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace) instance.

#### Discussion

To generate a [`CGColorSpace`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace) instance, the attachments dictionary needs to include values for either:

1. [`kCVImageBufferICCProfileKey`](kcvimagebuffericcprofilekey.md)
2. [`kCVImageBufferColorPrimariesKey`](kcvimagebuffercolorprimarieskey.md), [`kCVImageBufferTransferFunctionKey`](kcvimagebuffertransferfunctionkey.md), [`kCVImageBufferYCbCrMatrixKey`](kcvimagebufferycbcrmatrixkey.md), and possibly [`kCVImageBufferGammaLevelKey`](kcvimagebuffergammalevelkey.md)

Use [`CGColorSpaceRelease`](https://developer.apple.com/documentation/coregraphics/1408855-cgcolorspacerelease) to release the color space when you’re done with it.

## Parameters

- `attachments`: The dictionary of attachments for an image buffer, which you can obtain by calling   on the image buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagebuffercreatecolorspacefromattachments(_:))*