# url

**Framework**: AppKit  
**Kind**: property

The path value displayed by the receiver.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var url: URL? { get set }
```

#### Discussion

When setting, an array of `NSPathComponentCell` objects is automatically set based on the path in `url`. If `url` is a file URL (returns [`true`](https://developer.apple.com/documentation/swift/true) from [`isFileURL`](https://developer.apple.com/documentation/Foundation/NSURL/isFileURL)), the images are automatically filled with file icons, if the path exists. The URL value itself is stored in the `objectValue` property of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcontrol/url)*