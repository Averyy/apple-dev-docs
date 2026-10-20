# CTFontCollection

**Framework**: Core Text  
**Kind**: class  
**Role**: Class

A font collection.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class CTFontCollection
```

```c
typedef const struct __CTFontCollection * CTFontCollectionRef;
```

#### Overview

A font collection represents a group of font descriptors taken together as a single object.

Font collections provide the capabilities of font enumeration, access to global and custom font collections, and access to the font descriptors comprising the collection.

## Topics

### Creating Font Collections
- [func CTFontCollectionCreateFromAvailableFonts(CFDictionary?) -> CTFontCollection](./ctfontcollectioncreatefromavailablefonts%28_%29.md)
  Returns a new font collection containing all available fonts.
- [func CTFontCollectionCreateWithFontDescriptors(CFArray?, CFDictionary?) -> CTFontCollection](./ctfontcollectioncreatewithfontdescriptors%28_,_%29.md)
  Returns a new font collection based on the given array of font descriptors.
- [func CTFontCollectionCreateCopyWithFontDescriptors(CTFontCollection, CFArray?, CFDictionary?) -> CTFontCollection](./ctfontcollectioncreatecopywithfontdescriptors%28_,_,_%29.md)
  Returns a copy of the original collection augmented with the given new font descriptors.
- [func CTFontCollectionCreateMutableCopy(CTFontCollection) -> CTMutableFontCollection](./ctfontcollectioncreatemutablecopy%28_%29.md)
  Creates a mutable copy of the original collection.
### Excluding and Including Font Descriptors
- [func CTFontCollectionCopyExclusionDescriptors(CTFontCollection) -> CFArray?](./ctfontcollectioncopyexclusiondescriptors%28_%29.md)
  Retrieves the array of descriptors to exclude from the match.
- [func CTFontCollectionCopyQueryDescriptors(CTFontCollection) -> CFArray?](./ctfontcollectioncopyquerydescriptors%28_%29.md)
  Retrieves the array of descriptors for font matching.
- [func CTFontCollectionSetExclusionDescriptors(CTMutableFontCollection, CFArray?)](./ctfontcollectionsetexclusiondescriptors%28_,_%29.md)
  Replaces the array of descriptors to exclude from the match.
- [func CTFontCollectionSetQueryDescriptors(CTMutableFontCollection, CFArray?)](./ctfontcollectionsetquerydescriptors%28_,_%29.md)
  Replaces the array of descriptors for font matching.
### Getting Font Descriptors
- [func CTFontCollectionCreateMatchingFontDescriptors(CTFontCollection) -> CFArray?](./ctfontcollectioncreatematchingfontdescriptors%28_%29.md)
  Returns an array of font descriptors matching the collection.
- [func CTFontCollectionCreateMatchingFontDescriptorsWithOptions(CTFontCollection, CFDictionary?) -> CFArray?](./ctfontcollectioncreatematchingfontdescriptorswithoptions%28_,_%29.md)
  Creates an array of font descriptors that match the specified collection.
- [func CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(CTFontCollection, CTFontCollectionSortDescriptorsCallback?, UnsafeMutableRawPointer?) -> CFArray?](./ctfontcollectioncreatematchingfontdescriptorssortedwithcallback%28_,_,_%29.md)
  Returns the array of matching font descriptors sorted with the callback function.
- [func CTFontCollectionCreateMatchingFontDescriptorsForFamily(CTFontCollection, CFString, CFDictionary?) -> CFArray?](./ctfontcollectioncreatematchingfontdescriptorsforfamily%28_,_,_%29.md)
  Retrieves an array of font descriptors that match the specified family, one descriptor for each style in the collection.
- [typealias CTFontCollectionSortDescriptorsCallback](./ctfontcollectionsortdescriptorscallback.md)
  The collection sorting callback type.
### Get Font Descriptor Attributes
- [func CTFontCollectionCopyFontAttribute(CTFontCollection, CFString, CTFontCollectionCopyOptions) -> CFArray](./ctfontcollectioncopyfontattribute%28_,_,_%29.md)
  Retrieves an array of font descriptor attribute values.
- [func CTFontCollectionCopyFontAttributes(CTFontCollection, CFSet, CTFontCollectionCopyOptions) -> CFArray](./ctfontcollectioncopyfontattributes%28_,_,_%29.md)
  Retrieves an array of dictionaries containing font descriptor attribute values.
### Getting the Type Identifier
- [func CTFontCollectionGetTypeID() -> CFTypeID](./ctfontcollectiongettypeid%28%29.md)
  Returns the type identifier for Core Text font collection references.
### Data Types
- [class CTMutableFontCollection](./ctmutablefontcollection.md)
  A reference to a mutable font collection.
### Constants
- [let kCTFontCollectionRemoveDuplicatesOption: CFString](./kctfontcollectionremoveduplicatesoption.md)
- [struct CTFontCollectionCopyOptions](./ctfontcollectioncopyoptions.md)
  Option bits for use with CTFontCollectionCopyFontAttribute(s).

## Relationships

### Inherited By
- [CTMutableFontCollection](./ctmutablefontcollection.md)
### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Opaque Types
- [class CTFont](./ctfont.md)
  A font object.
- [class CTFontDescriptor](./ctfontdescriptor.md)
  A font descriptor.
- [class CTFrame](./ctframe.md)
  A frame.
- [class CTFramesetter](./ctframesetter.md)
  Generate text frames.
- [class CTGlyphInfo](./ctglyphinfo.md)
  Override a font’s specified mapping from Unicode to the glyph ID.
- [class CTLine](./ctline.md)
  A line of text.
- [class CTParagraphStyle](./ctparagraphstyle.md)
  Paragraph or ruler attributes in an attributed string.
- [class CTRun](./ctrun.md)
  A glyph run.
- [class CTRunDelegate](./ctrundelegate.md)
  A run delegate.
- [class CTTextTab](./cttexttab.md)
  A tab in a paragraph style, storing an alignment type and location.
- [class CTTypesetter](./cttypesetter.md)
  A typesetter which performs line layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcollection)*