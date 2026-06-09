# CVAttachmentValueRepresentable

**Framework**: Core Video  
**Kind**: protocol

Allows Swift types to be used as buffer attachment value.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
protocol CVAttachmentValueRepresentable
```

#### Overview

A type conforming to this protocol can be used as value for an attachment key. The [`CVAttachmentRawValue`](cvattachmentrawvalue.md) type facilitates conversion to and from raw attachment values. Conformances of standard Swift type to this protocol are provided in CoreVideo framework. Implementing this protocol for a custom struct is as simple as:

```swift
struct MyStruct {
	var number: Int
	var tags: [String]
}

extension MyStruct: CVAttachmentValueRepresentable {
	static func makeFromRawAttachmentValue(_ repr: CVAttachmentRawValue) -> Self? {
		guard let number: Int = repr["number"], tags: [String] = repr["tags"] else { return nil }
		return .init(number: number, tags: tags)
	}

	var rawAttachmentValueRepresentation: CVAttachmentRawValue {
		["number": self.number, "tags": self.tags]
	}
}
```

Default implementation is provided for `RawRepresentable` protocol where RawValue conforms to this protocol. This allow enumeration with raw values to conform to [`CVAttachmentValueRepresentable`](cvattachmentvaluerepresentable.md) protocol without a custom implementation.

## Topics

### Instance Properties
- [var rawAttachmentValueRepresentation: CVAttachmentRawValue](cvattachmentvaluerepresentable/rawattachmentvaluerepresentation.md)
### Type Methods
- [static func makeFromRawAttachmentValue(CVAttachmentRawValue) -> Self?](cvattachmentvaluerepresentable/makefromrawattachmentvalue(_:).md)

## Relationships

### Conforming Types
- [CVImageAlphaChannelMode](cvimagealphachannelmode.md)
- [CVImageChromaField](cvimagechromafield.md)
- [CVImageChromaField.ChromaSubsampling](cvimagechromafield/chromasubsampling.md)
- [CVImageChromaField.FieldLocation](cvimagechromafield/fieldlocation-swift.enum.md)
- [CVImageChromaField.SampleLocation](cvimagechromafield/samplelocation.md)
- [CVImageCleanAperture](cvimagecleanaperture.md)
- [CVImageColorPrimaries](cvimagecolorprimaries.md)
- [CVImageDisplayMaskRectangle](cvimagedisplaymaskrectangle.md)
- [CVImageFieldDetail](cvimagefielddetail.md)
- [CVImageLogTransferFunction](cvimagelogtransferfunction.md)
- [CVImagePixelAspectRatio](cvimagepixelaspectratio.md)
- [CVImageStereoDisplayMaskRectangle](cvimagestereodisplaymaskrectangle.md)
- [CVImageTransferFunction](cvimagetransferfunction.md)
- [CVImageYCbCrMatrix](cvimageycbcrmatrix.md)
- [CVProResRawMetadata](cvproresrawmetadata.md)
- [CVProResRawMetadata.RecommendedCrop](cvproresrawmetadata/recommendedcrop-swift.struct.md)
- [CVSenselArrayPattern](cvsenselarraypattern.md)
- [CVSenselSitingOffsets](cvsenselsitingoffsets.md)

## See Also

- [protocol CVBufferRepresentable](cvbufferrepresentable.md)
  CVBufferRepresentable protocol is a sealed protocol intended to be implemented by the types in CoreVideo framework. This protocol facilitates Swift types that wrap a value of CVBuffer type.
- [protocol CVAttachmentKeyDefinitions](cvattachmentkeydefinitions.md)
  Marks a type as a collection of attachment keys for an attachment bearer.
- [protocol CVAttachmentModePreference](cvattachmentmodepreference.md)
  Defines preferred mode for an attachment key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvattachmentvaluerepresentable)*