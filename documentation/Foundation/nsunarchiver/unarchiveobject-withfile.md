# unarchiveObject(withFile:)

**Framework**: Foundation  
**Kind**: method

Decodes and returns the object archived in the file `path`.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
class func unarchiveObject(withFile path: String) -> Any?
```

#### Return Value

The object, or object graph, that was archived in the file at `path`. Returns `nil` if the file at `path` cannot be unarchived.

#### Discussion

This convenience method reads the file by invoking the `NSData` method [`dataWithContentsOfFile:`](nsdata/datawithcontentsoffile:.md) and then invokes [`unarchiveObject(with:)`](nsunarchiver/unarchiveobject(with:).md).

## Parameters

- `path`: The path to a file than contains an archive created using  .

## See Also

- [class func unarchiveObject(with: Data) -> Any?](nsunarchiver/unarchiveobject(with:).md)
  Decodes and returns the object archived in a given `NSData` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsunarchiver/unarchiveobject(withfile:))*