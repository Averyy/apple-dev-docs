# write(to:atomically:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Writes the data object’s bytes to the location specified by a given URL.

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
func write(to url: URL, atomically: Bool) -> Bool
```

```objc
- (BOOL) writeToURL:(NSURL *) url atomically:(BOOL) atomically;
```

#### Return Value

[`true`](../../Swift/true.md) if the operation succeeds, otherwise [`false`](../../Swift/false.md).

#### Discussion

Since at present only `file://` URLs are supported, there is no difference between this method and [`write(toFile:atomically:)`](./write%28tofile,atomically%29.md), except for the type of the first argument.

This method may not be appropriate when writing to publicly accessible files. To securely write data to a public location, use [`FileHandle`](../filehandle.md) instead. For more information, see [Securing File Operations](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/RaceConditions.html#//apple_ref/doc/uid/TP40002585-SW9) in [Secure Coding Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Introduction.html#//apple_ref/doc/uid/TP40002415).

## Parameters

- `url`: The location to which to write the receiver’s bytes. Only `file://` URLs are supported.
- `atomically`: If [`true`](../../Swift/true.md), the data is written to a backup location, and then—assuming no errors occur—the backup location is renamed to the name specified by `aURL`; otherwise, the data is written directly to `aURL`. `atomically` is ignored if `aURL` is not of a type the supports atomic writes.

## See Also

### Writing Data to a File
- [func write(toFile: String, atomically: Bool) -> Bool](./write%28tofile,atomically%29.md)
  Writes the data object’s bytes to the file specified by a given path.
- [func write(toFile: String, options: NSData.WritingOptions) throws](./write%28tofile,options%29.md)
  Writes the data object’s bytes to the file specified by a given path.
- [func write(to: URL, options: NSData.WritingOptions) throws](./write%28to,options%29.md)
  Writes the data object’s bytes to the location specified by a given URL.
- [NSData.WritingOptions](./writingoptions.md)
  Options for methods used to write data objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/write(to:atomically:))*