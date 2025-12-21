# withoutMapping

**Framework**: Foundation  
**Kind**: property

Whether file mapping for regular file wrappers is disallowed.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var withoutMapping: FileWrapper.ReadingOptions { get }
```

#### Discussion

You can use this option to keep `NSFileWrapper` from memory-mapping files. This is useful if you want to make sure your application doesn’t hold files open (mapped files are open files), therefore preventing the user from ejecting DVDs, unmounting disk partitions, or unmounting disk images. In macOS 10.6 and later, `NSFileWrapper` memory-maps files that are on internal drives only. It never memory-maps files on external drives or network volumes, regardless of whether this option is used.

## See Also

- [static var immediate: FileWrapper.ReadingOptions](filewrapper/readingoptions/immediate.md)
  The option to read files immediately after creating a file wrapper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/readingoptions/withoutmapping)*