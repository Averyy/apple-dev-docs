# withNameUpdating

**Framework**: Foundation  
**Kind**: property

Whether descendant file wrappers’[`filename`](filewrapper/filename.md) properties are set if the writing succeeds.

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
static var withNameUpdating: FileWrapper.WritingOptions { get }
```

#### Discussion

This option is necessary when your application passes a URL in the `originalContentsURL` parameter to the [`write(to:options:originalContentsURL:)`](filewrapper/write(to:options:originalcontentsurl:).md) method. Without using this option (and reusing child file wrappers properly), subsequent invocations of [`write(to:options:originalContentsURL:)`](filewrapper/write(to:options:originalcontentsurl:).md) would not be able to reliably create hard links in a new file package, because the record of names in the old file package would be out of date.

## See Also

- [static var atomic: FileWrapper.WritingOptions](filewrapper/writingoptions/atomic.md)
  Whether writing is done atomically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/writingoptions/withnameupdating)*