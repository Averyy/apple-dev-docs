# dictionaryWithContentsOfURL:error:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates a dictionary using the keys and values found in a resource specified by a given URL.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```objc
+ (NSDictionary<NSString *,id> *) dictionaryWithContentsOfURL:(NSURL *) url error:(NSError **) error;
```

## Return Value

A new dictionary that contains the dictionary at `url`, or `nil` if there is an error or if the contents of the resource are an invalid representation of a dictionary.

## Discussion

The dictionary representation in the file identified by path must contain only property list objects ([`NSString`](../nsstring.md), [`NSData`](../nsdata.md), [`NSDate`](../nsdate.md), [`NSNumber`](../nsnumber.md), [`NSArray`](../nsarray.md), or [`NSDictionary`](../nsdictionary.md) objects). For more details, see [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i). The objects contained by this dictionary are immutable, even if the dictionary is mutable.

## Parameters

- `url`: A URL that identifies a resource containing a string representation of a property list whose root object is a dictionary.

## See Also

### Creating a Dictionary from an External Source
- [+ dictionaryWithContentsOfFile:](./dictionarywithcontentsoffile_.md)
  Creates a dictionary using the keys and values found in a file specified by a given path.
- [convenience init?(contentsOfFile: String)](./init%28contentsoffile%29.md)
  Initializes a newly allocated dictionary using the keys and values found in a file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/dictionarywithcontentsofurl:error:)*