# main

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The app’s main storyboard.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class var main: NSStoryboard? { get }
```

```objc
@property (class, strong, readonly, nullable) NSStoryboard * mainStoryboard;
```

## Discussion

The name of the main storyboard is stored in the [`NSMainStoryboardFile`](../../BundleResources/information-property-list/nsmainstoryboardfile.md) key of the app’s `Info.plist` file.

## See Also

### Creating a Storyboard Object
- [convenience init(name: NSStoryboard.Name, bundle: Bundle?)](./init%28name,bundle%29.md)
  Creates a storyboard based on the named storyboard file in the specified bundle.
- [NSStoryboard.Name](./name.md)
  The name of the storyboard file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstoryboard/main)*