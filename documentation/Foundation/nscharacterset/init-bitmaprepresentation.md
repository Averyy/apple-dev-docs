# init(bitmapRepresentation:)

**Framework**: Foundation  
**Kind**: init

Returns a character set containing characters determined by a given bitmap representation.

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
init(bitmapRepresentation data: Data)
```

#### Return Value

A character set containing characters determined by `data`.

#### Discussion

This method is useful for creating a character set object with data from a file or other external data source.

A raw bitmap representation of a character set is a byte array with the first 2^16 bits (that is, 8192 bytes) representing the code point range of the the Basic Multilingual Plane (BMP), such that the value of the bit at position n represents the presence in the character set of the character with decimal Unicode value n. A bitmap representation may contain zero to sixteen additional 8192 byte segments to for each additional Unicode plane containing a character in a character set, with each 8192 byte segment prepended with a single plane index byte.

To add a character in the Basic Multilingual Plane (BMP) with decimal Unicode value n to a raw bitmap representation, you might do the following:

```objc
unsigned char bitmapRep[8192];
bitmapRep[n >> 3] |= (((unsigned int)1) << (n & 7));
```

To remove that character:

```objc
bitmapRep[n >> 3] &= ~(((unsigned int)1) << (n & 7));
```

## Parameters

- `data`: A bitmap representation of a character set.

## See Also

- [init?(contentsOfFile: String)](nscharacterset/init(contentsoffile:).md)
  Returns a character set read from the bitmap representation stored in the file a given path.
- [var bitmapRepresentation: Data](nscharacterset/bitmaprepresentation.md)
  An `NSData` object encoding the receiver in binary format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscharacterset/init(bitmaprepresentation:))*