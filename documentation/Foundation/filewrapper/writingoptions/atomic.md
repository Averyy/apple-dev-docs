# atomic

**Framework**: Foundation  
**Kind**: property

Whether writing is done atomically.

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
static var atomic: FileWrapper.WritingOptions { get }
```

#### Discussion

You can use this option to ensure that, when overwriting a file package, the overwriting either completely succeeds or completely fails, with no possibility of leaving the file package in an inconsistent state. Because this option causes additional I/O, you shouldn’t use it unnecessarily. For example, don’t use this option in an override of `-[NSDocument` [`write(to:ofType:)`](https://developer.apple.com/documentation/AppKit/NSDocument/write(to:ofType:))`]`, because `NSDocument` safe-saving is already done atomically.

## See Also

- [static var withNameUpdating: FileWrapper.WritingOptions](filewrapper/writingoptions/withnameupdating.md)
  Whether descendant file wrappers’[`filename`](filewrapper/filename.md) properties are set if the writing succeeds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/writingoptions/atomic)*