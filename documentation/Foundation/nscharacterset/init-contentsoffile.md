# init(contentsOfFile:)

**Framework**: Foundation  
**Kind**: init

Returns a character set read from the bitmap representation stored in the file a given path.

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
init?(contentsOfFile fName: String)
```

#### Return Value

A character set read from the bitmap representation stored in the file at `path`.

#### Discussion

This method doesn’t use filenames to check for the uniqueness of the character sets it creates. To prevent duplication of character sets in memory, cache them and make them available through an API that checks whether the requested set has already been loaded.

To read a bitmap representation from any file, use the `NSData` method[`dataWithContentsOfFile:options:error:`](nsdata/datawithcontentsoffile:options:error:.md) and pass the result to [`init(bitmapRepresentation:)`](nscharacterset/init(bitmaprepresentation:).md).

## Parameters

- `fName`: A path to a file containing a bitmap representation of a character set. The path name must end with the extension  .

## See Also

- [init(bitmapRepresentation: Data)](nscharacterset/init(bitmaprepresentation:).md)
  Returns a character set containing characters determined by a given bitmap representation.
- [var bitmapRepresentation: Data](nscharacterset/bitmaprepresentation.md)
  An `NSData` object encoding the receiver in binary format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscharacterset/init(contentsoffile:))*