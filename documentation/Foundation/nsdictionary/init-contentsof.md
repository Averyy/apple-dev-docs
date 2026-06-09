# init(contentsOf:)

**Framework**: Foundation  
**Kind**: init

Initializes a newly allocated dictionary using the keys and values found at a given URL.

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
convenience init?(contentsOf url: URL)
```

#### Return Value

An initialized dictionary—which might be different than the original receiver—that contains the dictionary at `url`, or `nil` if there is an error or if the contents of the resource are an invalid representation of a dictionary.

#### Discussion

The dictionary representation in the file identified by `url` must contain only property list objects (`NSString`, `NSData`, `NSDate`, `NSNumber`, `NSArray`, or `NSDictionary` objects). For more details, see [`Property List Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i). The objects contained by this dictionary are immutable, even if the dictionary is mutable.

> **Note**: Use [`init(contentsOfURL:error:)`](nsdictionary/init(contentsofurl:error:).md) instead.

## Parameters

- `url`: An URL that identifies a resource containing a string representation of a property list whose root object is a dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/init(contentsof:))*