# write(toFile:atomically:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Writes the contents of the array to a file at a given path.

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
func write(toFile path: String, atomically useAuxiliaryFile: Bool) -> Bool
```

```objc
- (BOOL) writeToFile:(NSString *) path atomically:(BOOL) useAuxiliaryFile;
```

## Return Value

[`true`](../../Swift/true.md) if the file is written successfully, otherwise [`false`](../../Swift/false.md).

## Discussion

If the array’s contents are all property list objects (`NSString`, `NSData`, `NSArray`, or `NSDictionary` objects), the file written by this method can be used to initialize a new array with the class method [`arrayWithContentsOfFile:`](./arraywithcontentsoffile_.md) or the instance method [`init(contentsOfFile:)`](./init%28contentsoffile%29.md). This method recursively validates that all the contained objects are property list objects before writing out the file, and returns [`false`](../../Swift/false.md) if all the objects are not property list objects, since the resultant file would not be a valid property list.

## Parameters

- `path`: The path at which to write the contents of the array.

  If `path` contains a tilde (~) character, you must expand it with [`expandingTildeInPath`](../nsstring/expandingtildeinpath.md) before invoking this method.
- `useAuxiliaryFile`: If [`true`](../../Swift/true.md), the array is written to an auxiliary file, and then the auxiliary file is renamed to `path`. If [`false`](../../Swift/false.md), the array is written directly to `path`. The [`true`](../../Swift/true.md) option guarantees that `path`, if it exists at all, won’t be corrupted even if the system should crash during writing.

## See Also

### Related Documentation
- [convenience init?(contentsOfFile: String)](./init%28contentsoffile%29.md)
  Initializes a newly allocated array with the contents of the file specified by a given path.
### Storing Arrays
- [func write(to: URL, atomically: Bool) -> Bool](./write%28to,atomically%29.md)
  Writes the contents of the array to the location specified by a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/write(tofile:atomically:))*