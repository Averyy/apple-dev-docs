# icon

**Framework**: Foundation  
**Kind**: property

The icon that represents the file wrapper.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var icon: NSImage? { get set }
```

#### Discussion

You don’t have to use this icon; for example, a file viewer typically looks up icons automatically based on file extensions, and so wouldn’t need this one. Similarly, if a file wrapper represents an image file, you can display the image directly rather than a file icon.

This method may return `nil` if the file wrapper is a child created when its parent was read from the file system, and the child was modified before it was read. Use the `NSFileWrapperReadingImmediate` reading option to reduce the likelihood of that problem.

Because the `NSImage` object that’s returned might be shared by many [`FileWrapper`](filewrapper.md) objects, you must not mutate it. If you need to mutate the returned object, make a copy first and mutate the copy instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/icon)*