# write(toFile:atomically:)

**Framework**: Foundation  
**Kind**: method

Writes a property list representation of the contents of the dictionary to a given path.

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
func write(toFile path: String, atomically useAuxiliaryFile: Bool) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the file is written successfully, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method recursively validates that all the contained objects are property list objects (instances of `NSData`, `NSDate`, `NSNumber`, `NSString`, `NSArray`, or `NSDictionary`) before writing out the file, and returns [`false`](https://developer.apple.com/documentation/Swift/false) if all the objects are not property list objects, since the resultant file would not be a valid property list.

If the dictionary’s contents are all property list objects, the file written by this method can be used to initialize a new dictionary with the class method [`dictionaryWithContentsOfFile:`](nsdictionary/dictionarywithcontentsoffile:.md) or the instance method [`init(contentsOfFile:)`](nsdictionary/init(contentsoffile:).md).

If you need greater control over the property list representation, use [`PropertyListSerialization`](propertylistserialization.md) instead.

For more information about property lists, see [`Property List Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i).

## Parameters

- `path`: If   contains a tilde (~) character, you must expand it with   before invoking this method.
- `useAuxiliaryFile`: If   is  , the dictionary is written to an auxiliary file, and then the auxiliary file is renamed to  . If   is  , the dictionary is written directly to  . The   option guarantees that  , if it exists at all, won’t be corrupted even if the system should crash during writing.

## See Also

- [func write(to: URL) throws](nsdictionary/write(to:).md)
  Writes a property list representation of the contents of the dictionary to a given URL.
- [func write(to: URL, atomically: Bool) -> Bool](nsdictionary/write(to:atomically:).md)
  Writes a property list representation of the contents of the dictionary to a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/write(tofile:atomically:))*