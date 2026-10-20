# propertyListFromStringsFileFormat()

**Framework**: Foundation  
**Kind**: method

Returns a dictionary object initialized with the keys and values found in the receiver.

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
func propertyListFromStringsFileFormat() -> [AnyHashable : Any]?
```

#### Return Value

A dictionary object initialized with the keys and values found in the receiver

#### Discussion

The receiver must contain text in the format used for `.strings` files. In this format, keys and values are separated by an equal sign, and each key-value pair is terminated with a semicolon. The value is optional—if not present, the equal sign is also omitted. The keys and values themselves are always strings enclosed in straight quotation marks. Comments may be included, delimited by `/*` and `*/` as for ANSI C comments. Here’s a short example of a strings file:

```objc
/* Question in confirmation panel for quitting. */
"Confirm Quit" = "Are you sure you want to quit?";
 
/* Message when user tries to close unsaved document */
"Close or Save" = "Save changes before closing?";
 
/* Word for Cancel */
"Cancel";
```

## See Also

- [class func string(withContentsOfFile: String) -> Any?](nsstring/string(withcontentsoffile:).md)
  Returns a string created by reading data from the file named by a given path.
- [func propertyList() -> Any](nsstring/propertylist.md)
  Parses the receiver as a text representation of a property list, returning an `NSString`, `NSData`, `NSArray`, or `NSDictionary` object, according to the topmost element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/propertylistfromstringsfileformat())*