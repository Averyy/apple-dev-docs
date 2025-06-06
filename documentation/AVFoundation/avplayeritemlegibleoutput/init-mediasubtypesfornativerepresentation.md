# init(mediaSubtypesForNativeRepresentation:)

**Framework**: Avfoundation  
**Kind**: init

Creates an initialized legible-output object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(mediaSubtypesForNativeRepresentation subtypes: [NSNumber])
```

## Mentions

- [init](1805461-init.md)

#### Return Value

An initialized instance of `AVPlayerItemLegibleOutput`.

#### Discussion

When creating an instance you add media subtype FourCC codes as `NSNumber` objects to the `subtypes` array to elect to receive that type as a [`CMSampleBuffer`](https://developer.apple.com/documentation/CoreMedia/CMSampleBuffer) instead of an attributed string. FourCC codes are converted to `NSNumber` objects as shown:

```objc
@[ [NSNumber numberWithUnsignedInt:'tx3g'] ]
```

Initializing an `AVPlayerItemLegibleOutput` using the `init` method (which is preferred) is equivalent to calling this method with an empty `subtypes` array, which means that all legible data, regardless of media subtype, is delivered using [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString) instances in a common format.

If a media subtype for which there is no legible data in the current player item is included in the media `subtypes` array, no error occurs.  An `AVPlayerItemLegibleOutput` instance doesn’t vend closed caption data as a [`CMSampleBuffer`](https://developer.apple.com/documentation/CoreMedia/CMSampleBuffer), so it is an error to include `'c608'` in the media subtypes array.

> **Note**:  The preferred method of creating an `AVPlayerItemLegibleOutput` object is to use the [`init`](1805461-init.md) method.

## Parameters

- `subtypes`: An   of   FourCC codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/init(mediasubtypesfornativerepresentation:))*