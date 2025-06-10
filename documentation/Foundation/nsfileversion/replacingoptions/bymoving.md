# byMoving

**Framework**: Foundation  
**Kind**: property

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
static var byMoving: NSFileVersion.ReplacingOptions { get }
```

#### Discussion

When replacing a file, move the old version of the file out of the version store instead of copying the new contents into the file’s version. You should use this option in conjunction with a file coordinator to make sure the operation is coordinated with other clients of the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileversion/replacingoptions/bymoving)*