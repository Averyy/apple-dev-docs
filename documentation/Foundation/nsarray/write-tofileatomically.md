# write(toFile:atomically:)

**Framework**: Foundation  
**Kind**: method

Writes the contents of the array to a file at a given path.

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

[`true`](https://developer.apple.com/documentation/swift/true) if the file is written successfully, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

If the array’s contents are all property list objects (`NSString`, `NSData`, `NSArray`, or `NSDictionary` objects), the file written by this method can be used to initialize a new array with the class method [`arrayWithContentsOfFile:`](nsarray/arraywithcontentsoffile:.md) or the instance method [`init(contentsOfFile:)`](nsarray/init(contentsoffile:).md). This method recursively validates that all the contained objects are property list objects before writing out the file, and returns [`false`](https://developer.apple.com/documentation/swift/false) if all the objects are not property list objects, since the resultant file would not be a valid property list.

## Parameters

- `path`: If   contains a tilde (~) character, you must expand it with   before invoking this method.
- `useAuxiliaryFile`: If  , the array is written to an auxiliary file, and then the auxiliary file is renamed to  . If  , the array is written directly to  . The   option guarantees that  , if it exists at all, won’t be corrupted even if the system should crash during writing.

## See Also

- [convenience init?(contentsOfFile: String)](nsarray/init(contentsoffile:).md)
  Initializes a newly allocated array with the contents of the file specified by a given path.
- [func write(to: URL, atomically: Bool) -> Bool](nsarray/write(to:atomically:).md)
  Writes the contents of the array to the location specified by a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/write(tofile:atomically:))*