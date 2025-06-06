# init(name:bundle:)

**Framework**: AppKit  
**Kind**: init

Creates a storyboard based on the named storyboard file in the specified bundle.

**Availability**:
- macOS 10.10+

## Declaration

```swift
convenience init(name: NSStoryboard.Name, bundle storyboardBundleOrNil: Bundle?)
```

#### Return Value

A new storyboard object.

## Parameters

- `name`: The name of the storyboard file, without the filename extension. This method raises an exception if this parameter’s value is  .
- `storyboardBundleOrNil`: The bundle used to resolve references to resources, typically images, in the archived controllers represented in the storyboard file. If you specify  , AppKit uses the app’s main bundle.

## See Also

- [class var main: NSStoryboard?](nsstoryboard/main.md)
  The app’s main storyboard.
- [NSStoryboard.Name](nsstoryboard/name.md)
  The name of the storyboard file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstoryboard/init(name:bundle:))*