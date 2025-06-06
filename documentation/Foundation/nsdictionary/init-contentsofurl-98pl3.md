# init(contentsOfURL:)

**Framework**: Foundation  
**Kind**: init

Creates a dictionary using the keys and values found in a resource specified by a given URL.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(contentsOfURL url: URL)
```

#### Return Value

A new dictionary that contains the dictionary at `aURL`, or `nil` if there is an error or if the contents of the resource are an invalid representation of a dictionary.

#### Discussion

The dictionary representation in the file identified by `aURL` must contain only property list objects (`NSString`, `NSData`, `NSDate`, `NSNumber`, `NSArray`, or `NSDictionary` objects). For more details, see [`Property List Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i). The objects contained by this dictionary are immutable, even if the dictionary is mutable.

## Parameters

- `url`: An URL that identifies a resource containing a string representation of a property list whose root object is a dictionary.

## See Also

- [convenience init(contentsOfURL: URL, error: ()) throws](nsdictionary/init(contentsofurl:error:).md)
  Initializes a newly allocated dictionary using the keys and values found at a given URL.
- [convenience init?(contentsOfURL: URL)](nsdictionary/init(contentsofurl:)-4pv16.md)
  Initializes a newly allocated dictionary using the keys and values found at a given URL.
- [convenience init?(contentsOfFile: String)](nsdictionary/init(contentsoffile:).md)
  Initializes a newly allocated dictionary using the keys and values found in a file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/init(contentsofurl:)-98pl3)*