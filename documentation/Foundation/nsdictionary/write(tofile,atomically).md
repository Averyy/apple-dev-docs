# write(toFile:atomically:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Writes a property list representation of the contents of the dictionary to a given path.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.0+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [`write(to:)`](./write%28to%29.md) instead.

## Declaration

```swift
func write(toFile path: String, atomically useAuxiliaryFile: Bool) -> Bool
```

```objc
- (BOOL) writeToFile:(NSString *) path atomically:(BOOL) useAuxiliaryFile;
```

#### Return Value

[`true`](../../Swift/true.md) if the file is written successfully, otherwise [`false`](../../Swift/false.md).

#### Discussion

This method recursively validates that all the contained objects are property list objects (instances of `NSData`, `NSDate`, `NSNumber`, `NSString`, `NSArray`, or `NSDictionary`) before writing out the file, and returns [`false`](../../Swift/false.md) if all the objects are not property list objects, since the resultant file would not be a valid property list.

If the dictionary’s contents are all property list objects, the file written by this method can be used to initialize a new dictionary with the class method [`dictionaryWithContentsOfFile:`](./dictionarywithcontentsoffile_.md) or the instance method [`init(contentsOfFile:)`](./init%28contentsoffile%29.md).

If you need greater control over the property list representation, use [`PropertyListSerialization`](../propertylistserialization.md) instead.

For more information about property lists, see [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i).

## Parameters

- `path`: The path at which to write the file.

  If `path` contains a tilde (~) character, you must expand it with [`expandingTildeInPath`](../nsstring/expandingtildeinpath.md) before invoking this method.
- `useAuxiliaryFile`: A flag that specifies whether the file should be written atomically.

  If `useAuxiliaryFile` is [`true`](../../Swift/true.md), the dictionary is written to an auxiliary file, and then the auxiliary file is renamed to `path`. If `useAuxiliaryFile` is [`false`](../../Swift/false.md), the dictionary is written directly to `path`. The [`true`](../../Swift/true.md) option guarantees that `path`, if it exists at all, won’t be corrupted even if the system should crash during writing.

## See Also

### Storing Dictionaries
- [func write(to: URL) throws](./write%28to%29.md)
  Writes a property list representation of the contents of the dictionary to a given URL.
- [func write(to: URL, atomically: Bool) -> Bool](./write%28to,atomically%29.md)
  Writes a property list representation of the contents of the dictionary to a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/write(tofile:atomically:))*