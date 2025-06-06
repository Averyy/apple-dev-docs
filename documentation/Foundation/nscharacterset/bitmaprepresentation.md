# bitmapRepresentation

**Framework**: Foundation  
**Kind**: property

An `NSData` object encoding the receiver in binary format.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var bitmapRepresentation: Data { get }
```

#### Discussion

This format is suitable for saving to a file or otherwise transmitting or archiving.

A raw bitmap representation of a character set is a byte array with the first 2^16 bits (that is, 8192 bytes) representing the code point range of the the Basic Multilingual Plane (BMP), such that the value of the bit at position n represents the presence in the character set of the character with decimal Unicode value n. A bitmap representation may contain zero to sixteen additional 8192 byte segments to for each additional Unicode plane containing a character in a character set, with each 8192 byte segment prepended with a single plane index byte.

For example, a character set containing only Basic Latin (ASCII) characters, which are contained by the Basic Multilingual Plane (BMP, plane 0), has a bitmap representation with a size of 8192 bytes, whereas a character set containing both Basic Latin (ASCII) characters and emoji characters, which are contained by the Supplementary Multilingual Plane (SMP, plane 1), has a bitmap representation with a size of 16385 bytes (8192 bytes for BMP, followed by the byte `0x01` for the plane index of SMP, followed by 8192 bytes for SMP).

To test for the presence of a character in the Basic Multilingual Plane (BMP) with decimal Unicode value n in a raw bitmap representation, you might do the following:

```objc
unsigned char bitmapRep[8192];
if (bitmapRep[n >> 3] & (((unsigned int)1) << (n  & 7))) {
    /* Character is present. */
}
```

## See Also

- [init(bitmapRepresentation: Data)](nscharacterset/init(bitmaprepresentation:).md)
  Returns a character set containing characters determined by a given bitmap representation.
- [init?(contentsOfFile: String)](nscharacterset/init(contentsoffile:).md)
  Returns a character set read from the bitmap representation stored in the file a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscharacterset/bitmaprepresentation)*