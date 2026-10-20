# bestRepresentation(for:context:hints:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the best representation of the image for the specified rectangle using the provided hints.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func bestRepresentation(for rect: NSRect, context referenceContext: NSGraphicsContext?, hints: [NSImageRep.HintKey : Any]?) -> NSImageRep?
```

```objc
- (NSImageRep *) bestRepresentationForRect:(NSRect) rect context:(NSGraphicsContext *) referenceContext hints:(NSDictionary<NSString *,id> *) hints;
```

#### Return Value

The image representation that most closely matches the specified criteria.

## Parameters

- `rect`: The area of the image to return.
- `referenceContext`: A graphics context. This value can be `nil`.
- `hints`: An optional dictionary of hints that provide more context for selecting or generating a `CGImage`, and may override properties of the `referenceContext`. See `Image Hint Dictionary Keys` for a summary of the possible key-value pairs.

## See Also

### Working with Representations of Images
- [func addRepresentation(NSImageRep)](./addrepresentation%28_%29.md)
  Adds the specified image representation object to the image.
- [func addRepresentations([NSImageRep])](./addrepresentations%28_%29.md)
  Adds an array of image representation objects to the image.
- [var representations: [NSImageRep]](./representations.md)
  An array containing all of the image object’s image representations.
- [func removeRepresentation(NSImageRep)](./removerepresentation%28_%29.md)
  Removes and releases the specified image representation.
- [NSImageRep.HintKey](../nsimagerep/hintkey.md)
  Constants for the keys to include in a hints dictionary when drawing the image.
- [NSImage.LayoutDirection](./layoutdirection.md)
  Constants that describe the layout direction for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/bestrepresentation(for:context:hints:))*