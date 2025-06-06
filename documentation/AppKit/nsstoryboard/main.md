# main

**Framework**: AppKit  
**Kind**: property

The app’s main storyboard.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class var main: NSStoryboard? { get }
```

#### Discussion

The name of the main storyboard is stored in the [`NSMainStoryboardFile`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMainStoryboardFile) key of the app’s `Info.plist` file.

## See Also

- [convenience init(name: NSStoryboard.Name, bundle: Bundle?)](nsstoryboard/init(name:bundle:).md)
  Creates a storyboard based on the named storyboard file in the specified bundle.
- [NSStoryboard.Name](nsstoryboard/name.md)
  The name of the storyboard file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstoryboard/main)*