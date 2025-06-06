# write(toFile:atomically:)

**Framework**: Foundation  
**Kind**: method

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

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the operation succeeds, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method may not be appropriate when writing to publicly accessible files. To securely write data to a public location, use [`FileHandle`](filehandle.md) instead. For more information, see [`Securing File Operations`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/RaceConditions.html#//apple_ref/doc/uid/TP40002585-SW9) in [`Secure Coding Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Introduction.html#//apple_ref/doc/uid/TP40002415).

## Parameters

- `path`: The location to which to write the receiver’s bytes. If   contains a tilde (~) character, you must expand it with   before invoking this method.
- `useAuxiliaryFile`: If  , the data is written to a backup file, and then—assuming no errors occur—the backup file is renamed to the name specified by  ; otherwise, the data is written directly to  .

## See Also

- [func write(toFile: String, options: NSData.WritingOptions) throws](nsdata/write(tofile:options:).md)
  Writes the data object’s bytes to the file specified by a given path.
- [func write(to: URL, atomically: Bool) -> Bool](nsdata/write(to:atomically:).md)
  Writes the data object’s bytes to the location specified by a given URL.
- [func write(to: URL, options: NSData.WritingOptions) throws](nsdata/write(to:options:).md)
  Writes the data object’s bytes to the location specified by a given URL.
- [NSData.WritingOptions](nsdata/writingoptions.md)
  Options for methods used to write data objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/write(tofile:atomically:))*