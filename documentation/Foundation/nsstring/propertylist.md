# propertyList()

**Framework**: Foundation  
**Kind**: method

Parses the receiver as a text representation of a property list, returning an `NSString`, `NSData`, `NSArray`, or `NSDictionary` object, according to the topmost element.

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
func propertyList() -> Any
```

#### Return Value

A property list representation of returning an `NSString`, `NSData`, `NSArray`, or `NSDictionary` object, according to the topmost element.

#### Discussion

The receiver must contain a string in a property list format. For a discussion of property list formats, see [`Property List Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i).

> ❗ **Important**:  Raises an `NSParseErrorException` if the receiver cannot be parsed as a property list.

## See Also

- [class func string(withContentsOfFile: String) -> Any?](nsstring/string(withcontentsoffile:).md)
  Returns a string created by reading data from the file named by a given path.
- [func propertyListFromStringsFileFormat() -> [AnyHashable : Any]?](nsstring/propertylistfromstringsfileformat.md)
  Returns a dictionary object initialized with the keys and values found in the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/propertylist())*