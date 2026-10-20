# init(contentsOfFile:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a newly allocated dictionary using the keys and values found in a file at a given path.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.0+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

## Declaration

```swift
convenience init?(contentsOfFile path: String)
```

```objc
- (NSDictionary<id,id> *) initWithContentsOfFile:(NSString *) path;
```

#### Return Value

An initialized dictionary—which might be different than the original receiver—that contains the dictionary at `path`, or `nil` if there is a file error or if the contents of the file are an invalid representation of a dictionary.

#### Discussion

The dictionary representation in the file identified by `path` must contain only property list objects (`NSString`, `NSData`, `NSDate`, `NSNumber`, `NSArray`, or `NSDictionary` objects). For more details, see [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i). The objects contained by this dictionary are immutable, even if the dictionary is mutable.

## Parameters

- `path`: A full or relative pathname. The file identified by `path` must contain a string representation of a property list whose root object is a dictionary.

## See Also

### Creating a Dictionary from an External Source
- [convenience init(contentsOfURL: URL, error: ()) throws](./init%28contentsofurl,error%29.md)
  Initializes a newly allocated dictionary using the keys and values found at a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/init(contentsoffile:))*