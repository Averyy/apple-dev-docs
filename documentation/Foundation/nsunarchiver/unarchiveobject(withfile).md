# unarchiveObject(withFile:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Decodes and returns the object archived in the file `path`.

**Availability**:
- iOS 2.0+ - Deprecated in 11.0
- iPadOS 2.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use NSKeyedUnarchiver instead

## Declaration

```swift
class func unarchiveObject(withFile path: String) -> Any?
```

```objc
+ (id) unarchiveObjectWithFile:(NSString *) path;
```

## Return Value

The object, or object graph, that was archived in the file at `path`. Returns `nil` if the file at `path` cannot be unarchived.

## Discussion

This convenience method reads the file by invoking the `NSData` method [`dataWithContentsOfFile:`](../nsdata/datawithcontentsoffile_.md) and then invokes [`unarchiveObject(with:)`](./unarchiveobject%28with%29.md).

## Parameters

- `path`: The path to a file than contains an archive created using [`NSArchiver`](../nsarchiver.md).

## See Also

### Decoding objects
- [class func unarchiveObject(with: Data) -> Any?](./unarchiveobject%28with%29.md)
  Decodes and returns the object archived in a given `NSData` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsunarchiver/unarchiveobject(withfile:))*