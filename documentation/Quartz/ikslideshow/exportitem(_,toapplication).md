# exportItem(_:toApplication:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Type Method

Exports a slideshow item to the application that has the provided bundle identifier.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class func exportItem(_ item: Any!, toApplication applicationBundleIdentifier: String!)
```

```objc
+ (void) exportSlideshowItem:(id) item toApplication:(NSString *) applicationBundleIdentifier;
```

## Parameters

- `item`: The item to export
- `applicationBundleIdentifier`: The bundle identifier of the application that you want to export the item to.

## See Also

### Exporting Slideshow Items
- [class func canExport(toApplication: String!) -> Bool](./canexport%28toapplication%29.md)
  Finds out whether the slideshow can export its contents to an application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikslideshow/exportitem(_:toapplication:))*