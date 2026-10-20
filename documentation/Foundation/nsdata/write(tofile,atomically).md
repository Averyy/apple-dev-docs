# write(toFile:atomically:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Writes the data object’s bytes to the file specified by a given path.

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
func write(toFile path: String, atomically useAuxiliaryFile: Bool) -> Bool
```

```objc
- (BOOL) writeToFile:(NSString *) path atomically:(BOOL) useAuxiliaryFile;
```

#### Return Value

[`true`](../../Swift/true.md) if the operation succeeds, otherwise [`false`](../../Swift/false.md).

#### Discussion

This method may not be appropriate when writing to publicly accessible files. To securely write data to a public location, use [`FileHandle`](../filehandle.md) instead. For more information, see [Securing File Operations](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/RaceConditions.html#//apple_ref/doc/uid/TP40002585-SW9) in [Secure Coding Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Introduction.html#//apple_ref/doc/uid/TP40002415).

## Parameters

- `path`: The location to which to write the receiver’s bytes. If `path` contains a tilde (~) character, you must expand it with [`expandingTildeInPath`](../nsstring/expandingtildeinpath.md) before invoking this method.
- `useAuxiliaryFile`: If [`true`](../../Swift/true.md), the data is written to a backup file, and then—assuming no errors occur—the backup file is renamed to the name specified by `path`; otherwise, the data is written directly to `path`.

## See Also

### Writing Data to a File
- [func write(toFile: String, options: NSData.WritingOptions) throws](./write%28tofile,options%29.md)
  Writes the data object’s bytes to the file specified by a given path.
- [func write(to: URL, atomically: Bool) -> Bool](./write%28to,atomically%29.md)
  Writes the data object’s bytes to the location specified by a given URL.
- [func write(to: URL, options: NSData.WritingOptions) throws](./write%28to,options%29.md)
  Writes the data object’s bytes to the location specified by a given URL.
- [NSData.WritingOptions](./writingoptions.md)
  Options for methods used to write data objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/write(tofile:atomically:))*